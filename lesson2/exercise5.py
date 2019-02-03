#!/usr/bin/env python3
"""
 On both the NXOS1 and NXOS2 switches configure five VLANs including VLAN names 
 (just pick 5 VLAN numbers between 100 - 999). 
 Use Netmiko's send_config_from_file() method to accomplish this. 
 Also use Netmiko's save_config() method to save the changes to the startup-config.
"""

from netmiko import ConnectHandler
from getpass import getpass

password = getpass(prompt="Bitte Passwort eingeben : ")
cisco_nxos1 = {"host": "nxos1.lasthop.io",
               "username": "pyclass",
               "password": password,
               "device_type": "cisco_nxos",
               "session_log": "my_session1.txt"}

cisco_nxos2 = {"host": "nxos2.lasthop.io",
               "username": "pyclass",
               "password": password,
               "device_type": "cisco_nxos",
               "session_log": "my_session2.txt"}


device_list = [cisco_nxos1, cisco_nxos2]

for device in device_list:
    nxos_connect = ConnectHandler(**device)
    print(nxos_connect.find_prompt())
    output = nxos_connect.send_config_from_file("vlan.txt")
    output += nxos_connect.save_config()
    #print(output)
    nxos_connect.disconnect()



