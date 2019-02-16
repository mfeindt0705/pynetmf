#!/usr/bin/env python3
"""
cisco3:
  device_type: cisco_xe
  host: cisco3.lasthop.io

cisco4:
  device_type: cisco_xe
  host: cisco4.lasthop.io

nxos1:
  device_type: cisco_nxos
  host: nxos1.lasthop.io
  port: 22

nxos2:
  device_type: cisco_nxos
  host: nxos2.lasthop.io
  port: 22


a. Create a list where each of the list elements is a dictionary representing one of the network devices in the lab. 
Do this for at least four of the lab devices. 
The dictionary should have keys corresponding to the device_name, host (i.e. FQDN), username, and password. 
Use a fictional username/password to avoid checking the lab password into GitHub.

b. Write the data structure you created in part 2a out to a YAML file. 
Use expanded YAML format. How could you re-use this YAML file later when creating Netmiko connections to devices?
"""

import yaml
from pprint import pprint

cisco1 = {"device_name": "nxos1", "host": "nxos1.lasthop.io"}

cisco2 = {"device_name": "nxos2", "host": "nxos2.lasthop.io"}

cisco3 = {"devicename": "cisco3", "host": "cisco3.lasthop.io"}

cisco4 = {"devicename": "cisco4", "host": "cisco4.lasthop.io"}

dev_list = [cisco1, cisco2, cisco3, cisco4]

for dev in dev_list:
    dev['username'] = "newuser"
    dev['password'] = "newpass"

filename = "ciscodev.yaml"

with open(filename, 'w') as f:
    yaml.dump(dev_list, f, default_flow_style=False)







