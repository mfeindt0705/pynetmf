#!/usr/bin/env python 3
"""
In your lab environment, there is a file located at ~/.netmiko.yml. This file contains all of the devices used in the lab. 
Create a Python program that processes this YAML file and then uses Netmiko to connect to the Cisco3 router. 
Print out the router prompt from this device.

Note, the device dictionaries in the .netmiko.yml file use key-value pairs designed to work directly with Netmiko. 
The .netmiko.yml also contains group definitions for: cisco, arista, juniper, and nxos groups. 
These group definitions are lists of devices. Once again, don't check the .netmiko.yml into GitHub.

"""

import yaml
import os
from netmiko import ConnectHandler

#filename = "/home/mfeindt/.netmiko.yml"
filename = os.path.join(os.path.expanduser("~"), ".netmiko.yml")

with open(filename, 'r') as f:
    inv_data = yaml.load(f)

cisco_ios3 = inv_data['cisco3']
cisco_ios3["session_log"] = "my_session.txt"

ios_connect = ConnectHandler(**cisco_ios3)

delimit = "-------------"

print(delimit)
print(ios_connect.find_prompt())
print(delimit)

ios_connect.disconnect()







