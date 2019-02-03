#!/usr/bin/env python3
"""
On your AWS lab server, look at the ntc-templates index file (at ~/ntc-templates/templates/index). 
Look at some of the commands available for cisco_ios 
(you can use 'cat ~/ntc-templates/templates/index | grep cisco_ios' to see this). 
Also look at some of the abbreviated forms of Cisco IOS commands that are supported in the index file.

cisco_ios_show_version.template, .*, cisco_ios, sh[[ow]] ver[[sion]]
cisco_ios_show_lldp_neighbors.template, .*, cisco_ios, sh[[ow]] lld[[p]] neig[[hbors]]


Create a script using Netmiko that executes 'show version' and 'show lldp neighbors' 
against the Cisco4 device with use_textfsm=True.

What is the outermost data structure that is returned from 'show lldp neighbors' (dictionary, list, string, something else)? 
The Cisco4 device should only have one LLDP entry (the HPE switch that this router connects to). 
From this LLDP data, print out the remote device's interface. 
In other words, print out the port number on the HPE switch that Cisco4 connects into.

"""

from netmiko import ConnectHandler
from getpass import getpass
from pprint import pprint

cisco_ios4 = {"host": "cisco4.lasthop.io",
              "username": "pyclass",
              "password": getpass(prompt="Bitte Passwort eingeben : "),
              "device_type": "cisco_ios",
              "session_log": "my_session.txt"}

ios_connect = ConnectHandler(**cisco_ios4)
print(ios_connect.find_prompt())

delimit = "-----------------"

print(delimit)
output = ios_connect.send_command("show version", use_textfsm=True)
pprint(output)

print(delimit)
output = ios_connect.send_command("show lldp neighbors", use_textfsm=True)
pprint(output)
print(delimit)
print(type(output))
print(output[0]['neighbor_interface'])


ios_connect.disconnect()


