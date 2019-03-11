#!/usr/bin/env python3
"""
exercise for Arista 
"""

import pyeapi
from getpass import getpass
from pprint import pprint

connection = pyeapi.client.connect(transport="https",
    host="arista3.lasthop.io",
    username="pyclass",
    password=getpass(prompt="Password :"),
    port="443")

device = pyeapi.client.Node(connection)
print(type(device))
output = device.enable(["show ip arp"])

print("*" * 24)
print("Map of learned MAC addresses")
print("*" * 24)
maclist = output[0]['result']['ipV4Neighbors']

for macaddress in maclist:
    ipv4 = macaddress['address']
    mac = macaddress['hwAddress']
    print("IP Address {0:s} \t  Mac Address {1:s}".format(ipv4, mac))

print("*" * 24)

