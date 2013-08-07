# vim: tabstop=4 shiftwidth=4 softtabstop=4
#
# Copyright 2013 OpenStack Foundation
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.
#

"""Add agent management extension model support

Revision ID: 511471cc46b
Revises: 363468ac592c
Create Date: 2013-02-18 05:09:32.523460

"""

# revision identifiers, used by Alembic.
revision = '511471cc46b'
down_revision = '363468ac592c'

# Change to ['*'] if this migration applies to all plugins

migration_for_plugins = [
    'neutron.plugins.openvswitch.ovs_neutron_plugin.OVSNeutronPluginV2',
    'neutron.plugins.linuxbridge.lb_neutron_plugin.LinuxBridgePluginV2',
    'neutron.plugins.nicira.NeutronPlugin.NvpPluginV2',
    'neutron.plugins.nec.nec_plugin.NECPluginV2',
    'neutron.plugins.brocade.NeutronPlugin.BrocadePluginV2',
    'neutron.services.loadbalancer.plugin.LoadBalancerPlugin',
]

from alembic import op
import sqlalchemy as sa


from neutron.db import migration


def upgrade(active_plugins=None, options=None):
    if not migration.should_run(active_plugins, migration_for_plugins):
        return

    ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        'agents',
        sa.Column('id', sa.String(length=36), nullable=False),
        sa.Column('agent_type', sa.String(length=255), nullable=False),
        sa.Column('binary', sa.String(length=255), nullable=False),
        sa.Column('topic', sa.String(length=255), nullable=False),
        sa.Column('host', sa.String(length=255), nullable=False),
        sa.Column('admin_state_up', sa.Boolean(), nullable=False),
        sa.Column('created_at', sa.DateTime(), nullable=False),
        sa.Column('started_at', sa.DateTime(), nullable=False),
        sa.Column('heartbeat_timestamp', sa.DateTime(), nullable=False),
        sa.Column('description', sa.String(length=255), nullable=True),
        sa.Column('configurations', sa.String(length=4095), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade(active_plugins=None, options=None):
    if not migration.should_run(active_plugins, migration_for_plugins):
        return

    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('agents')
    ### end Alembic commands ###
