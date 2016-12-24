#! /usr/bin/env python
# -*- coding: utf-8 -*-

import napalm

'''
# For JUNOS firefly1
driver = napalm.get_network_driver('junos')
device = driver(
    hostname='192.168.34.16',
    username='user1',
    password='password1')
    #optional_args={'config_lock': False} )
'''

# For Cisco IOSXRv
driver = napalm.get_network_driver('iosxr')
device = driver(
    hostname='127.0.0.1',
    username='vagrant',
    password='vagrant',
    # IOSXRv default ssh port
    optional_args={'port': 2223}) 

print 'Open session: ',
device.open()
print 'OK'

print 'get hostname : ', 
print device.get_facts()[u'hostname']

print 'Config load (merge mode): ',

# For JUNOS firefly1
#device.load_merge_candidate(filename='./change_hostname_JUNOS.conf')
# For Cisco IOSXRv
device.load_merge_candidate(filename='./change_hostname_IOSXR.conf')
print 'OK'

print 'Compare config: '
print device.compare_config()

print 'Do you commit? y/n'
choice = raw_input().lower()
if choice == 'y':
    print 'Commit config:',
    device.commit_config()
    print 'OK'
else:
    print 'Discard config:',
    device.discard_config()
    print 'OK'

print 'get hostname : ', 
print device.get_facts()[u'hostname']

print 'Close session: ',
device.close()
print 'OK'