#!/usr/bin/env python3
"""
exercise 2a for Arista eAPI
"""

from getpass import getpass
import pyeapi
from pprint import pprint

import yaml

arista_file = "arista.yml"

with open(arista_file, 'r') as f:
    arista_dict = yaml.safe_load(f)

for name, values in arista_dict.items():
    values['password'] = getpass(prompt="Password :")
    #pprint(values)
    #break
    connection = pyeapi.client.connect(**values)
    device = pyeapi.client.Node(connection)
    output = device.enable(["show ip arp"])
    #pprint(output)
    print("*" * 24)
    print("Map of learned MAC addresses")
    print("*" * 24)
    maclist = output[0]['result']['ipV4Neighbors']
    for macaddress in maclist:
        ipv4 = macaddress['address']
        mac = macaddress['hwAddress']
        print("IP Address {0:15} \t Mac Address {1:s}".format(ipv4, mac))
    print("*" * 24)

