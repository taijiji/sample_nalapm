#! /usr/bin/env python
# -*- coding: utf-8 -*-

import napalm
from pprint import pprint

# For JUNOS firefly1
#driver = napalm.get_network_driver('junos')
#device = driver(
#    hostname='192.168.34.16',
#    username='user1',
#    password='password1')

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

print 'get facts: '
pprint(device.get_facts())

print 'get interface IP: '
pprint(device.get_interfaces_ip())

print 'get ARP table'
pprint(device.get_arp_table())

#for JUNOS firefly1
#print 'get route to 192.168.35.0'
#pprint(device.get_route_to(destination=u'192.168.35.0'))

#for Cisco IOSXRv, but Include error (pyIOSXR bug?)
#print 'get route to 10.0.2.2'
#pprint(device.get_route_to(destination=u'10.0.2.2'))
#pprint(device.get_route_to(destination=u'10.0.2.2', protocol=u'bgp'))

print 'get BGP config'
pprint(device.get_bgp_config())

print 'get BGP neighbors'
pprint(device.get_bgp_neighbors())

print 'Close session: ',
device.close()
print 'OK'
