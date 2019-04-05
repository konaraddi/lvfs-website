#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# Copyright (C) 2019 Richard Hughes <richard@hughsie.com>
# Licensed under the GNU General Public License Version 2

from flask import request, url_for, redirect, flash, g, render_template
from flask_login import login_required

from app import app, db

from .models import Category
from .util import _error_internal, _error_permission_denied

@app.route('/lvfs/category/all')
@login_required
def category_all():

    # security check
    if not g.user.check_acl('@view-categories'):
        return _error_permission_denied('Unable to view categories')

    # only show categories with the correct group_id
    categories = db.session.query(Category).order_by(Category.category_id.asc()).all()
    return render_template('category-list.html', categories=categories)

@app.route('/lvfs/category/add', methods=['POST'])
@login_required
def category_add():

    # security check
    if not Category('').check_acl('@create'):
        return _error_permission_denied('Unable to add category')

    # ensure has enough data
    if 'value' not in request.form:
        return _error_internal('No form data found!')
    value = request.form['value']
    if not value or not value.startswith('X-') or value.find(' ') != -1:
        flash('Failed to add category: Value needs to be a valid group name', 'warning')
        return redirect(url_for('.category_all'))

    # already exists
    if db.session.query(Category).filter(Category.value == value).first():
        flash('Failed to add category: The category already exists', 'info')
        return redirect(url_for('.category_all'))

    # add category
    cat = Category(value=request.form['value'])
    db.session.add(cat)
    db.session.commit()
    flash('Added category', 'info')
    return redirect(url_for('.category_details', category_id=cat.category_id))

@app.route('/lvfs/category/<int:category_id>/delete')
@login_required
def category_delete(category_id):

    # get category
    cat = db.session.query(Category).\
            filter(Category.category_id == category_id).first()
    if not cat:
        flash('No category found', 'info')
        return redirect(url_for('.category_all'))

    # security check
    if not cat.check_acl('@modify'):
        return _error_permission_denied('Unable to delete category')

    # delete
    db.session.delete(cat)
    db.session.commit()
    flash('Deleted category', 'info')
    return redirect(url_for('.category_all'))

@app.route('/lvfs/category/<int:category_id>/modify', methods=['POST'])
@login_required
def category_modify(category_id):

    # find category
    cat = db.session.query(Category).\
                filter(Category.category_id == category_id).first()
    if not cat:
        flash('No category found', 'info')
        return redirect(url_for('.category_all'))

    # security check
    if not cat.check_acl('@modify'):
        return _error_permission_denied('Unable to modify category')

    # modify category
    for key in ['name', 'fallbacks']:
        if key in request.form:
            setattr(cat, key, request.form[key])
    db.session.commit()

    # success
    flash('Modified category', 'info')
    return redirect(url_for('.category_details', category_id=category_id))

@app.route('/lvfs/category/<int:category_id>/details')
@login_required
def category_details(category_id):

    # find category
    cat = db.session.query(Category).\
            filter(Category.category_id == category_id).first()
    if not cat:
        flash('No category found', 'info')
        return redirect(url_for('.category_all'))

    # security check
    if not cat.check_acl('@view'):
        return _error_permission_denied('Unable to view category details')

    # show details
    return render_template('category-details.html', cat=cat)