#!/usr/bin/env python3
"""
simple exercise using the pyeapi Arista module
"""

import pyeapi
from getpass import getpass

connection = pyeapi.client.connect(
    transport="https",
    host="arista8.lasthop.io",
    username="pyclass",
    password=getpass(),
    port="443",
)

enable = getpass("Enable: ")
device = pyeapi.client.Node(connection, enablepwd=enable)

vlan_cfg = device.api("vlans")
print(vlan_cfg)

