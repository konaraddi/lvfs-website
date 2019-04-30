#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# Copyright (C) 2015-2018 Richard Hughes <richard@hughsie.com>
# Licensed under the GNU General Public License Version 2
#
# pylint: disable=singleton-comparison,wrong-import-position

import os
import sys
import hashlib
import datetime

import gi
gi.require_version('AppStreamGlib', '1.0')
from gi.repository import AppStreamGlib
gi.require_version('GCab', '1.0')
from gi.repository import GCab
from gi.repository import Gio
from gi.repository import GLib

import app as application   #lgtm [py/import-and-import-from]
from app import db, ploader

from app.dbutils import _execute_count_star
from app.models import Remote, Firmware, Vendor, Client, AnalyticVendor
from app.models import AnalyticFirmware, Useragent, UseragentKind, Analytic, Report
from app.models import _get_datestr_from_datetime
from app.metadata import _metadata_update_targets, _metadata_update_pulp
from app.util import _archive_get_files_from_glob, _get_dirname_safe, _event_log
from app.pluginloader import PluginError

# make compatible with Flask
app = application.app

def _regenerate_and_sign_metadata():

    # get list of dirty remotes
    remotes = []
    for r in db.session.query(Remote).all():
        if not r.is_signed:
            continue
        # fix up any remotes that are not dirty, but have firmware that is dirty
        # -- which shouldn't happen, but did...
        if not r.is_dirty:
            for fw in r.fws:
                if not fw.is_dirty:
                    continue
                print('Marking remote %s as dirty due to %u' % (r.name, fw.firmware_id))
                r.is_dirty = True
        if r.is_dirty:
            remotes.append(r)

    # nothing to do
    if not len(remotes):
        return

    # update everything required
    for r in remotes:
        print('Updating: %s' % r.name)
    _metadata_update_targets(remotes)
    for r in remotes:
        if r.name == 'stable':
            _metadata_update_pulp()

    # sign and sync
    download_dir = app.config['DOWNLOAD_DIR']
    for r in remotes:
        ploader.file_modified(os.path.join(download_dir, r.filename))

    # mark as no longer dirty
    for r in remotes:
        r.is_dirty = False
        db.session.commit()

    # drop caches in other sessions
    db.session.expire_all()

    # log what we did
    for r in remotes:
        _event_log('Signed metadata %s' % r.name)

def _sign_md(cfarchive, cf):
    # parse each metainfo file
    try:
        component = AppStreamGlib.App.new()
        component.parse_data(cf.get_bytes(), AppStreamGlib.AppParseFlags.NONE)
    except Exception as e:
        raise NotImplementedError('Invalid metadata in %s: %s' % (cf.get_name(), str(e)))

    # sign each firmware
    release = component.get_release_default()
    csum = release.get_checksum_by_target(AppStreamGlib.ChecksumTarget.CONTENT)
    if not csum:
        csum = AppStreamGlib.Checksum.new()
        csum.set_filename('firmware.bin')

    # get the filename including the correct dirname
    fn = os.path.join(_get_dirname_safe(cf.get_name()), csum.get_filename())
    cfs = _archive_get_files_from_glob(cfarchive, fn)
    if not cfs:
        raise NotImplementedError('no %s firmware found in %s' % (fn, cf.get_name()))

    # sign the firmware.bin file
    ploader.archive_sign(cfarchive, cfs[0])

def _sign_fw(fw):

    # load the .cab file
    download_dir = app.config['DOWNLOAD_DIR']
    fn = os.path.join(download_dir, fw.filename)
    try:
        with open(fn, 'rb') as f:
            data = f.read()
    except IOError as e:
        raise NotImplementedError('cannot read %s: %s' % (fn, str(e)))
    istream = Gio.MemoryInputStream.new_from_bytes(GLib.Bytes.new(data))
    cfarchive = GCab.Cabinet.new()
    cfarchive.load(istream)
    cfarchive.extract(None)

    # look for each metainfo file
    cfs = _archive_get_files_from_glob(cfarchive, '*.metainfo.xml')
    if len(cfs) == 0:
        raise NotImplementedError('no .metadata.xml files in %s' % fn)

    # parse each MetaInfo file
    print('Signing: %s' % fn)
    for cf in cfs:
        _sign_md(cfarchive, cf)

    # save the new archive
    ostream = Gio.MemoryOutputStream.new_resizable()
    cfarchive.write_simple(ostream)
    cab_data = Gio.MemoryOutputStream.steal_as_bytes(ostream).get_data()

    # overwrite old file
    with open(fn, 'wb') as f:
        f.write(cab_data)

    # inform the plugin loader
    ploader.file_modified(fn)

    # update the database
    fw.checksum_signed = hashlib.sha1(cab_data).hexdigest()
    fw.signed_timestamp = datetime.datetime.utcnow()
    db.session.commit()

def _regenerate_and_sign_firmware():

    # find all unsigned firmware
    fws = db.session.query(Firmware).\
                        filter(Firmware.signed_timestamp == None).all()
    if not len(fws):
        return

    # sign each firmware in each file
    for fw in fws:
        if fw.is_deleted:
            continue
        print('Signing firmware %u...' % fw.firmware_id)
        _sign_fw(fw)
        _event_log('Signed firmware %s' % fw.firmware_id)

    # drop caches in other sessions
    db.session.expire_all()

def _purge_old_deleted_firmware():

    # find all unsigned firmware
    for fw in db.session.query(Firmware).all():
        if fw.is_deleted and fw.target_duration > datetime.timedelta(days=30*6):
            print('Deleting %s as age %s' % (fw.filename, fw.target_duration))
            path = os.path.join(app.config['RESTORE_DIR'], fw.filename)
            if os.path.exists(path):
                os.remove(path)
            db.session.delete(fw)

    # all done
    db.session.commit()

def _check_firmware():

    # ensure the test has been added for the firmware type
    fws = db.session.query(Firmware).all()
    for fw in fws:
        if fw.is_deleted:
            continue
        ploader.ensure_test_for_fw(fw)
    db.session.commit()

    # make a list of all the tests that need running
    test_fws = []
    for fw in fws:
        for test in fw.tests:
            if test.needs_running:
                test_fws.append((test, fw))

    # mark all the tests as started
    for test, fw in test_fws:
        print('Marking test %s started for firmware %u...' % (test.plugin_id, fw.firmware_id))
        test.started_ts = datetime.datetime.utcnow()
    db.session.commit()

    # process each test
    for test, fw in test_fws:
        plugin = ploader.get_by_id(test.plugin_id)
        if not plugin:
            _event_log('No plugin %s' % test.plugin_id)
            test.ended_ts = datetime.datetime.utcnow()
            continue
        if not hasattr(plugin, 'run_test_on_fw'):
            _event_log('No run_test_on_fw in %s' % test.plugin_id)
            test.ended_ts = datetime.datetime.utcnow()
            continue
        try:
            print('Running test %s for firmware %s' % (test.plugin_id, fw.firmware_id))
            plugin.run_test_on_fw(test, fw)
            test.ended_ts = datetime.datetime.utcnow()
            # don't leave a failed task running
            db.session.commit()
        except PluginError as e:
            test.ended_ts = datetime.datetime.utcnow()
            test.add_fail('An exception occurred', str(e))

    # all done
    db.session.commit()


def _generate_stats_for_vendor(v, datestr):

    # is datestr older than firmware
    if not v.ctime:
        return
    if datestr < _get_datestr_from_datetime(v.ctime - datetime.timedelta(days=1)):
        return

    # get all the firmware for a specific vendor
    fw_ids = []
    for fw in v.fws:
        fw_ids.append(fw.firmware_id)
    if not fw_ids:
        return

    # count how many times any of the firmware files were downloaded
    cnt = _execute_count_star(db.session.query(Client).\
                    filter(Client.firmware_id.in_(fw_ids)).\
                    filter(Client.datestr == datestr))
    analytic = AnalyticVendor(v.vendor_id, datestr, cnt)
    print('adding %s:%s = %i' % (datestr, v.group_id, cnt))
    db.session.add(analytic)

def _generate_stats_for_firmware(fw, datestr):

    # is datestr older than firmware
    if datestr < _get_datestr_from_datetime(fw.timestamp):
        return

    # count how many times any of the firmware files were downloaded
    cnt = _execute_count_star(db.session.query(Client).\
                    filter(Client.firmware_id == fw.firmware_id).\
                    filter(Client.datestr == datestr))
    analytic = AnalyticFirmware(fw.firmware_id, datestr, cnt)
    db.session.add(analytic)

def _generate_stats_firmware_reports(fw):

    # count how many times any of the firmware files were downloaded
    reports_success = 0
    reports_failure = 0
    reports_issue = 0
    for r in db.session.query(Report).\
                    filter(Report.firmware_id == fw.firmware_id).all():
        if r.state == 2:
            reports_success += 1
        if r.state == 3:
            if r.issue_id:
                reports_issue += 1
            else:
                reports_failure += 1

    # update
    fw.report_success_cnt = reports_success
    fw.report_failure_cnt = reports_failure
    fw.report_issue_cnt = reports_issue

def _get_app_from_ua(ua):
    # always exists
    return ua.split(' ')[0]

def _get_fwupd_from_ua(ua):
    for part in ua.split(' '):
        if part.startswith('fwupd/'):
            return part[6:]
    return 'Unknown'

def _get_lang_distro_from_ua(ua):
    start = ua.find('(')
    end = ua.rfind(')')
    if start == -1 or end == -1:
        return None
    parts = ua[start+1:end].split('; ')
    if len(parts) != 3:
        return None
    return (parts[1], parts[2])

def _generate_stats(kinds=None):
    if not kinds:
        kinds = ['FirmwareReport']

    # update FirmwareReport counts
    if 'FirmwareReport' in kinds:
        for fw in db.session.query(Firmware).all():
            _generate_stats_firmware_reports(fw)
        db.session.commit()
    print('generated %s' % ','.join(kinds))

def _generate_stats_for_datestr(datestr, kinds=None):

    if not kinds:
        kinds = ['Analytic',
                 'AnalyticVendor',
                 'AnalyticFirmware',
                 'Useragent']

    # update AnalyticVendor
    if 'AnalyticVendor' in kinds:
        for analytic in db.session.query(AnalyticVendor).filter(AnalyticVendor.datestr == datestr).all():
            db.session.delete(analytic)
        for v in db.session.query(Vendor).all():
            _generate_stats_for_vendor(v, datestr)
        db.session.commit()

    # update AnalyticFirmware
    if 'AnalyticFirmware' in kinds:
        for analytic in db.session.query(AnalyticFirmware).filter(AnalyticFirmware.datestr == datestr).all():
            db.session.delete(analytic)
        for fw in db.session.query(Firmware).all():
            _generate_stats_for_firmware(fw, datestr)
        db.session.commit()

    # update Useragent
    if 'Useragent' in kinds:
        for agnt in db.session.query(Useragent).filter(Useragent.datestr == datestr).all():
            db.session.delete(agnt)
        ua_apps = {}
        ua_fwupds = {}
        ua_distros = {}
        ua_langs = {}
        clients = db.session.query(Client.user_agent).\
                        filter(Client.datestr == datestr).all()
        for res in clients:
            ua = res[0]
            if not ua:
                continue

            # downloader app
            ua_app = _get_app_from_ua(ua)
            if ua_app not in ua_apps:
                ua_apps[ua_app] = 1
            else:
                ua_apps[ua_app] += 1

            # fwupd version
            ua_fwupd = _get_fwupd_from_ua(ua)
            if ua_fwupd not in ua_fwupds:
                ua_fwupds[ua_fwupd] = 1
            else:
                ua_fwupds[ua_fwupd] += 1

            # language and distro
            ua_lang_distro = _get_lang_distro_from_ua(ua)
            if ua_lang_distro:
                ua_lang = ua_lang_distro[0]
                ua_distro = ua_lang_distro[1]
                if ua_lang not in ua_langs:
                    ua_langs[ua_lang] = 1
                else:
                    ua_langs[ua_lang] += 1
                if ua_distro not in ua_distros:
                    ua_distros[ua_distro] = 1
                else:
                    ua_distros[ua_distro] += 1
        for ua in ua_apps:
            db.session.add(Useragent(UseragentKind.APP, ua, datestr, cnt=ua_apps[ua]))
        for ua in ua_fwupds:
            db.session.add(Useragent(UseragentKind.FWUPD, ua, datestr, cnt=ua_fwupds[ua]))
        for ua in ua_langs:
            db.session.add(Useragent(UseragentKind.LANG, ua, datestr, cnt=ua_langs[ua]))
        for ua in ua_distros:
            db.session.add(Useragent(UseragentKind.DISTRO, ua, datestr, cnt=ua_distros[ua]))
        db.session.commit()

    # update Analytic
    if 'Analytic' in kinds:
        analytic = db.session.query(Analytic).filter(Analytic.datestr == datestr).first()
        if analytic:
            db.session.delete(analytic)
        db.session.add(Analytic(datestr, len(clients)))
        db.session.commit()

    # for the log
    print('generated for %s: %s' % (datestr, ','.join(kinds)))

if __name__ == '__main__':

    if len(sys.argv) < 2:
        print('Usage: %s [metadata] [firmware]' % sys.argv[0])
        sys.exit(1)

    # regenerate and sign firmware then metadata
    if 'firmware' in sys.argv:
        try:
            with app.test_request_context():
                _regenerate_and_sign_firmware()
        except NotImplementedError as e:
            print(str(e))
            sys.exit(1)
    if 'metadata' in sys.argv:
        try:
            with app.test_request_context():
                _regenerate_and_sign_metadata()
        except NotImplementedError as e:
            print(str(e))
            sys.exit(1)
    if 'purgedelete' in sys.argv:
        try:
            with app.test_request_context():
                _purge_old_deleted_firmware()
        except NotImplementedError as e:
            print(str(e))
            sys.exit(1)
    if 'fwchecks' in sys.argv:
        try:
            with app.test_request_context():
                _check_firmware()
        except NotImplementedError as e:
            print(str(e))
            sys.exit(1)
    if 'stats' in sys.argv:
        try:
            with app.test_request_context():
                # default to yesterday, but also allow specifying the offset
                days = 1
                if len(sys.argv) > 2:
                    days = int(sys.argv[2])
                val = _get_datestr_from_datetime(datetime.date.today() - datetime.timedelta(days=days))
                _generate_stats_for_datestr(val)
                _generate_stats()
        except NotImplementedError as e:
            print(str(e))
            sys.exit(1)
    if 'statsmigrate' in sys.argv:
        try:
            update_kinds = None
            if len(sys.argv) > 2:
                update_kinds = sys.argv[2:]
            with app.test_request_context():
                for days in range(1, 720):
                    val = _get_datestr_from_datetime(datetime.date.today() - datetime.timedelta(days=days))
                    _generate_stats_for_datestr(val, kinds=update_kinds)
        except NotImplementedError as e:
            print(str(e))
            sys.exit(1)

    # success
    sys.exit(0)
