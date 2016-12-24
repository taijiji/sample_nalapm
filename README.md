# NAPALM Sample code
Sample use case and code for automating multi-vendor Routers.
This tools are supported for Juniper firefly and cisco IOSXRv.

NAPALM : 
- https://github.com/napalm-automation/napalm

IOSXRv on Vagnrant: 
- https://xrdocs.github.io/application-hosting/tutorials/iosxr-vagrant-quickstart

Firefly on Vagrant:
- https://github.com/JNPRAutomate/vagrant-junos

# get_info.py

```python
% python get_info.py                                                                                                                                                                         (git)-[master]
Open session:  OK
get facts:
{u'fqdn': u'firefly1',
 u'hostname': u'firefly1',
 u'interface_list': ['ge-0/0/0',
                     'gr-0/0/0',
                     'ip-0/0/0',
                     'lsq-0/0/0',
                     'lt-0/0/0',
                     'mt-0/0/0',
                     'sp-0/0/0',
                     'ge-0/0/1',
                     'ge-0/0/2',
                     '.local.',
                     'dsc',
                     'gre',
                     'ipip',
                     'irb',
                     'lo0',
                     'lsi',
                     'mtun',
                     'pimd',
                     'pime',
                     'pp0',
                     'ppd0',
                     'ppe0',
                     'st0',
                     'tap',
                     'vlan'],
 u'model': u'FIREFLY-PERIMETER',
 u'os_version': u'12.1X47-D20.7',
 u'serial_number': u'f0016079634f',
 u'uptime': 4080,
 u'vendor': u'Juniper'}
get interface IP:
{u'ge-0/0/0.0': {u'ipv4': {u'10.0.2.15': {u'prefix_length': 24}}},
 u'ge-0/0/1.0': {u'ipv4': {u'192.168.34.16': {u'prefix_length': 24}}},
 u'ge-0/0/2.0': {u'ipv4': {u'192.168.35.1': {u'prefix_length': 30}}},
 u'lo0.16384': {u'ipv4': {u'127.0.0.1': {u'prefix_length': 0}}},
 u'lo0.16385': {u'ipv4': {u'10.0.0.1': {u'prefix_length': 0},
                          u'10.0.0.16': {u'prefix_length': 0},
                          u'128.0.0.1': {u'prefix_length': 0},
                          u'128.0.0.4': {u'prefix_length': 0},
                          u'128.0.1.16': {u'prefix_length': 0}}},
 u'sp-0/0/0.16383': {u'ipv4': {u'10.0.0.1': {u'prefix_length': 0},
                               u'10.0.0.6': {u'prefix_length': 0},
                               u'128.0.0.1': {u'prefix_length': 0},
                               u'128.0.0.6': {u'prefix_length': 0}}}}
get ARP table
[{'age': 558.0,
  'interface': u'ge-0/0/0.0',
  'ip': u'10.0.2.2',
  'mac': u'52:54:00:12:35:02'},
 {'age': 478.0,
  'interface': u'ge-0/0/0.0',
  'ip': u'10.0.2.3',
  'mac': u'52:54:00:12:35:03'},
 {'age': 1278.0,
  'interface': u'ge-0/0/1.0',
  'ip': u'192.168.34.1',
  'mac': u'0A:00:27:00:00:04'}]
get route to 192.168.35.0
{u'192.168.35.0/30': [{'age': 4058,
                       'current_active': True,
                       'inactive_reason': u'',
                       'last_active': True,
                       'next_hop': None,
                       'outgoing_interface': u'ge-0/0/2.0',
                       'preference': 0,
                       'protocol': u'Direct',
                       u'protocol_attributes': {},
                       'routing_table': u'inet.0',
                       'selected_next_hop': True}]}
get BGP config
{'ge-0/0/2': {u'apply_groups': [],
              u'description': u'',
              u'export_policy': u'advertised_for_firefly2',
              u'import_policy': u'',
              u'local_address': u'',
              u'local_as': 0,
              u'multihop_ttl': 0,
              u'multipath': False,
              u'neighbors': {u'192.168.35.2': {u'authentication_key': u'',
                                               u'description': u'',
                                               u'export_policy': u'',
                                               u'import_policy': u'',
                                               u'local_address': u'',
                                               u'local_as': 0,
                                               u'nhs': False,
                                               u'prefix_limit': {},
                                               u'remote_as': 65002,
                                               u'route_reflector_client': False}},
              u'prefix_limit': {},
              u'remote_as': 0,
              u'remove_private_as': False,
              u'type': u'external'}}
Close session:  OK
[taiji@aooni] ~/work/github/sample_nalapm
%                                                                                                                                                                                            (git)-[master]
[taiji@aooni] ~/work/github/sample_nalapm
%                                                                                                                                                                                            (git)-[master]
[taiji@aooni] ~/work/github/sample_nalapm
%                                                                                                                                                                                            (git)-[master]
[taiji@aooni] ~/work/github/sample_nalapm
% python get_info.py                                                                                                                                                                         (git)-[master]
Open session:  OK
get facts:
{u'fqdn': u'firefly1',
 u'hostname': u'firefly1',
 u'interface_list': ['ge-0/0/0',
                     'gr-0/0/0',
                     'ip-0/0/0',
                     'lsq-0/0/0',
                     'lt-0/0/0',
                     'mt-0/0/0',
                     'sp-0/0/0',
                     'ge-0/0/1',
                     'ge-0/0/2',
                     '.local.',
                     'dsc',
                     'gre',
                     'ipip',
                     'irb',
                     'lo0',
                     'lsi',
                     'mtun',
                     'pimd',
                     'pime',
                     'pp0',
                     'ppd0',
                     'ppe0',
                     'st0',
                     'tap',
                     'vlan'],
 u'model': u'FIREFLY-PERIMETER',
 u'os_version': u'12.1X47-D20.7',
 u'serial_number': u'f0016079634f',
 u'uptime': 4260,
 u'vendor': u'Juniper'}
get interface IP:
{u'ge-0/0/0.0': {u'ipv4': {u'10.0.2.15': {u'prefix_length': 24}}},
 u'ge-0/0/1.0': {u'ipv4': {u'192.168.34.16': {u'prefix_length': 24}}},
 u'ge-0/0/2.0': {u'ipv4': {u'192.168.35.1': {u'prefix_length': 30}}},
 u'lo0.16384': {u'ipv4': {u'127.0.0.1': {u'prefix_length': 0}}},
 u'lo0.16385': {u'ipv4': {u'10.0.0.1': {u'prefix_length': 0},
                          u'10.0.0.16': {u'prefix_length': 0},
                          u'128.0.0.1': {u'prefix_length': 0},
                          u'128.0.0.4': {u'prefix_length': 0},
                          u'128.0.1.16': {u'prefix_length': 0}}},
 u'sp-0/0/0.16383': {u'ipv4': {u'10.0.0.1': {u'prefix_length': 0},
                               u'10.0.0.6': {u'prefix_length': 0},
                               u'128.0.0.1': {u'prefix_length': 0},
                               u'128.0.0.6': {u'prefix_length': 0}}}}
get interface IP:
{u'ge-0/0/0.0': {u'ipv4': {u'10.0.2.15': {u'prefix_length': 24}}},
 u'ge-0/0/1.0': {u'ipv4': {u'192.168.34.16': {u'prefix_length': 24}}},
 u'ge-0/0/2.0': {u'ipv4': {u'192.168.35.1': {u'prefix_length': 30}}},
 u'lo0.16384': {u'ipv4': {u'127.0.0.1': {u'prefix_length': 0}}},
 u'lo0.16385': {u'ipv4': {u'10.0.0.1': {u'prefix_length': 0},
                          u'10.0.0.16': {u'prefix_length': 0},
                          u'128.0.0.1': {u'prefix_length': 0},
                          u'128.0.0.4': {u'prefix_length': 0},
                          u'128.0.1.16': {u'prefix_length': 0}}},
 u'sp-0/0/0.16383': {u'ipv4': {u'10.0.0.1': {u'prefix_length': 0},
                               u'10.0.0.6': {u'prefix_length': 0},
                               u'128.0.0.1': {u'prefix_length': 0},
                               u'128.0.0.6': {u'prefix_length': 0}}}}
get ARP table
[{'age': 351.0,
  'interface': u'ge-0/0/0.0',
  'ip': u'10.0.2.2',
  'mac': u'52:54:00:12:35:02'},
 {'age': 270.0,
  'interface': u'ge-0/0/0.0',
  'ip': u'10.0.2.3',
  'mac': u'52:54:00:12:35:03'},
 {'age': 1331.0,
  'interface': u'ge-0/0/1.0',
  'ip': u'192.168.34.1',
  'mac': u'0A:00:27:00:00:04'}]
get route to 192.168.35.0
{u'192.168.35.0/30': [{'age': 4265,
                       'current_active': True,
                       'inactive_reason': u'',
                       'last_active': True,
                       'next_hop': None,
                       'outgoing_interface': u'ge-0/0/2.0',
                       'preference': 0,
                       'protocol': u'Direct',
                       u'protocol_attributes': {},
                       'routing_table': u'inet.0',
                       'selected_next_hop': True}]}
get BGP config
{'ge-0/0/2': {u'apply_groups': [],
              u'description': u'',
              u'export_policy': u'advertised_for_firefly2',
              u'import_policy': u'',
              u'local_address': u'',
              u'local_as': 0,
              u'multihop_ttl': 0,
              u'multipath': False,
              u'neighbors': {u'192.168.35.2': {u'authentication_key': u'',
                                               u'description': u'',
                                               u'export_policy': u'',
                                               u'import_policy': u'',
                                               u'local_address': u'',
                                               u'local_as': 0,
                                               u'nhs': False,
                                               u'prefix_limit': {},
                                               u'remote_as': 65002,
                                               u'route_reflector_client': False}},
              u'prefix_limit': {},
              u'remote_as': 0,
              u'remove_private_as': False,
              u'type': u'external'}}
get BGP neighbors
{u'global': {u'peers': {u'192.168.35.2': {u'address_family': {},
                                          'description': u'',
                                          'is_enabled': True,
                                          'is_up': False,
                                          'local_as': 65001,
                                          'remote_as': 65002,
                                          'remote_id': u'',
                                          u'uptime': 291}},
             u'router_id': u'None'}}
Close session:  OK
```

# set_hostname.py

```
% python set_hostname.py                                                                                                                                                                     (git)-[master]
Open session:  OK
get hostname :  ios
Config load (merge mode):  OK
Compare config:
---
+++
@@ -1,5 +1,6 @@
 !! Last configuration change at Fri Dec 23 13:20:24 2016 by vagrant
 !
+hostname iosxrv1_changed_by_NAPALM
 telnet vrf default ipv4 server max-servers 10
 username vagrant
  group root-lr
Do you commit? y/n
y
Commit config: OK
get hostname :  iosxrv1_changed_by_NAPALM
Close session:  OK
```