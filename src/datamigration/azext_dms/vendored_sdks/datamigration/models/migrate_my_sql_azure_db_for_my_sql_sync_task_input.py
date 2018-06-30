# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class MigrateMySqlAzureDbForMySqlSyncTaskInput(Model):
    """Input for the task that migrates MySQL databases to Azure Database for
    MySQL with continuous sync.

    :param selected_databases: Databases to migrate
    :type selected_databases:
     list[~azure.mgmt.datamigration.models.MigrateMySqlAzureDbForMySqlSyncDatabaseInput]
    :param target_connection_info: Connection information for target Azure
     Database for MySQL
    :type target_connection_info:
     ~azure.mgmt.datamigration.models.MySqlConnectionInfo
    :param source_connection_info: Connection information for source MySQL
    :type source_connection_info:
     ~azure.mgmt.datamigration.models.MySqlConnectionInfo
    """

    _validation = {
        'selected_databases': {'required': True},
        'target_connection_info': {'required': True},
        'source_connection_info': {'required': True},
    }

    _attribute_map = {
        'selected_databases': {'key': 'selectedDatabases', 'type': '[MigrateMySqlAzureDbForMySqlSyncDatabaseInput]'},
        'target_connection_info': {'key': 'targetConnectionInfo', 'type': 'MySqlConnectionInfo'},
        'source_connection_info': {'key': 'sourceConnectionInfo', 'type': 'MySqlConnectionInfo'},
    }

    def __init__(self, selected_databases, target_connection_info, source_connection_info):
        super(MigrateMySqlAzureDbForMySqlSyncTaskInput, self).__init__()
        self.selected_databases = selected_databases
        self.target_connection_info = target_connection_info
        self.source_connection_info = source_connection_info