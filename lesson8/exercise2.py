#!/usr/binenv python 3
"""
exercise 2 PyEZ

This program should have four separate functions:
1. check_connected() - Verify that your NETCONF connection is working. 
2. gather_routes() - Return the routing table from the device.
3. gather_arp_table() - Return the ARP table from the device.
4. print_output() - A function that takes the Juniper PyEZ Device object, etc

"""

import warnings
warnings.filterwarnings(action='ignore', module='.*paramiko.*')

from getpass import getpass
from pprint import pprint
from jnpr.junos import Device
from jnpr.junos.utils.config import Config
from jnpr.junos.op.arp import ArpTable
from jnpr.junos.op.routes import RouteTable
from jnpr_devices import junos_devices


def check_connected(a_device):
    return a_device.connected


def gather_routes(a_device):
    route_entries = RouteTable(a_device)
    route_entries.get()
    return route_entries


def gather_arp_tables(a_device):
    arp_entries = ArpTable(a_device)
    arp_entries.get()
    return arp_entries

def print_output(a_device, arp_table, route_table):
    # print device host facts
    vdict = a_device.facts
    print(f"Model {vdict['model']} with hostname {vdict['hostname']}")
    print(f"Connected via port {a_device.port} with user {a_device.user}")

    # print arp cache entries
    print("")
    print("Device Arp cache entries : ")
    for mac in arp_table:
        print(f"MAC address {mac['mac_address']} for IP address {mac['ip_address']}")

    # print routing table entries
    print("")
    print("Device route table entries : ")
    for k in route_table.keys():
        vdict = dict(route_table[k].items())
        if vdict['nexthop']:
            next_hop_ip = vdict['nexthop']
        else:
            next_hop_ip = "LOCAL"
        print(f"Network {k} with next hop IP {next_hop_ip}")
    return None


if __name__ == "__main__":
    srx_device = junos_devices[0]
    a_device = Device(**srx_device)
    a_device.open()

    # Task a
    if check_connected(a_device):
        print("Verify Connection was successful")
    else:
        print("Verify Connection was unsuccessful")

    # Task b
    arps = gather_arp_tables(a_device)
    routes = gather_routes(a_device)
    if check_connected(a_device):
        print_output(a_device, arps, routes)

