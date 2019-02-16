#!/usr/bin/env python3
"""
You have the following JSON ARP data from an Arista switch:
{
    "dynamicEntries": 2,
    "ipV4Neighbors": [
        {
            "hwAddress": "dc38.e111.97cf",
            "address": "172.17.17.1",
            "interface": "Ethernet45",
            "age": 0
        },
        {
            "hwAddress": "90e2.ba5c.25fd",
            "address": "172.17.16.1",
            "interface": "Ethernet36",
            "age": 0
        }
    ],
    "notLearnedEntries": 0,
    "totalEntries": 2,
    "staticEntries": 0
}

From a file, read this JSON data into your Python program. 
Process this ARP data and return a dictionary where the dictionary keys 
are the IP addresses and the dictionary values are the MAC addresses. 
Print this dictionary to standard output.
"""

import json
from pprint import pprint

filename = "aristaarp.json"

arista_arp = {}

with open(filename, 'r') as f:
    arp_data = json.load(f)

pprint(arp_data)

# grab the IP and mac mappings - type is a list
arp_data = arp_data['ipV4Neighbors']

for arp in arp_data:
    print("IP and MAC Mapping : {} maps {}".format(arp['address'], arp['hwAddress']))
    arista_arp[arp['address']] = arp['hwAddress']

pprint(arista_arp)


