#!/usr/bin/env python3
"""
module for yaml functions
"""

import yaml
from pprint import pprint

def load_yaml(file_yaml):
    with open(file_yaml, 'r') as f:
        handle_yaml = yaml.safe_load(f)
        return handle_yaml


def print_output(output):
    print("*" * 24)
    print("Map of learned MAC addresses")
    print("*" * 24)
    maclist = output[0]['result']['ipV4Neighbors']
    for macaddress in maclist:
        ipv4 = macaddress['address']
        mac = macaddress['hwAddress']
        print("IP Address {0:15} \t Mac Address {1:s}".format(ipv4, mac))
    print("*" * 24)


def print_routes(output, vrf="default"):
    print("*" * 24)
    print("Map of learned Routing Entries")
    print("*" * 24)
    vrf_table = output[0]['result']['vrfs'][vrf]['routes']
    for route, values in vrf_table.items():
        if values['directlyConnected']:
            print("{0:15} \t directly connected".format(route))
        else:
            next_hop = values['vias'][0]
            print("{0:15} \t next hop : {1:s}".format(route, next_hop['nexthopAddr']))

