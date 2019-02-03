#!/usr/bin/env python3
"""
 Create a Netmiko connection to the 'nxos2' device using a global_delay_factor of 2. 
 Execute 'show lldp neighbors detail' and print the returned output to standard output. 
 Execute 'show lldp neighbors detail' a second time using send_command() with a delay_factor of 8. 
 Print the output of this command to standard output. 
 Use the Python datetime library to record the execution time of both of these commands. 
 Print these execution times to standard output.
 nxos2:
  device_type: cisco_nxos
  host: nxos2.lasthop.io
  username: pyclass
  password: 88newclass
  port: 22

"""

from netmiko import ConnectHandler
from getpass import getpass
from datetime import datetime

cisco_nxos2 = {"host": "nxos2.lasthop.io",
               "username": "pyclass",
               "password": getpass(prompt="Bitte Passwort eingeben :"),
               "device_type": "cisco_nxos",
               "session_log": "my_session.txt"}

nxos_connect = ConnectHandler(**cisco_nxos2)
print(nxos_connect.find_prompt())

starttime = datetime.now()
command = "show lldp neighbors detail"
output = nxos_connect.send_command(command)
totaltime1 = datetime.now() - starttime
print(output)

starttime = datetime.now()
output = nxos_connect.send_command(command, delay_factor=8)
totaltime2 = datetime.now() - starttime
print(output)

delimit = "------------------"

print(delimit)
print("elapsed time with global delay 2 :" + str(totaltime1))

print(delimit)
print("elapsed time with local delay 8 :" + str(totaltime2))

nxos_connect.disconnect()

