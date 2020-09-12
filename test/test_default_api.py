# coding: utf-8

"""
    KubeVirt API

    This is KubeVirt API an add-on for Kubernetes.

    OpenAPI spec version: 1.0.0
    Contact: kubevirt-dev@googlegroups.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kubevirt
from kubevirt.rest import ApiException
from kubevirt.apis.default_api import DefaultApi


class TestDefaultApi(unittest.TestCase):
    """ DefaultApi unit test stubs """

    def setUp(self):
        self.api = kubevirt.apis.default_api.DefaultApi()

    def tearDown(self):
        pass

    def test_check_health(self):
        """
        Test case for check_health

        
        """
        pass

    def test_console(self):
        """
        Test case for console

        
        """
        pass

    def test_create_namespaced_kube_virt(self):
        """
        Test case for create_namespaced_kube_virt

        
        """
        pass

    def test_create_namespaced_virtual_machine(self):
        """
        Test case for create_namespaced_virtual_machine

        
        """
        pass

    def test_create_namespaced_virtual_machine_instance(self):
        """
        Test case for create_namespaced_virtual_machine_instance

        
        """
        pass

    def test_create_namespaced_virtual_machine_instance_migration(self):
        """
        Test case for create_namespaced_virtual_machine_instance_migration

        
        """
        pass

    def test_create_namespaced_virtual_machine_instance_preset(self):
        """
        Test case for create_namespaced_virtual_machine_instance_preset

        
        """
        pass

    def test_create_namespaced_virtual_machine_instance_replica_set(self):
        """
        Test case for create_namespaced_virtual_machine_instance_replica_set

        
        """
        pass

    def test_create_namespaced_virtual_machine_restore(self):
        """
        Test case for create_namespaced_virtual_machine_restore

        
        """
        pass

    def test_create_namespaced_virtual_machine_snapshot(self):
        """
        Test case for create_namespaced_virtual_machine_snapshot

        
        """
        pass

    def test_create_namespaced_virtual_machine_snapshot_content(self):
        """
        Test case for create_namespaced_virtual_machine_snapshot_content

        
        """
        pass

    def test_delete_collection_namespaced_kube_virt(self):
        """
        Test case for delete_collection_namespaced_kube_virt

        
        """
        pass

    def test_delete_collection_namespaced_virtual_machine(self):
        """
        Test case for delete_collection_namespaced_virtual_machine

        
        """
        pass

    def test_delete_collection_namespaced_virtual_machine_instance(self):
        """
        Test case for delete_collection_namespaced_virtual_machine_instance

        
        """
        pass

    def test_delete_collection_namespaced_virtual_machine_instance_migration(self):
        """
        Test case for delete_collection_namespaced_virtual_machine_instance_migration

        
        """
        pass

    def test_delete_collection_namespaced_virtual_machine_instance_preset(self):
        """
        Test case for delete_collection_namespaced_virtual_machine_instance_preset

        
        """
        pass

    def test_delete_collection_namespaced_virtual_machine_instance_replica_set(self):
        """
        Test case for delete_collection_namespaced_virtual_machine_instance_replica_set

        
        """
        pass

    def test_delete_collection_namespaced_virtual_machine_restore(self):
        """
        Test case for delete_collection_namespaced_virtual_machine_restore

        
        """
        pass

    def test_delete_collection_namespaced_virtual_machine_snapshot(self):
        """
        Test case for delete_collection_namespaced_virtual_machine_snapshot

        
        """
        pass

    def test_delete_collection_namespaced_virtual_machine_snapshot_content(self):
        """
        Test case for delete_collection_namespaced_virtual_machine_snapshot_content

        
        """
        pass

    def test_delete_namespaced_kube_virt(self):
        """
        Test case for delete_namespaced_kube_virt

        
        """
        pass

    def test_delete_namespaced_virtual_machine(self):
        """
        Test case for delete_namespaced_virtual_machine

        
        """
        pass

    def test_delete_namespaced_virtual_machine_instance(self):
        """
        Test case for delete_namespaced_virtual_machine_instance

        
        """
        pass

    def test_delete_namespaced_virtual_machine_instance_migration(self):
        """
        Test case for delete_namespaced_virtual_machine_instance_migration

        
        """
        pass

    def test_delete_namespaced_virtual_machine_instance_preset(self):
        """
        Test case for delete_namespaced_virtual_machine_instance_preset

        
        """
        pass

    def test_delete_namespaced_virtual_machine_instance_replica_set(self):
        """
        Test case for delete_namespaced_virtual_machine_instance_replica_set

        
        """
        pass

    def test_delete_namespaced_virtual_machine_restore(self):
        """
        Test case for delete_namespaced_virtual_machine_restore

        
        """
        pass

    def test_delete_namespaced_virtual_machine_snapshot(self):
        """
        Test case for delete_namespaced_virtual_machine_snapshot

        
        """
        pass

    def test_delete_namespaced_virtual_machine_snapshot_content(self):
        """
        Test case for delete_namespaced_virtual_machine_snapshot_content

        
        """
        pass

    def test_filesystemlist(self):
        """
        Test case for filesystemlist

        
        """
        pass

    def test_func1(self):
        """
        Test case for func1

        
        """
        pass

    def test_func7(self):
        """
        Test case for func7

        
        """
        pass

    def test_get_api_group_kubevirt_io(self):
        """
        Test case for get_api_group_kubevirt_io

        
        """
        pass

    def test_get_api_group_list(self):
        """
        Test case for get_api_group_list

        
        """
        pass

    def test_get_api_group_snapshot_kubevirt_io(self):
        """
        Test case for get_api_group_snapshot_kubevirt_io

        
        """
        pass

    def test_get_api_resources_kubevirt_io_v1alpha3(self):
        """
        Test case for get_api_resources_kubevirt_io_v1alpha3

        
        """
        pass

    def test_get_api_resources_snapshot_kubevirt_io_v1alpha1(self):
        """
        Test case for get_api_resources_snapshot_kubevirt_io_v1alpha1

        
        """
        pass

    def test_get_api_sub_resources(self):
        """
        Test case for get_api_sub_resources

        
        """
        pass

    def test_get_root_paths(self):
        """
        Test case for get_root_paths

        
        """
        pass

    def test_get_sub_api_group(self):
        """
        Test case for get_sub_api_group

        
        """
        pass

    def test_guestosinfo(self):
        """
        Test case for guestosinfo

        
        """
        pass

    def test_list_kube_virt_for_all_namespaces(self):
        """
        Test case for list_kube_virt_for_all_namespaces

        
        """
        pass

    def test_list_namespaced_kube_virt(self):
        """
        Test case for list_namespaced_kube_virt

        
        """
        pass

    def test_list_namespaced_virtual_machine(self):
        """
        Test case for list_namespaced_virtual_machine

        
        """
        pass

    def test_list_namespaced_virtual_machine_instance(self):
        """
        Test case for list_namespaced_virtual_machine_instance

        
        """
        pass

    def test_list_namespaced_virtual_machine_instance_migration(self):
        """
        Test case for list_namespaced_virtual_machine_instance_migration

        
        """
        pass

    def test_list_namespaced_virtual_machine_instance_preset(self):
        """
        Test case for list_namespaced_virtual_machine_instance_preset

        
        """
        pass

    def test_list_namespaced_virtual_machine_instance_replica_set(self):
        """
        Test case for list_namespaced_virtual_machine_instance_replica_set

        
        """
        pass

    def test_list_namespaced_virtual_machine_restore(self):
        """
        Test case for list_namespaced_virtual_machine_restore

        
        """
        pass

    def test_list_namespaced_virtual_machine_snapshot(self):
        """
        Test case for list_namespaced_virtual_machine_snapshot

        
        """
        pass

    def test_list_namespaced_virtual_machine_snapshot_content(self):
        """
        Test case for list_namespaced_virtual_machine_snapshot_content

        
        """
        pass

    def test_list_virtual_machine_for_all_namespaces(self):
        """
        Test case for list_virtual_machine_for_all_namespaces

        
        """
        pass

    def test_list_virtual_machine_instance_for_all_namespaces(self):
        """
        Test case for list_virtual_machine_instance_for_all_namespaces

        
        """
        pass

    def test_list_virtual_machine_instance_migration_for_all_namespaces(self):
        """
        Test case for list_virtual_machine_instance_migration_for_all_namespaces

        
        """
        pass

    def test_list_virtual_machine_instance_preset_for_all_namespaces(self):
        """
        Test case for list_virtual_machine_instance_preset_for_all_namespaces

        
        """
        pass

    def test_list_virtual_machine_instance_replica_set_for_all_namespaces(self):
        """
        Test case for list_virtual_machine_instance_replica_set_for_all_namespaces

        
        """
        pass

    def test_list_virtual_machine_restore_for_all_namespaces(self):
        """
        Test case for list_virtual_machine_restore_for_all_namespaces

        
        """
        pass

    def test_list_virtual_machine_snapshot_content_for_all_namespaces(self):
        """
        Test case for list_virtual_machine_snapshot_content_for_all_namespaces

        
        """
        pass

    def test_list_virtual_machine_snapshot_for_all_namespaces(self):
        """
        Test case for list_virtual_machine_snapshot_for_all_namespaces

        
        """
        pass

    def test_migrate(self):
        """
        Test case for migrate

        
        """
        pass

    def test_patch_namespaced_kube_virt(self):
        """
        Test case for patch_namespaced_kube_virt

        
        """
        pass

    def test_patch_namespaced_virtual_machine(self):
        """
        Test case for patch_namespaced_virtual_machine

        
        """
        pass

    def test_patch_namespaced_virtual_machine_instance(self):
        """
        Test case for patch_namespaced_virtual_machine_instance

        
        """
        pass

    def test_patch_namespaced_virtual_machine_instance_migration(self):
        """
        Test case for patch_namespaced_virtual_machine_instance_migration

        
        """
        pass

    def test_patch_namespaced_virtual_machine_instance_preset(self):
        """
        Test case for patch_namespaced_virtual_machine_instance_preset

        
        """
        pass

    def test_patch_namespaced_virtual_machine_instance_replica_set(self):
        """
        Test case for patch_namespaced_virtual_machine_instance_replica_set

        
        """
        pass

    def test_patch_namespaced_virtual_machine_restore(self):
        """
        Test case for patch_namespaced_virtual_machine_restore

        
        """
        pass

    def test_patch_namespaced_virtual_machine_snapshot(self):
        """
        Test case for patch_namespaced_virtual_machine_snapshot

        
        """
        pass

    def test_patch_namespaced_virtual_machine_snapshot_content(self):
        """
        Test case for patch_namespaced_virtual_machine_snapshot_content

        
        """
        pass

    def test_pause(self):
        """
        Test case for pause

        
        """
        pass

    def test_read_namespaced_kube_virt(self):
        """
        Test case for read_namespaced_kube_virt

        
        """
        pass

    def test_read_namespaced_virtual_machine(self):
        """
        Test case for read_namespaced_virtual_machine

        
        """
        pass

    def test_read_namespaced_virtual_machine_instance(self):
        """
        Test case for read_namespaced_virtual_machine_instance

        
        """
        pass

    def test_read_namespaced_virtual_machine_instance_migration(self):
        """
        Test case for read_namespaced_virtual_machine_instance_migration

        
        """
        pass

    def test_read_namespaced_virtual_machine_instance_preset(self):
        """
        Test case for read_namespaced_virtual_machine_instance_preset

        
        """
        pass

    def test_read_namespaced_virtual_machine_instance_replica_set(self):
        """
        Test case for read_namespaced_virtual_machine_instance_replica_set

        
        """
        pass

    def test_read_namespaced_virtual_machine_restore(self):
        """
        Test case for read_namespaced_virtual_machine_restore

        
        """
        pass

    def test_read_namespaced_virtual_machine_snapshot(self):
        """
        Test case for read_namespaced_virtual_machine_snapshot

        
        """
        pass

    def test_read_namespaced_virtual_machine_snapshot_content(self):
        """
        Test case for read_namespaced_virtual_machine_snapshot_content

        
        """
        pass

    def test_rename(self):
        """
        Test case for rename

        
        """
        pass

    def test_replace_namespaced_kube_virt(self):
        """
        Test case for replace_namespaced_kube_virt

        
        """
        pass

    def test_replace_namespaced_virtual_machine(self):
        """
        Test case for replace_namespaced_virtual_machine

        
        """
        pass

    def test_replace_namespaced_virtual_machine_instance(self):
        """
        Test case for replace_namespaced_virtual_machine_instance

        
        """
        pass

    def test_replace_namespaced_virtual_machine_instance_migration(self):
        """
        Test case for replace_namespaced_virtual_machine_instance_migration

        
        """
        pass

    def test_replace_namespaced_virtual_machine_instance_preset(self):
        """
        Test case for replace_namespaced_virtual_machine_instance_preset

        
        """
        pass

    def test_replace_namespaced_virtual_machine_instance_replica_set(self):
        """
        Test case for replace_namespaced_virtual_machine_instance_replica_set

        
        """
        pass

    def test_replace_namespaced_virtual_machine_restore(self):
        """
        Test case for replace_namespaced_virtual_machine_restore

        
        """
        pass

    def test_replace_namespaced_virtual_machine_snapshot(self):
        """
        Test case for replace_namespaced_virtual_machine_snapshot

        
        """
        pass

    def test_replace_namespaced_virtual_machine_snapshot_content(self):
        """
        Test case for replace_namespaced_virtual_machine_snapshot_content

        
        """
        pass

    def test_restart(self):
        """
        Test case for restart

        
        """
        pass

    def test_start(self):
        """
        Test case for start

        
        """
        pass

    def test_stop(self):
        """
        Test case for stop

        
        """
        pass

    def test_test(self):
        """
        Test case for test

        
        """
        pass

    def test_unpause(self):
        """
        Test case for unpause

        
        """
        pass

    def test_userlist(self):
        """
        Test case for userlist

        
        """
        pass

    def test_version(self):
        """
        Test case for version

        
        """
        pass

    def test_vnc(self):
        """
        Test case for vnc

        
        """
        pass

    def test_watch_kube_virt_list_for_all_namespaces(self):
        """
        Test case for watch_kube_virt_list_for_all_namespaces

        
        """
        pass

    def test_watch_namespaced_kube_virt(self):
        """
        Test case for watch_namespaced_kube_virt

        
        """
        pass

    def test_watch_namespaced_virtual_machine(self):
        """
        Test case for watch_namespaced_virtual_machine

        
        """
        pass

    def test_watch_namespaced_virtual_machine_instance(self):
        """
        Test case for watch_namespaced_virtual_machine_instance

        
        """
        pass

    def test_watch_namespaced_virtual_machine_instance_migration(self):
        """
        Test case for watch_namespaced_virtual_machine_instance_migration

        
        """
        pass

    def test_watch_namespaced_virtual_machine_instance_preset(self):
        """
        Test case for watch_namespaced_virtual_machine_instance_preset

        
        """
        pass

    def test_watch_namespaced_virtual_machine_instance_replica_set(self):
        """
        Test case for watch_namespaced_virtual_machine_instance_replica_set

        
        """
        pass

    def test_watch_namespaced_virtual_machine_restore(self):
        """
        Test case for watch_namespaced_virtual_machine_restore

        
        """
        pass

    def test_watch_namespaced_virtual_machine_snapshot(self):
        """
        Test case for watch_namespaced_virtual_machine_snapshot

        
        """
        pass

    def test_watch_namespaced_virtual_machine_snapshot_content(self):
        """
        Test case for watch_namespaced_virtual_machine_snapshot_content

        
        """
        pass

    def test_watch_virtual_machine_instance_list_for_all_namespaces(self):
        """
        Test case for watch_virtual_machine_instance_list_for_all_namespaces

        
        """
        pass

    def test_watch_virtual_machine_instance_migration_list_for_all_namespaces(self):
        """
        Test case for watch_virtual_machine_instance_migration_list_for_all_namespaces

        
        """
        pass

    def test_watch_virtual_machine_instance_preset_list_for_all_namespaces(self):
        """
        Test case for watch_virtual_machine_instance_preset_list_for_all_namespaces

        
        """
        pass

    def test_watch_virtual_machine_instance_replica_set_list_for_all_namespaces(self):
        """
        Test case for watch_virtual_machine_instance_replica_set_list_for_all_namespaces

        
        """
        pass

    def test_watch_virtual_machine_list_for_all_namespaces(self):
        """
        Test case for watch_virtual_machine_list_for_all_namespaces

        
        """
        pass

    def test_watch_virtual_machine_restore_list_for_all_namespaces(self):
        """
        Test case for watch_virtual_machine_restore_list_for_all_namespaces

        
        """
        pass

    def test_watch_virtual_machine_snapshot_content_list_for_all_namespaces(self):
        """
        Test case for watch_virtual_machine_snapshot_content_list_for_all_namespaces

        
        """
        pass

    def test_watch_virtual_machine_snapshot_list_for_all_namespaces(self):
        """
        Test case for watch_virtual_machine_snapshot_list_for_all_namespaces

        
        """
        pass


if __name__ == '__main__':
    unittest.main()
