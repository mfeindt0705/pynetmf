#!/usr/bin/env python3

"""
use extended ping to ping on router cisco4
target ip is 8.8.8.8

use the send_command_timing method

cisco4:
  device_type: cisco_xe
  host: cisco4.lasthop.io
  username: pyclass
  password: 88newclass

"""

from netmiko import ConnectHandler
from getpass import getpass

cisco_ios4 = {"host": "cisco4.lasthop.io",
              "username": "pyclass",
              "password": getpass(prompt='Bitte Password eingeben: '),
              "device_type": "cisco_ios",
              "session_log": "my_session.txt"}

ios_connect = ConnectHandler(**cisco_ios4)
print(ios_connect.find_prompt())


output = ios_connect.send_command_timing(
    "ping", strip_prompt=False, strip_command=False
)
output += ios_connect.send_command_timing(
    "ip", strip_prompt=False, strip_command=False
)
output += ios_connect.send_command_timing(
    "8.8.8.8", strip_prompt=False, strip_command=False
)
output += ios_connect.send_command_timing(
    "\n", strip_prompt=False, strip_command=False
)
output += ios_connect.send_command_timing(
    "\n", strip_prompt=False, strip_command=False
)
output += ios_connect.send_command_timing(
    "\n", strip_prompt=False, strip_command=False
)
output += ios_connect.send_command_timing(
    "n", strip_prompt=False, strip_command=False
)
output += ios_connect.send_command_timing(
    "n", strip_prompt=False, strip_command=False
)

ios_connect.disconnect()

delimit = "-------------"

print(delimit)
print(output)
print(delimit)

