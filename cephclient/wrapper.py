#   Copyright 2013 David Moreau Simard
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#
#   Author: David Moreau Simard <moi@dmsimard.com>
#

import cephclient.client as client
import cephclient.exceptions as exceptions

class CephWrapper(client.CephClient):
    def __init__(self, **params):
        super(CephWrapper, self).__init__(**params)
        self.user_agent = 'python-cephclient-wrapper'

    ###
    # root GET calls
    ###
    def df(self, detail=None, **kwargs):
        if detail is not None:
            return self.get('df?detail={0}'.format(detail), **kwargs)
        else:
            return self.get('df', **kwargs)

    def fsid(self, **kwargs):
        return self.get('fsid', **kwargs)

    def health(self, detail=None, **kwargs):
        if detail is not None:
            return self.get('health?detail={0}'.format(detail), **kwargs)
        else:
            return self.get('health', **kwargs)

    def quorum_status(self, **kwargs):
        return self.get('quorum_status', **kwargs)

    def report(self, tags=None, **kwargs):
        if tags is not None:
            return self.get('report?tags={0}'.format(tags), **kwargs)
        else:
            return self.get('report', **kwargs)

    def status(self, **kwargs):
        return self.get('status', **kwargs)

    ###
    # root PUT calls
    ###
    def compact(self, **kwargs):
        return self.put('compact', **kwargs)

    def heap(self, heapcmd, **kwargs):
        return self.put('heap?heapcmd={0}'.format(heapcmd), **kwargs)

    def injectargs(self, injected_args, **kwargs):
        return self.put('injectargs?injected_args={0}'.format(injected_args),
                        **kwargs)

    def log(self, logtext, **kwargs):
        return self.put('log?logtext={0}'.format(logtext), **kwargs)

    def quorum(self, quorumcmd, **kwargs):
        return self.put('quorum?quorumcmd={0}'.format(quorumcmd), **kwargs)

    def scrub(self, **kwargs):
        return self.put('scrub', **kwargs)

    def tell(self, target, args, **kwargs):
        return self.put('tell?target={0}&args={1}'.format(target,args),
                        **kwargs)

    ###
    # auth GET calls
    ###
    def auth_export(self, entity=None, **kwargs):
        if entity is not None:
            return self.get('auth/export?entity={0}'.format(entity), **kwargs)
        else:
            return self.get('auth/export', **kwargs)

    def auth_get(self, entity, **kwargs):
        return self.get('auth/get?entity={0}'.format(entity), **kwargs)

    def auth_get_key(self, entity, **kwargs):
        return self.get('auth/get-key?entity={0}'.format(entity), **kwargs)

    def auth_list(self, **kwargs):
        return self.get('auth/list', **kwargs)

    def auth_print_key(self, entity, **kwargs):
        return self.get('auth/print-key?entity={0}'.format(entity), **kwargs)

    ###
    # auth PUT calls
    ###
    """
    caps dictionary format:
    caps = {
        'mon': 'allow rwx',
        'osd': 'allow *',
        ...
    }
    """
    def auth_add(self, entity, caps={}, file=None, **kwargs):
        # XXX-TODO: Implement file input
        caps_expanded = list()
        if caps:
            for key in caps:
                permissions = caps[key].replace(' ', '+')
                caps_expanded.append('&caps={0}&caps={1}'.format(key, permissions))

        return self.put('auth/add?entity={0}{1}'.format(entity, ''.join(caps_expanded)), **kwargs)

    def auth_caps(self, entity, caps={}, **kwargs):
        caps_expanded = list()
        if caps:
            for key in caps:
                permissions = caps[key].replace(' ', '+')
                caps_expanded.append('&caps={0}&caps={1}'.format(key, permissions))

        return self.put('auth/caps?entity={0}{1}'.format(entity, ''.join(caps_expanded)), **kwargs)

    def auth_del(self, entity, **kwargs):
        return self.put('auth/del?entity={0}'.format(entity), **kwargs)

    def auth_get_or_create(self, entity, caps={}, file=None, **kwargs):
        # XXX-TODO: Implement file input
        caps_expanded = list()
        if caps:
            for key in caps:
                permissions = caps[key].replace(' ', '+')
                caps_expanded.append('&caps={0}&caps={1}'.format(key, permissions))

        return self.put('auth/get-or-create?entity={0}{1}'.format(entity, ''.join(caps_expanded)), **kwargs)

    def auth_get_or_create_key(self, entity, caps={}, **kwargs):
        # XXX-TODO: Implement file input
        caps_expanded = list()
        if caps:
            for key in caps:
                permissions = caps[key].replace(' ', '+')
                caps_expanded.append('&caps={0}&caps={1}'.format(key, permissions))

        return self.put('auth/get-or-create-key?entity={0}{1}'.format(entity, ''.join(caps_expanded)), **kwargs)

    def auth_import(self, file):
        # XXX-TODO: Implement file input
        raise exceptions.FunctionNotImplemented()

    ###
    # config-key GET calls
    ###
    def config_key_exists(self, key, **kwargs):
        return self.get('config-key/exists?key={0}'.format(key), **kwargs)

    def config_key_get(self, key, **kwargs):
        return self.get('config-key/get?key={0}'.format(key), **kwargs)

    def config_key_list(self, **kwargs):
        return self.get('config-key/list', **kwargs)

    ###
    # mds GET calls
    ###
    def mds_compat_show(self, **kwargs):
        return self.get('mds/compat/show', **kwargs)

    def mds_dump(self, epoch=None, **kwargs):
        if epoch is not None:
            return self.get('mds/dump?epoch={0}'.format(epoch), **kwargs)
        else:
            return self.get('mds/dump', **kwargs)

    def mds_getmap(self, epoch=None, **kwargs):
        kwargs['supported_body_types'] = ['binary']

        if epoch is not None:
            return self.get('mds/getmap?epoch={0}'.format(epoch), **kwargs)
        else:
            return self.get('mds/getmap', **kwargs)

    def mds_stat(self, **kwargs):
        return self.get('mds/stat', **kwargs)

    ###
    # mds PUT calls
    ###
    def mds_add_data_pool(self, pool, **kwargs):
        return self.put('mds/add_data_pool?pool={0}'.format(pool), **kwargs)

    def mds_cluster_down(self, **kwargs):
        return self.put('mds/cluster_down', **kwargs)

    def mds_cluster_up(self, **kwargs):
        return self.put('mds/cluster_up', **kwargs)

    def mds_compat_rm_compat(self, feature, **kwargs):
        return self.put('mds/compat/rm_compat?feature={0}'.format(feature), **kwargs)

    def mds_compat_rm_incompat(self, feature, **kwargs):
        return self.put('mds/compat/rm_incompat?feature={0}'.format(feature), **kwargs)

    def mds_deactivate(self, who, **kwargs):
        return self.put('mds/deactivate?who={0}'.format(who), **kwargs)

    def mds_fail(self, who, **kwargs):
        return self.put('mds/fail?who={0}'.format(who), **kwargs)

    def mds_newfs(self, metadata, data, sure, **kwargs):
        return self.put('mds/newfs?metadata={0}&data={1}&sure={2}'.format(metadata, data, sure), **kwargs)

    def mds_remove_data_pool(self, pool, **kwargs):
        return self.put('mds/remove_data_pool?pool={0}'.format(pool), **kwargs)

    def mds_rm(self, gid, who, **kwargs):
        return self.put('mds/rm?gid={0}&who={1}'.format(gid, who), **kwargs)

    def mds_rmfailed(self, who, **kwargs):
        return self.put('mds/rmfailed?who={0}'.format(who), **kwargs)

    def mds_set_allow_new_snaps(self, sure, **kwargs):
        """
        mds/set?key=allow_new_snaps&sure=
        """
        raise exceptions.FunctionNotImplemented()

    def mds_set_max_mds(self, maxmds, **kwargs):
        return self.put('mds/set_max_mds?maxmds={0}'.format(maxmds), **kwargs)

    def mds_setmap(self, epoch, **kwargs):
        return self.put('mds/setmap?epoch={0}'.format(epoch), **kwargs)

    def mds_stop(self, who, **kwargs):
        return self.put('mds/stop?who={0}'.format(who), **kwargs)

    def mds_tell(self, who, args, **kwargs):
        return self.put('mds/tell?who={0}&args={1}'.format(who, args), **kwargs)

    def mds_unset_allow_new_snaps(self, sure, **kwargs):
        """
        mds/unset?key=allow_new_snaps&sure=
        """
        raise exceptions.FunctionNotImplemented()

    ###
    # mon GET calls
    ###
    def mon_dump(self, epoch=None, **kwargs):
        if epoch is not None:
            return self.get('mon/dump?epoch={0}'.format(epoch), **kwargs)
        else:
            return self.get('mon/dump', **kwargs)

    def mon_getmap(self, epoch=None, **kwargs):
        kwargs['supported_body_types'] = ['binary']

        if epoch is not None:
            return self.get('mon/getmap?epoch={0}'.format(epoch), **kwargs)
        else:
            return self.get('mon/getmap', **kwargs)

    def mon_stat(self, **kwargs):
        kwargs['supported_body_types'] = ['text', 'xml']

        return self.get('mon/stat', **kwargs)

    def mon_status(self, **kwargs):
        return self.get('mon_status', **kwargs)

    ###
    # mon PUT calls
    ###
    def mon_add(self, name, addr, **kwargs):
        return self.put('mon/add?name={0}&addr={1}'.format(name, addr), **kwargs)

    def mon_remove(self, name, **kwargs):
        return self.put('mon/remove?name={0}'.format(name), **kwargs)

    ###
    # osd GET calls
    ###
    def osd_blacklist_ls(self, **kwargs):
        return self.get('osd/blacklist/ls', **kwargs)

    def osd_crush_dump(self, **kwargs):
        return self.get('osd/crush/dump', **kwargs)

    def osd_crush_rule_dump(self, **kwargs):
        return self.get('osd/crush/rule/dump', **kwargs)

    def osd_crush_rule_list(self, **kwargs):
        return self.get('osd/crush/rule/list', **kwargs)

    def osd_crush_rule_ls(self, **kwargs):
        return self.get('osd/crush/rule/ls', **kwargs)

    def osd_dump(self, epoch=None, **kwargs):
        if epoch is not None:
            return self.get('osd/dump?epoch={0}'.format(epoch), **kwargs)
        else:
            return self.get('osd/dump', **kwargs)

    def osd_find(self, id, **kwargs):
        return self.get('osd/find?id={0}'.format(id), **kwargs)

    def osd_getcrushmap(self, epoch=None, **kwargs):
        kwargs['supported_body_types'] = ['binary']

        if epoch is not None:
            return self.get('osd/getcrushmap?epoch={0}'.format(epoch), **kwargs)
        else:
            return self.get('osd/getcrushmap', **kwargs)

    def osd_getmap(self, epoch=None, **kwargs):
        kwargs['supported_body_types'] = ['binary']

        if epoch is not None:
            return self.get('osd/getmap?epoch={0}'.format(epoch), **kwargs)
        else:
            return self.get('osd/getmap', **kwargs)

    def osd_getmaxosd(self, **kwargs):
        return self.get('osd/getmaxosd', **kwargs)

    def osd_ls(self, epoch=None, **kwargs):
        if epoch is not None:
            return self.get('osd/ls?epoch={0}'.format(epoch), **kwargs)
        else:
            return self.get('osd/ls', **kwargs)

    def osd_lspools(self, auid=None, **kwargs):
        if auid is not None:
            return self.get('osd/lspools?auid={0}'.format(auid), **kwargs)
        else:
            return self.get('osd/lspools', **kwargs)

    def osd_map(self, pool, object, **kwargs):
        return self.get('osd/map?pool={0}&object={1}'.format(
            pool, object), **kwargs)

    def osd_perf(self, **kwargs):
        return self.get('osd/perf', **kwargs)

    def osd_pool_get(self, pool, var, **kwargs):
        return self.get('osd/pool/get?pool={0}&var={1}'.format(
            pool, var), **kwargs)

    def osd_pool_stats(self, name=None, **kwargs):
        if name is not None:
            return self.get('osd/pool/stats?name={0}'.format(name), **kwargs)
        else:
            return self.get('osd/pool/stats', **kwargs)

    def osd_stat(self, **kwargs):
        return self.get('osd/stat', **kwargs)

    def osd_tree(self, epoch=None, **kwargs):
        if epoch is not None:
            return self.get('osd/tree?epoch={0}'.format(epoch), **kwargs)
        else:
            return self.get('osd/tree', **kwargs)

    ###
    # pg GET calls
    ###
    def pg_debug(self, debugop, **kwargs):
        kwargs['supported_body_types'] = ['text', 'xml']

        return self.get('pg/debug?debugop={0}'.format(debugop), **kwargs)

    def pg_dump(self, dumpcontents=None, **kwargs):
        if dumpcontents is not None:
            return self.get('pg/dump?dumpcontents={0}'.format(
                dumpcontents), **kwargs)
        else:
            return self.get('pg/dump', **kwargs)

    def pg_dump_json(self, dumpcontents=None, **kwargs):
        if dumpcontents is not None:
            return self.get('pg/dump_json?dumpcontents={0}'.format(
                dumpcontents), **kwargs)
        else:
            return self.get('pg/dump_json', **kwargs)

    def pg_dump_pools_json(self, **kwargs):
        return self.get('pg/dump_pools_json', **kwargs)

    def pg_dump_stuck(self, stuckops=None, **kwargs):
        if stuckops is not None:
            return self.get('pg/dump_stuck?stuckops={0}'.format(
                stuckops), **kwargs)
        else:
            return self.get('pg/dump_stuck', **kwargs)

    def pg_getmap(self, **kwargs):
        kwargs['supported_body_types'] = ['binary']

        return self.get('pg/getmap', **kwargs)

    def pg_map(self, pgid, **kwargs):
        return self.get('pg/map?pgid={0}'.format(pgid), **kwargs)

    def pg_stat(self, **kwargs):
        return self.get('pg/stat', **kwargs)

    ###
    # tell GET calls
    ###
    def tell_debug_dump_missing(self, id, filename, **kwargs):
        return self.get('/tell/{0}/debug_dump_missing?filename={1}'.format(
            id, filename), **kwargs)

    def tell_dump_pg_recovery_stats(self, id, **kwargs):
        return self.get('/tell/{0}/dump_pg_recovery_stats'.format(id), **kwargs)

    def tell_list_missing(self, id, offset, **kwargs):
        return self.get('/tell/{0}/list_missing?offset={1}'.format(
            id, offset), **kwargs)

    def tell_query(self, id, **kwargs):
        return self.get('/tell/{0}/query'.format(id), **kwargs)

    def tell_version(self, id, **kwargs):
        return self.get('/tell/{0}/version'.format(id), **kwargs)
