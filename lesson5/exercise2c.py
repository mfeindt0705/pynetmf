#!/usr/bin/env python3
"""
exercise 2c for jinja rendering

Use Netmiko to push the configurations generated in exercise 2b to the nxos1 device and to the nxos2 device, respectively. 
Verify you are able to ping between the devices and also verify that the BGP session reaches the established state. 
Note, you might need to use an alternate interface besides Ethernet 2/1 (you can use either Ethernet 2/1, 2/2, 2/3, or 2/4). 
Additionally, you might need to use a different IP network (to avoid conflicts with other students). 
Your autonomous system should remain 22, however.

For this exercise you should store your Netmiko connection dictionaries in an external file named my_devices.py 
and should import nxos1, and nxos2 from that external file. 
Make sure that you use getpass() to enter the password in for these devices (as opposed to storing the definitions in the file)

"""

from __future__ import unicode_literals, print_function

from jinja2.environment import Environment
from jinja2 import FileSystemLoader, StrictUndefined
from my_devices import nxos1, nxos2

env = Environment(undefined=StrictUndefined)
env.loader = FileSystemLoader("./templates")

template_file = "exercise2_template_b.j2"

interface = "Ethernet2/2"

nxos_1 = {
    "intf_name": interface,
    "ipv4": "10.1.224.1",
    "mask": "24",
    "local_as": "22",
    "peer_ip": "10.1.100.2",
    "hostname": "NXOS1"
}

nxos_2 = {
    "intf_name": interface,
    "ipv4": "10.1.224.2",
    "mask": "24",
    "local_as": "22",
    "peer_ip": "10.1.100.1",
    "hostname": "NXOS2"
}


