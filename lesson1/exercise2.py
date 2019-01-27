#!/usr/bin/env python
"""
Add a second NX-OS device to your first exercise. Make sure you are using dictionaries to represent the two NX-OS devices. 
Additionally, use a for-loop to accomplish the Netmiko connection creation. 
Once again print the prompt back from the devices that you connected to.
"""

from netmiko import ConnectHandler
from getpass import getpass

password = getpass(prompt='Bitte Password eingeben: ')

nxos1 = {"host": "nxos1.lasthop.io",
         "username": "pyclass",
         "password": password,
         "device_type": "cisco_nxos"}

nxos2 = {"host": "nxos2.lasthop.io",
         "username": "pyclass",
         "password": password,
         "device_type": "cisco_nxos"}

nxoslist = (nxos1, nxos2)

for host in nxoslist:
    nxos_connect = ConnectHandler(**host)
    print(str(nxos_connect.find_prompt()))



