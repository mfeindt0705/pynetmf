#!/usr/bin/env python 3
"""
 Use Netmiko to retrieve 'show run' from the Cisco4 device. Feed this configuration into CiscoConfParse.

Use CiscoConfParse to find all of the interfaces on Cisco4 that have an IP address. 
Again use netmiko.yml to gather device data
Print out the interface name and IP address for each interface. 
Your solution should work if there is more than one IP address configured on Cisco4. 
For example, if you configure a loopback interface on Cisco4 with an IP address,then your solution should continue to work. 
The output from this program should look similar to the following: 
$ python confparse_ex6.py 
 
Interface Line: interface GigabitEthernet0/0/0
IP Address Line:  ip address 10.220.88.23 255.255.255.0

"""

from netmiko import ConnectHandler
import os
import re
import yaml
from ciscoconfparse import CiscoConfParse

filename = os.path.join(os.path.expanduser("~"), ".netmiko.yml")

with open(filename, 'r') as f:
    inv_data = yaml.load(f)

ios_device = inv_data['cisco4']
ios_device['session_log'] = "my_session.txt"
ios_connect = ConnectHandler(**ios_device)
ios_command = "show running-config"
ios_config = ios_connect.send_command(ios_command)
ios_connect.disconnect()
ios_config = ios_config.splitlines()
ios_parse = CiscoConfParse(ios_config)
ios_ip_intf = ios_parse.find_objects_w_child(parentspec=r"interface", childspec="^\s+ip address")
print()
for intf in ios_ip_intf:
    print("*" * 12)
    print("List of IP addresses  :")
    print("Interface Line : \t {}".format(intf.parent.text))
    for cmd in intf.re_search_children(r"\sip address"):
        print("IP Address Line : \t {}".format(cmd.text.strip()))
    print("*" * 12)


