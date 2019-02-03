#!/usr/bin/env python3
"""
 Use the extended 'ping' command and Netmiko on the 'cisco4' router. 
 This should prompt you for additional information as follows:

b. Use send_command() and the expect_string argument to handle the additional prompting. 
Once again specify a target IP address of '8.8.8.8'.

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

output = ios_connect.send_command(
    "ping", expect_string=r"Protocol", strip_prompt=False, strip_command=False
)
output += ios_connect.send_command(
    "ip", expect_string=r"Target IP", strip_prompt=False, strip_command=False
)
output += ios_connect.send_command(
    "8.8.8.8", expect_string=r"Repeat count", strip_prompt=False, strip_command=False
)
output += ios_connect.send_command(
    "\n", expect_string=r"Datagram size", strip_prompt=False, strip_command=False
)
output += ios_connect.send_command(
    "\n", expect_string=r"Timeout in seconds", strip_prompt=False, strip_command=False
)
output += ios_connect.send_command(
    "\n", expect_string=r"Extended commands", strip_prompt=False, strip_command=False
)
output += ios_connect.send_command(
    "n", expect_string=r"Sweep range", strip_prompt=False, strip_command=False
)
output += ios_connect.send_command(
    "n", expect_string=r"#", strip_prompt=False, strip_command=False
)

ios_connect.disconnect()

delimit = "-------------"

print(delimit)
print(output)
print(delimit)

