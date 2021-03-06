"""

Revision ID: c91c4ad6768a
Revises: 43f3d6d89335
Create Date: 2020-01-15 09:22:01.162528

"""

# revision identifiers, used by Alembic.
revision = 'c91c4ad6768a'
down_revision = '43f3d6d89335'

from alembic import op
import sqlalchemy as sa


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('idx_17307_affiliation_id', table_name='affiliation_actions')
    op.drop_index('idx_17307_user_id', table_name='affiliation_actions')
    op.drop_constraint('affiliation_actions_ibfk_2', 'affiliation_actions', type_='foreignkey')
    op.drop_constraint('affiliation_actions_ibfk_1', 'affiliation_actions', type_='foreignkey')
    op.create_foreign_key(None, 'affiliation_actions', 'users', ['user_id'], ['user_id'])
    op.create_foreign_key(None, 'affiliation_actions', 'affiliations', ['affiliation_id'], ['affiliation_id'])
    op.drop_index('idx_17301_vendor_id', table_name='affiliations')
    op.drop_index('idx_17301_vendor_id_odm', table_name='affiliations')
    op.drop_constraint('affiliations_ibfk_1', 'affiliations', type_='foreignkey')
    op.drop_constraint('affiliations_ibfk_2', 'affiliations', type_='foreignkey')
    op.create_foreign_key(None, 'affiliations', 'vendors', ['vendor_id'], ['vendor_id'])
    op.create_foreign_key(None, 'affiliations', 'vendors', ['vendor_id_odm'], ['vendor_id'])
    op.create_index(op.f('ix_analytics_firmware_datestr'), 'analytics_firmware', ['datestr'], unique=False)
    op.create_index(op.f('ix_analytics_firmware_firmware_id'), 'analytics_firmware', ['firmware_id'], unique=False)
    op.drop_index('idx_17333_ix_analytics_firmware_datestr', table_name='analytics_firmware')
    op.drop_index('idx_17333_ix_analytics_firmware_firmware_id', table_name='analytics_firmware')
    op.drop_constraint('analytics_firmware_ibfk_1', 'analytics_firmware', type_='foreignkey')
    op.create_foreign_key(None, 'analytics_firmware', 'firmware', ['firmware_id'], ['firmware_id'])
    op.create_index(op.f('ix_analytics_vendor_datestr'), 'analytics_vendor', ['datestr'], unique=False)
    op.create_index(op.f('ix_analytics_vendor_vendor_id'), 'analytics_vendor', ['vendor_id'], unique=False)
    op.drop_index('idx_17339_ix_analytics_vendor_datestr', table_name='analytics_vendor')
    op.drop_index('idx_17339_ix_analytics_vendor_vendor_id', table_name='analytics_vendor')
    op.drop_constraint('analytics_vendor_ibfk_1', 'analytics_vendor', type_='foreignkey')
    op.create_foreign_key(None, 'analytics_vendor', 'vendors', ['vendor_id'], ['vendor_id'])
    op.drop_index('idx_17354_user_id', table_name='certificates')
    op.drop_constraint('certificates_ibfk_1', 'certificates', type_='foreignkey')
    op.create_foreign_key(None, 'certificates', 'users', ['user_id'], ['user_id'])
    op.drop_index('idx_17363_component_id', table_name='checksums')
    op.drop_constraint('checksums_ibfk_1', 'checksums', type_='foreignkey')
    op.create_foreign_key(None, 'checksums', 'components', ['component_id'], ['component_id'])
    op.create_index(op.f('ix_clients_datestr'), 'clients', ['datestr'], unique=False)
    op.create_index(op.f('ix_clients_firmware_id'), 'clients', ['firmware_id'], unique=False)
    op.create_index(op.f('ix_clients_timestamp'), 'clients', ['timestamp'], unique=False)
    op.drop_index('idx_17372_ix_clients_datestr', table_name='clients')
    op.drop_index('idx_17372_ix_clients_firmware_id', table_name='clients')
    op.drop_index('idx_17372_ix_clients_timestamp', table_name='clients')
    op.drop_constraint('clients_ibfk_1', 'clients', type_='foreignkey')
    op.create_foreign_key(None, 'clients', 'firmware', ['firmware_id'], ['firmware_id'])
    op.drop_index('idx_17391_component_id', table_name='component_claims')
    op.drop_constraint('component_claims_ibfk_1', 'component_claims', type_='foreignkey')
    op.create_foreign_key(None, 'component_claims', 'components', ['component_id'], ['component_id'])
    op.drop_index('idx_17400_component_id', table_name='component_issues')
    op.drop_constraint('component_issues_ibfk_1', 'component_issues', type_='foreignkey')
    op.create_foreign_key(None, 'component_issues', 'components', ['component_id'], ['component_id'])
    op.drop_index('idx_17409_component_id', table_name='component_refs')
    op.drop_index('idx_17409_protocol_id', table_name='component_refs')
    op.drop_index('idx_17409_vendor_id', table_name='component_refs')
    op.drop_index('idx_17409_vendor_id_partner', table_name='component_refs')
    op.drop_constraint('component_refs_ibfk_2', 'component_refs', type_='foreignkey')
    op.drop_constraint('component_refs_ibfk_4', 'component_refs', type_='foreignkey')
    op.drop_constraint('component_refs_ibfk_3', 'component_refs', type_='foreignkey')
    op.drop_constraint('component_refs_ibfk_1', 'component_refs', type_='foreignkey')
    op.create_foreign_key(None, 'component_refs', 'protocol', ['protocol_id'], ['protocol_id'])
    op.create_foreign_key(None, 'component_refs', 'vendors', ['vendor_id_partner'], ['vendor_id'])
    op.create_foreign_key(None, 'component_refs', 'vendors', ['vendor_id'], ['vendor_id'])
    op.create_foreign_key(None, 'component_refs', 'components', ['component_id'], ['component_id'])
    op.drop_index('idx_17427_component_shard_id', table_name='component_shard_certificates')
    op.drop_constraint('component_shard_certificates_ibfk_1', 'component_shard_certificates', type_='foreignkey')
    op.create_foreign_key(None, 'component_shard_certificates', 'component_shards', ['component_shard_id'], ['component_shard_id'])
    op.drop_index('idx_17436_component_shard_id', table_name='component_shard_checksums')
    op.drop_constraint('component_shard_checksums_ibfk_1', 'component_shard_checksums', type_='foreignkey')
    op.create_foreign_key(None, 'component_shard_checksums', 'component_shards', ['component_shard_id'], ['component_shard_id'])
    op.create_index(op.f('ix_component_shard_infos_guid'), 'component_shard_infos', ['guid'], unique=False)
    op.drop_index('idx_17445_ix_component_shard_infos_guid', table_name='component_shard_infos')
    op.create_index(op.f('ix_component_shards_guid'), 'component_shards', ['guid'], unique=False)
    op.drop_index('idx_17418_component_id', table_name='component_shards')
    op.drop_index('idx_17418_component_shard_info_id', table_name='component_shards')
    op.drop_index('idx_17418_ix_component_shards_guid', table_name='component_shards')
    op.drop_constraint('component_shards_ibfk_2', 'component_shards', type_='foreignkey')
    op.drop_constraint('component_shards_ibfk_1', 'component_shards', type_='foreignkey')
    op.create_foreign_key(None, 'component_shards', 'component_shard_infos', ['component_shard_info_id'], ['component_shard_info_id'])
    op.create_foreign_key(None, 'component_shards', 'components', ['component_id'], ['component_id'])
    op.create_index(op.f('ix_components_firmware_id'), 'components', ['firmware_id'], unique=False)
    op.drop_index('idx_17379_components_ibfk_2', table_name='components')
    op.drop_index('idx_17379_components_ibfk_3', table_name='components')
    op.drop_index('idx_17379_components_ibfk_4', table_name='components')
    op.drop_index('idx_17379_ix_components_firmware_id', table_name='components')
    op.drop_constraint('components_ibfk_1', 'components', type_='foreignkey')
    op.drop_constraint('components_ibfk_4', 'components', type_='foreignkey')
    op.drop_constraint('components_ibfk_2', 'components', type_='foreignkey')
    op.drop_constraint('components_ibfk_3', 'components', type_='foreignkey')
    op.create_foreign_key(None, 'components', 'verfmts', ['verfmt_id'], ['verfmt_id'])
    op.create_foreign_key(None, 'components', 'firmware', ['firmware_id'], ['firmware_id'])
    op.create_foreign_key(None, 'components', 'categories', ['category_id'], ['category_id'])
    op.create_foreign_key(None, 'components', 'protocol', ['protocol_id'], ['protocol_id'])
    op.drop_index('idx_17454_issue_id', table_name='conditions')
    op.drop_constraint('conditions_ibfk_1', 'conditions', type_='foreignkey')
    op.create_foreign_key(None, 'conditions', 'issues', ['issue_id'], ['issue_id'])
    op.drop_index('idx_17463_user_id', table_name='event_log')
    op.drop_index('idx_17463_vendor_id', table_name='event_log')
    op.drop_constraint('event_log_ibfk_2', 'event_log', type_='foreignkey')
    op.drop_constraint('event_log_ibfk_1', 'event_log', type_='foreignkey')
    op.create_foreign_key(None, 'event_log', 'vendors', ['vendor_id'], ['vendor_id'])
    op.create_foreign_key(None, 'event_log', 'users', ['user_id'], ['user_id'])
    op.alter_column('firmware', 'checksum_signed_sha1',
               existing_type=sa.VARCHAR(length=40),
               nullable=False)
    op.alter_column('firmware', 'checksum_signed_sha256',
               existing_type=sa.VARCHAR(length=64),
               nullable=False)
    op.alter_column('firmware', 'checksum_upload_sha1',
               existing_type=sa.VARCHAR(length=40),
               nullable=False)
    op.create_index(op.f('ix_firmware_checksum_upload_sha1'), 'firmware', ['checksum_upload_sha1'], unique=False)
    op.drop_index('idx_17474_ix_firmware_checksum_upload', table_name='firmware')
    op.drop_index('idx_17474_remote_id', table_name='firmware')
    op.drop_index('idx_17474_user_id', table_name='firmware')
    op.drop_index('idx_17474_vendor_id', table_name='firmware')
    op.drop_constraint('firmware_ibfk_2', 'firmware', type_='foreignkey')
    op.drop_constraint('firmware_ibfk_1', 'firmware', type_='foreignkey')
    op.drop_constraint('firmware_ibfk_3', 'firmware', type_='foreignkey')
    op.create_foreign_key(None, 'firmware', 'users', ['user_id'], ['user_id'])
    op.create_foreign_key(None, 'firmware', 'vendors', ['vendor_id'], ['vendor_id'])
    op.create_foreign_key(None, 'firmware', 'remotes', ['remote_id'], ['remote_id'])
    op.drop_index('idx_17485_firmware_id', table_name='firmware_events')
    op.drop_index('idx_17485_remote_id', table_name='firmware_events')
    op.drop_index('idx_17485_user_id', table_name='firmware_events')
    op.drop_constraint('firmware_events_ibfk_2', 'firmware_events', type_='foreignkey')
    op.drop_constraint('firmware_events_ibfk_1', 'firmware_events', type_='foreignkey')
    op.drop_constraint('firmware_events_ibfk_3', 'firmware_events', type_='foreignkey')
    op.create_foreign_key(None, 'firmware_events', 'users', ['user_id'], ['user_id'])
    op.create_foreign_key(None, 'firmware_events', 'firmware', ['firmware_id'], ['firmware_id'])
    op.create_foreign_key(None, 'firmware_events', 'remotes', ['remote_id'], ['remote_id'])
    op.drop_index('idx_17491_firmware_id', table_name='firmware_limits')
    op.drop_constraint('firmware_limits_ibfk_1', 'firmware_limits', type_='foreignkey')
    op.create_foreign_key(None, 'firmware_limits', 'firmware', ['firmware_id'], ['firmware_id'])
    op.drop_index('idx_17500_component_id', table_name='guids')
    op.drop_constraint('guids_ibfk_1', 'guids', type_='foreignkey')
    op.create_foreign_key(None, 'guids', 'components', ['component_id'], ['component_id'])
    op.drop_index('idx_17509_vendor_id', table_name='issues')
    op.drop_constraint('issues_ibfk_1', 'issues', type_='foreignkey')
    op.create_foreign_key(None, 'issues', 'vendors', ['vendor_id'], ['vendor_id'])
    op.drop_index('idx_17518_component_id', table_name='keywords')
    op.drop_constraint('keywords_ibfk_1', 'keywords', type_='foreignkey')
    op.create_foreign_key(None, 'keywords', 'components', ['component_id'], ['component_id'])
    op.drop_index('idx_17527_namespace_ibfk_3', table_name='namespaces')
    op.drop_index('idx_17527_vendor_id', table_name='namespaces')
    op.drop_constraint('namespaces_ibfk_1', 'namespaces', type_='foreignkey')
    op.drop_constraint('namespace_ibfk_3', 'namespaces', type_='foreignkey')
    op.create_foreign_key(None, 'namespaces', 'vendors', ['vendor_id'], ['vendor_id'])
    op.create_foreign_key(None, 'namespaces', 'users', ['user_id'], ['user_id'])
    op.drop_index('idx_17536_protocol_ibfk_1', table_name='protocol')
    op.drop_constraint('protocol_ibfk_1', 'protocol', type_='foreignkey')
    op.create_foreign_key(None, 'protocol', 'verfmts', ['verfmt_id'], ['verfmt_id'])
    op.drop_index('idx_17563_report_id', table_name='report_attributes')
    op.drop_constraint('report_attributes_ibfk_1', 'report_attributes', type_='foreignkey')
    op.create_foreign_key(None, 'report_attributes', 'reports', ['report_id'], ['report_id'])
    op.create_index(op.f('ix_reports_firmware_id'), 'reports', ['firmware_id'], unique=False)
    op.drop_index('idx_17554_ix_reports_firmware_id', table_name='reports')
    op.drop_index('idx_17554_user_id', table_name='reports')
    op.drop_constraint('reports_ibfk_1', 'reports', type_='foreignkey')
    op.drop_constraint('reports_ibfk_2', 'reports', type_='foreignkey')
    op.create_foreign_key(None, 'reports', 'firmware', ['firmware_id'], ['firmware_id'])
    op.create_foreign_key(None, 'reports', 'users', ['user_id'], ['user_id'])
    op.drop_index('idx_17572_component_id', table_name='requirements')
    op.drop_constraint('requirements_ibfk_1', 'requirements', type_='foreignkey')
    op.create_foreign_key(None, 'requirements', 'components', ['component_id'], ['component_id'])
    op.drop_index('idx_17581_vendor_id', table_name='restrictions')
    op.drop_constraint('restrictions_ibfk_1', 'restrictions', type_='foreignkey')
    op.create_foreign_key(None, 'restrictions', 'vendors', ['vendor_id'], ['vendor_id'])
    op.drop_index('idx_17617_test_id', table_name='test_attributes')
    op.drop_constraint('test_attributes_ibfk_1', 'test_attributes', type_='foreignkey')
    op.create_foreign_key(None, 'test_attributes', 'tests', ['test_id'], ['test_id'])
    op.drop_index('idx_17608_firmware_id', table_name='tests')
    op.drop_index('idx_17608_waived_user_id', table_name='tests')
    op.drop_constraint('tests_ibfk_1', 'tests', type_='foreignkey')
    op.drop_constraint('tests_ibfk_2', 'tests', type_='foreignkey')
    op.create_foreign_key(None, 'tests', 'firmware', ['firmware_id'], ['firmware_id'])
    op.create_foreign_key(None, 'tests', 'users', ['waived_user_id'], ['user_id'])
    op.drop_index('idx_17644_user_id', table_name='user_actions')
    op.drop_constraint('user_actions_ibfk_1', 'user_actions', type_='foreignkey')
    op.create_foreign_key(None, 'user_actions', 'users', ['user_id'], ['user_id'])
    op.create_index(op.f('ix_useragents_kind'), 'useragents', ['kind'], unique=False)
    op.drop_index('idx_17626_ix_useragents_kind', table_name='useragents')
    op.create_index('idx_users_username_password', 'users', ['username', 'password'], unique=False)
    op.create_index(op.f('ix_users_username'), 'users', ['username'], unique=False)
    op.drop_index('idx_17635_agreement_id', table_name='users')
    op.drop_index('idx_17635_human_user_id', table_name='users')
    op.drop_index('idx_17635_idx_users_username_password', table_name='users')
    op.drop_index('idx_17635_ix_users_username', table_name='users')
    op.drop_index('idx_17635_vendor_id', table_name='users')
    op.drop_constraint('users_ibfk_3', 'users', type_='foreignkey')
    op.drop_constraint('users_ibfk_1', 'users', type_='foreignkey')
    op.drop_constraint('users_ibfk_2', 'users', type_='foreignkey')
    op.create_foreign_key(None, 'users', 'users', ['human_user_id'], ['user_id'])
    op.create_foreign_key(None, 'users', 'agreements', ['agreement_id'], ['agreement_id'])
    op.create_foreign_key(None, 'users', 'vendors', ['vendor_id'], ['vendor_id'])
    op.create_index(op.f('ix_vendors_group_id'), 'vendors', ['group_id'], unique=False)
    op.drop_index('idx_17653_ix_vendors_group_id', table_name='vendors')
    op.drop_index('idx_17653_remote_id', table_name='vendors')
    op.drop_index('idx_17653_vendors_ibfk_2', table_name='vendors')
    op.drop_constraint('vendors_ibfk_1', 'vendors', type_='foreignkey')
    op.drop_constraint('vendors_ibfk_2', 'vendors', type_='foreignkey')
    op.create_foreign_key(None, 'vendors', 'remotes', ['remote_id'], ['remote_id'])
    op.create_foreign_key(None, 'vendors', 'verfmts', ['verfmt_id'], ['verfmt_id'])
    op.drop_index('idx_17674_user_id', table_name='yara_query')
    op.drop_constraint('yara_query_ibfk_1', 'yara_query', type_='foreignkey')
    op.create_foreign_key(None, 'yara_query', 'users', ['user_id'], ['user_id'])
    op.drop_index('idx_17683_component_id', table_name='yara_query_result')
    op.drop_index('idx_17683_component_shard_id', table_name='yara_query_result')
    op.drop_index('idx_17683_yara_query_id', table_name='yara_query_result')
    op.drop_constraint('yara_query_result_ibfk_1', 'yara_query_result', type_='foreignkey')
    op.drop_constraint('yara_query_result_ibfk_3', 'yara_query_result', type_='foreignkey')
    op.drop_constraint('yara_query_result_ibfk_2', 'yara_query_result', type_='foreignkey')
    op.create_foreign_key(None, 'yara_query_result', 'component_shards', ['component_shard_id'], ['component_shard_id'])
    op.create_foreign_key(None, 'yara_query_result', 'components', ['component_id'], ['component_id'])
    op.create_foreign_key(None, 'yara_query_result', 'yara_query', ['yara_query_id'], ['yara_query_id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'yara_query_result', type_='foreignkey')
    op.drop_constraint(None, 'yara_query_result', type_='foreignkey')
    op.drop_constraint(None, 'yara_query_result', type_='foreignkey')
    op.create_foreign_key('yara_query_result_ibfk_2', 'yara_query_result', 'yara_query', ['yara_query_id'], ['yara_query_id'], onupdate='RESTRICT', ondelete='RESTRICT')
    op.create_foreign_key('yara_query_result_ibfk_3', 'yara_query_result', 'components', ['component_id'], ['component_id'], onupdate='RESTRICT', ondelete='RESTRICT')
    op.create_foreign_key('yara_query_result_ibfk_1', 'yara_query_result', 'component_shards', ['component_shard_id'], ['component_shard_id'], onupdate='RESTRICT', ondelete='RESTRICT')
    op.create_index('idx_17683_yara_query_id', 'yara_query_result', ['yara_query_id'], unique=False)
    op.create_index('idx_17683_component_shard_id', 'yara_query_result', ['component_shard_id'], unique=False)
    op.create_index('idx_17683_component_id', 'yara_query_result', ['component_id'], unique=False)
    op.drop_constraint(None, 'yara_query', type_='foreignkey')
    op.create_foreign_key('yara_query_ibfk_1', 'yara_query', 'users', ['user_id'], ['user_id'], onupdate='RESTRICT', ondelete='RESTRICT')
    op.create_index('idx_17674_user_id', 'yara_query', ['user_id'], unique=False)
    op.drop_constraint(None, 'vendors', type_='foreignkey')
    op.drop_constraint(None, 'vendors', type_='foreignkey')
    op.create_foreign_key('vendors_ibfk_2', 'vendors', 'verfmts', ['verfmt_id'], ['verfmt_id'], onupdate='RESTRICT', ondelete='RESTRICT')
    op.create_foreign_key('vendors_ibfk_1', 'vendors', 'remotes', ['remote_id'], ['remote_id'], onupdate='RESTRICT', ondelete='RESTRICT')
    op.create_index('idx_17653_vendors_ibfk_2', 'vendors', ['verfmt_id'], unique=False)
    op.create_index('idx_17653_remote_id', 'vendors', ['remote_id'], unique=False)
    op.create_index('idx_17653_ix_vendors_group_id', 'vendors', ['group_id'], unique=False)
    op.drop_index(op.f('ix_vendors_group_id'), table_name='vendors')
    op.drop_constraint(None, 'users', type_='foreignkey')
    op.drop_constraint(None, 'users', type_='foreignkey')
    op.drop_constraint(None, 'users', type_='foreignkey')
    op.create_foreign_key('users_ibfk_2', 'users', 'agreements', ['agreement_id'], ['agreement_id'], onupdate='RESTRICT', ondelete='RESTRICT')
    op.create_foreign_key('users_ibfk_1', 'users', 'vendors', ['vendor_id'], ['vendor_id'], onupdate='RESTRICT', ondelete='RESTRICT')
    op.create_foreign_key('users_ibfk_3', 'users', 'users', ['human_user_id'], ['user_id'], onupdate='RESTRICT', ondelete='RESTRICT')
    op.create_index('idx_17635_vendor_id', 'users', ['vendor_id'], unique=False)
    op.create_index('idx_17635_ix_users_username', 'users', ['username'], unique=False)
    op.create_index('idx_17635_idx_users_username_password', 'users', ['username', 'password'], unique=False)
    op.create_index('idx_17635_human_user_id', 'users', ['human_user_id'], unique=False)
    op.create_index('idx_17635_agreement_id', 'users', ['agreement_id'], unique=False)
    op.drop_index(op.f('ix_users_username'), table_name='users')
    op.drop_index('idx_users_username_password', table_name='users')
    op.create_index('idx_17626_ix_useragents_kind', 'useragents', ['kind'], unique=False)
    op.drop_index(op.f('ix_useragents_kind'), table_name='useragents')
    op.drop_constraint(None, 'user_actions', type_='foreignkey')
    op.create_foreign_key('user_actions_ibfk_1', 'user_actions', 'users', ['user_id'], ['user_id'], onupdate='RESTRICT', ondelete='RESTRICT')
    op.create_index('idx_17644_user_id', 'user_actions', ['user_id'], unique=False)
    op.drop_constraint(None, 'tests', type_='foreignkey')
    op.drop_constraint(None, 'tests', type_='foreignkey')
    op.create_foreign_key('tests_ibfk_2', 'tests', 'users', ['waived_user_id'], ['user_id'], onupdate='RESTRICT', ondelete='RESTRICT')
    op.create_foreign_key('tests_ibfk_1', 'tests', 'firmware', ['firmware_id'], ['firmware_id'], onupdate='RESTRICT', ondelete='RESTRICT')
    op.create_index('idx_17608_waived_user_id', 'tests', ['waived_user_id'], unique=False)
    op.create_index('idx_17608_firmware_id', 'tests', ['firmware_id'], unique=False)
    op.drop_constraint(None, 'test_attributes', type_='foreignkey')
    op.create_foreign_key('test_attributes_ibfk_1', 'test_attributes', 'tests', ['test_id'], ['test_id'], onupdate='RESTRICT', ondelete='RESTRICT')
    op.create_index('idx_17617_test_id', 'test_attributes', ['test_id'], unique=False)
    op.drop_constraint(None, 'restrictions', type_='foreignkey')
    op.create_foreign_key('restrictions_ibfk_1', 'restrictions', 'vendors', ['vendor_id'], ['vendor_id'], onupdate='RESTRICT', ondelete='RESTRICT')
    op.create_index('idx_17581_vendor_id', 'restrictions', ['vendor_id'], unique=False)
    op.drop_constraint(None, 'requirements', type_='foreignkey')
    op.create_foreign_key('requirements_ibfk_1', 'requirements', 'components', ['component_id'], ['component_id'], onupdate='RESTRICT', ondelete='RESTRICT')
    op.create_index('idx_17572_component_id', 'requirements', ['component_id'], unique=False)
    op.drop_constraint(None, 'reports', type_='foreignkey')
    op.drop_constraint(None, 'reports', type_='foreignkey')
    op.create_foreign_key('reports_ibfk_2', 'reports', 'users', ['user_id'], ['user_id'], onupdate='RESTRICT', ondelete='RESTRICT')
    op.create_foreign_key('reports_ibfk_1', 'reports', 'firmware', ['firmware_id'], ['firmware_id'], onupdate='RESTRICT', ondelete='RESTRICT')
    op.create_index('idx_17554_user_id', 'reports', ['user_id'], unique=False)
    op.create_index('idx_17554_ix_reports_firmware_id', 'reports', ['firmware_id'], unique=False)
    op.drop_index(op.f('ix_reports_firmware_id'), table_name='reports')
    op.drop_constraint(None, 'report_attributes', type_='foreignkey')
    op.create_foreign_key('report_attributes_ibfk_1', 'report_attributes', 'reports', ['report_id'], ['report_id'], onupdate='RESTRICT', ondelete='RESTRICT')
    op.create_index('idx_17563_report_id', 'report_attributes', ['report_id'], unique=False)
    op.drop_constraint(None, 'protocol', type_='foreignkey')
    op.create_foreign_key('protocol_ibfk_1', 'protocol', 'verfmts', ['verfmt_id'], ['verfmt_id'], onupdate='RESTRICT', ondelete='RESTRICT')
    op.create_index('idx_17536_protocol_ibfk_1', 'protocol', ['verfmt_id'], unique=False)
    op.drop_constraint(None, 'namespaces', type_='foreignkey')
    op.drop_constraint(None, 'namespaces', type_='foreignkey')
    op.create_foreign_key('namespace_ibfk_3', 'namespaces', 'users', ['user_id'], ['user_id'], onupdate='RESTRICT', ondelete='RESTRICT')
    op.create_foreign_key('namespaces_ibfk_1', 'namespaces', 'vendors', ['vendor_id'], ['vendor_id'], onupdate='RESTRICT', ondelete='RESTRICT')
    op.create_index('idx_17527_vendor_id', 'namespaces', ['vendor_id'], unique=False)
    op.create_index('idx_17527_namespace_ibfk_3', 'namespaces', ['user_id'], unique=False)
    op.drop_constraint(None, 'keywords', type_='foreignkey')
    op.create_foreign_key('keywords_ibfk_1', 'keywords', 'components', ['component_id'], ['component_id'], onupdate='RESTRICT', ondelete='RESTRICT')
    op.create_index('idx_17518_component_id', 'keywords', ['component_id'], unique=False)
    op.drop_constraint(None, 'issues', type_='foreignkey')
    op.create_foreign_key('issues_ibfk_1', 'issues', 'vendors', ['vendor_id'], ['vendor_id'], onupdate='RESTRICT', ondelete='RESTRICT')
    op.create_index('idx_17509_vendor_id', 'issues', ['vendor_id'], unique=False)
    op.drop_constraint(None, 'guids', type_='foreignkey')
    op.create_foreign_key('guids_ibfk_1', 'guids', 'components', ['component_id'], ['component_id'], onupdate='RESTRICT', ondelete='RESTRICT')
    op.create_index('idx_17500_component_id', 'guids', ['component_id'], unique=False)
    op.drop_constraint(None, 'firmware_limits', type_='foreignkey')
    op.create_foreign_key('firmware_limits_ibfk_1', 'firmware_limits', 'firmware', ['firmware_id'], ['firmware_id'], onupdate='RESTRICT', ondelete='RESTRICT')
    op.create_index('idx_17491_firmware_id', 'firmware_limits', ['firmware_id'], unique=False)
    op.drop_constraint(None, 'firmware_events', type_='foreignkey')
    op.drop_constraint(None, 'firmware_events', type_='foreignkey')
    op.drop_constraint(None, 'firmware_events', type_='foreignkey')
    op.create_foreign_key('firmware_events_ibfk_3', 'firmware_events', 'remotes', ['remote_id'], ['remote_id'], onupdate='RESTRICT', ondelete='RESTRICT')
    op.create_foreign_key('firmware_events_ibfk_1', 'firmware_events', 'firmware', ['firmware_id'], ['firmware_id'], onupdate='RESTRICT', ondelete='RESTRICT')
    op.create_foreign_key('firmware_events_ibfk_2', 'firmware_events', 'users', ['user_id'], ['user_id'], onupdate='RESTRICT', ondelete='RESTRICT')
    op.create_index('idx_17485_user_id', 'firmware_events', ['user_id'], unique=False)
    op.create_index('idx_17485_remote_id', 'firmware_events', ['remote_id'], unique=False)
    op.create_index('idx_17485_firmware_id', 'firmware_events', ['firmware_id'], unique=False)
    op.drop_constraint(None, 'firmware', type_='foreignkey')
    op.drop_constraint(None, 'firmware', type_='foreignkey')
    op.drop_constraint(None, 'firmware', type_='foreignkey')
    op.create_foreign_key('firmware_ibfk_3', 'firmware', 'remotes', ['remote_id'], ['remote_id'], onupdate='RESTRICT', ondelete='RESTRICT')
    op.create_foreign_key('firmware_ibfk_1', 'firmware', 'vendors', ['vendor_id'], ['vendor_id'], onupdate='RESTRICT', ondelete='RESTRICT')
    op.create_foreign_key('firmware_ibfk_2', 'firmware', 'users', ['user_id'], ['user_id'], onupdate='RESTRICT', ondelete='RESTRICT')
    op.create_index('idx_17474_vendor_id', 'firmware', ['vendor_id'], unique=False)
    op.create_index('idx_17474_user_id', 'firmware', ['user_id'], unique=False)
    op.create_index('idx_17474_remote_id', 'firmware', ['remote_id'], unique=False)
    op.create_index('idx_17474_ix_firmware_checksum_upload', 'firmware', ['checksum_upload_sha1'], unique=False)
    op.drop_index(op.f('ix_firmware_checksum_upload_sha1'), table_name='firmware')
    op.alter_column('firmware', 'checksum_upload_sha1',
               existing_type=sa.VARCHAR(length=40),
               nullable=True)
    op.alter_column('firmware', 'checksum_signed_sha256',
               existing_type=sa.VARCHAR(length=64),
               nullable=True)
    op.alter_column('firmware', 'checksum_signed_sha1',
               existing_type=sa.VARCHAR(length=40),
               nullable=True)
    op.drop_constraint(None, 'event_log', type_='foreignkey')
    op.drop_constraint(None, 'event_log', type_='foreignkey')
    op.create_foreign_key('event_log_ibfk_1', 'event_log', 'users', ['user_id'], ['user_id'], onupdate='RESTRICT', ondelete='RESTRICT')
    op.create_foreign_key('event_log_ibfk_2', 'event_log', 'vendors', ['vendor_id'], ['vendor_id'], onupdate='RESTRICT', ondelete='RESTRICT')
    op.create_index('idx_17463_vendor_id', 'event_log', ['vendor_id'], unique=False)
    op.create_index('idx_17463_user_id', 'event_log', ['user_id'], unique=False)
    op.drop_constraint(None, 'conditions', type_='foreignkey')
    op.create_foreign_key('conditions_ibfk_1', 'conditions', 'issues', ['issue_id'], ['issue_id'], onupdate='RESTRICT', ondelete='RESTRICT')
    op.create_index('idx_17454_issue_id', 'conditions', ['issue_id'], unique=False)
    op.drop_constraint(None, 'components', type_='foreignkey')
    op.drop_constraint(None, 'components', type_='foreignkey')
    op.drop_constraint(None, 'components', type_='foreignkey')
    op.drop_constraint(None, 'components', type_='foreignkey')
    op.create_foreign_key('components_ibfk_3', 'components', 'categories', ['category_id'], ['category_id'], onupdate='RESTRICT', ondelete='RESTRICT')
    op.create_foreign_key('components_ibfk_2', 'components', 'protocol', ['protocol_id'], ['protocol_id'], onupdate='RESTRICT', ondelete='RESTRICT')
    op.create_foreign_key('components_ibfk_4', 'components', 'verfmts', ['verfmt_id'], ['verfmt_id'], onupdate='RESTRICT', ondelete='RESTRICT')
    op.create_foreign_key('components_ibfk_1', 'components', 'firmware', ['firmware_id'], ['firmware_id'], onupdate='RESTRICT', ondelete='RESTRICT')
    op.create_index('idx_17379_ix_components_firmware_id', 'components', ['firmware_id'], unique=False)
    op.create_index('idx_17379_components_ibfk_4', 'components', ['verfmt_id'], unique=False)
    op.create_index('idx_17379_components_ibfk_3', 'components', ['category_id'], unique=False)
    op.create_index('idx_17379_components_ibfk_2', 'components', ['protocol_id'], unique=False)
    op.drop_index(op.f('ix_components_firmware_id'), table_name='components')
    op.drop_constraint(None, 'component_shards', type_='foreignkey')
    op.drop_constraint(None, 'component_shards', type_='foreignkey')
    op.create_foreign_key('component_shards_ibfk_1', 'component_shards', 'components', ['component_id'], ['component_id'], onupdate='RESTRICT', ondelete='RESTRICT')
    op.create_foreign_key('component_shards_ibfk_2', 'component_shards', 'component_shard_infos', ['component_shard_info_id'], ['component_shard_info_id'], onupdate='RESTRICT', ondelete='RESTRICT')
    op.create_index('idx_17418_ix_component_shards_guid', 'component_shards', ['guid'], unique=False)
    op.create_index('idx_17418_component_shard_info_id', 'component_shards', ['component_shard_info_id'], unique=False)
    op.create_index('idx_17418_component_id', 'component_shards', ['component_id'], unique=False)
    op.drop_index(op.f('ix_component_shards_guid'), table_name='component_shards')
    op.create_index('idx_17445_ix_component_shard_infos_guid', 'component_shard_infos', ['guid'], unique=False)
    op.drop_index(op.f('ix_component_shard_infos_guid'), table_name='component_shard_infos')
    op.drop_constraint(None, 'component_shard_checksums', type_='foreignkey')
    op.create_foreign_key('component_shard_checksums_ibfk_1', 'component_shard_checksums', 'component_shards', ['component_shard_id'], ['component_shard_id'], onupdate='RESTRICT', ondelete='RESTRICT')
    op.create_index('idx_17436_component_shard_id', 'component_shard_checksums', ['component_shard_id'], unique=False)
    op.drop_constraint(None, 'component_shard_certificates', type_='foreignkey')
    op.create_foreign_key('component_shard_certificates_ibfk_1', 'component_shard_certificates', 'component_shards', ['component_shard_id'], ['component_shard_id'], onupdate='RESTRICT', ondelete='RESTRICT')
    op.create_index('idx_17427_component_shard_id', 'component_shard_certificates', ['component_shard_id'], unique=False)
    op.drop_constraint(None, 'component_refs', type_='foreignkey')
    op.drop_constraint(None, 'component_refs', type_='foreignkey')
    op.drop_constraint(None, 'component_refs', type_='foreignkey')
    op.drop_constraint(None, 'component_refs', type_='foreignkey')
    op.create_foreign_key('component_refs_ibfk_1', 'component_refs', 'components', ['component_id'], ['component_id'], onupdate='RESTRICT', ondelete='RESTRICT')
    op.create_foreign_key('component_refs_ibfk_3', 'component_refs', 'vendors', ['vendor_id'], ['vendor_id'], onupdate='RESTRICT', ondelete='RESTRICT')
    op.create_foreign_key('component_refs_ibfk_4', 'component_refs', 'vendors', ['vendor_id_partner'], ['vendor_id'], onupdate='RESTRICT', ondelete='RESTRICT')
    op.create_foreign_key('component_refs_ibfk_2', 'component_refs', 'protocol', ['protocol_id'], ['protocol_id'], onupdate='RESTRICT', ondelete='RESTRICT')
    op.create_index('idx_17409_vendor_id_partner', 'component_refs', ['vendor_id_partner'], unique=False)
    op.create_index('idx_17409_vendor_id', 'component_refs', ['vendor_id'], unique=False)
    op.create_index('idx_17409_protocol_id', 'component_refs', ['protocol_id'], unique=False)
    op.create_index('idx_17409_component_id', 'component_refs', ['component_id'], unique=False)
    op.drop_constraint(None, 'component_issues', type_='foreignkey')
    op.create_foreign_key('component_issues_ibfk_1', 'component_issues', 'components', ['component_id'], ['component_id'], onupdate='RESTRICT', ondelete='RESTRICT')
    op.create_index('idx_17400_component_id', 'component_issues', ['component_id'], unique=False)
    op.drop_constraint(None, 'component_claims', type_='foreignkey')
    op.create_foreign_key('component_claims_ibfk_1', 'component_claims', 'components', ['component_id'], ['component_id'], onupdate='RESTRICT', ondelete='RESTRICT')
    op.create_index('idx_17391_component_id', 'component_claims', ['component_id'], unique=False)
    op.drop_constraint(None, 'clients', type_='foreignkey')
    op.create_foreign_key('clients_ibfk_1', 'clients', 'firmware', ['firmware_id'], ['firmware_id'], onupdate='RESTRICT', ondelete='RESTRICT')
    op.create_index('idx_17372_ix_clients_timestamp', 'clients', ['timestamp'], unique=False)
    op.create_index('idx_17372_ix_clients_firmware_id', 'clients', ['firmware_id'], unique=False)
    op.create_index('idx_17372_ix_clients_datestr', 'clients', ['datestr'], unique=False)
    op.drop_index(op.f('ix_clients_timestamp'), table_name='clients')
    op.drop_index(op.f('ix_clients_firmware_id'), table_name='clients')
    op.drop_index(op.f('ix_clients_datestr'), table_name='clients')
    op.drop_constraint(None, 'checksums', type_='foreignkey')
    op.create_foreign_key('checksums_ibfk_1', 'checksums', 'components', ['component_id'], ['component_id'], onupdate='RESTRICT', ondelete='RESTRICT')
    op.create_index('idx_17363_component_id', 'checksums', ['component_id'], unique=False)
    op.drop_constraint(None, 'certificates', type_='foreignkey')
    op.create_foreign_key('certificates_ibfk_1', 'certificates', 'users', ['user_id'], ['user_id'], onupdate='RESTRICT', ondelete='RESTRICT')
    op.create_index('idx_17354_user_id', 'certificates', ['user_id'], unique=False)
    op.drop_constraint(None, 'analytics_vendor', type_='foreignkey')
    op.create_foreign_key('analytics_vendor_ibfk_1', 'analytics_vendor', 'vendors', ['vendor_id'], ['vendor_id'], onupdate='RESTRICT', ondelete='RESTRICT')
    op.create_index('idx_17339_ix_analytics_vendor_vendor_id', 'analytics_vendor', ['vendor_id'], unique=False)
    op.create_index('idx_17339_ix_analytics_vendor_datestr', 'analytics_vendor', ['datestr'], unique=False)
    op.drop_index(op.f('ix_analytics_vendor_vendor_id'), table_name='analytics_vendor')
    op.drop_index(op.f('ix_analytics_vendor_datestr'), table_name='analytics_vendor')
    op.drop_constraint(None, 'analytics_firmware', type_='foreignkey')
    op.create_foreign_key('analytics_firmware_ibfk_1', 'analytics_firmware', 'firmware', ['firmware_id'], ['firmware_id'], onupdate='RESTRICT', ondelete='RESTRICT')
    op.create_index('idx_17333_ix_analytics_firmware_firmware_id', 'analytics_firmware', ['firmware_id'], unique=False)
    op.create_index('idx_17333_ix_analytics_firmware_datestr', 'analytics_firmware', ['datestr'], unique=False)
    op.drop_index(op.f('ix_analytics_firmware_firmware_id'), table_name='analytics_firmware')
    op.drop_index(op.f('ix_analytics_firmware_datestr'), table_name='analytics_firmware')
    op.drop_constraint(None, 'affiliations', type_='foreignkey')
    op.drop_constraint(None, 'affiliations', type_='foreignkey')
    op.create_foreign_key('affiliations_ibfk_2', 'affiliations', 'vendors', ['vendor_id_odm'], ['vendor_id'], onupdate='RESTRICT', ondelete='RESTRICT')
    op.create_foreign_key('affiliations_ibfk_1', 'affiliations', 'vendors', ['vendor_id'], ['vendor_id'], onupdate='RESTRICT', ondelete='RESTRICT')
    op.create_index('idx_17301_vendor_id_odm', 'affiliations', ['vendor_id_odm'], unique=False)
    op.create_index('idx_17301_vendor_id', 'affiliations', ['vendor_id'], unique=False)
    op.drop_constraint(None, 'affiliation_actions', type_='foreignkey')
    op.drop_constraint(None, 'affiliation_actions', type_='foreignkey')
    op.create_foreign_key('affiliation_actions_ibfk_1', 'affiliation_actions', 'affiliations', ['affiliation_id'], ['affiliation_id'], onupdate='RESTRICT', ondelete='RESTRICT')
    op.create_foreign_key('affiliation_actions_ibfk_2', 'affiliation_actions', 'users', ['user_id'], ['user_id'], onupdate='RESTRICT', ondelete='RESTRICT')
    op.create_index('idx_17307_user_id', 'affiliation_actions', ['user_id'], unique=False)
    op.create_index('idx_17307_affiliation_id', 'affiliation_actions', ['affiliation_id'], unique=False)
    # ### end Alembic commands ###
