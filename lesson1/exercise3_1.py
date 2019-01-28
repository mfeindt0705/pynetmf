#!/usr/bin/env python
"""
For one of the Cisco IOS devices, use Netmiko and the send_command() method to retrieve 'show version'. 
Save this output to a file in the current working directory.
"""

from netmiko import ConnectHandler
from getpass import getpass

ios3 = {"host": "cisco3.lasthop.io",
         "username": "pyclass",
         "password": getpass(prompt='Bitte Password eingeben: '),
         "device_type": "cisco_ios",
	 "session_log": "my_session.txt"}

ios_connect = ConnectHandler(**ios3)
output = ios_connect.send_command("show version")
with open("my_version.txt", 'w') as f:
    f.write(output)

ios_connect.disconnect()

