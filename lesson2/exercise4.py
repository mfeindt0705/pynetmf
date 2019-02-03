#!/usr/bin/env python3
"""
Use Netmiko and the send_config_set() method to configure the following on the Cisco3 router.

ip name-server 1.1.1.1
ip name-server 1.0.0.1
ip domain-lookup

Experiment with fast_cli=True to see how long the script takes to execute (with and without this option enabled).

Verify DNS lookups on the router are now working by executing 'ping google.com'.
Verify from this that you receive a ping response back.


"""

from netmiko import ConnectHandler
from getpass import getpass
from datetime import datetime

cisco_ios3 = {"host": "cisco3.lasthop.io",
              "username": "pyclass",
              "password": getpass(prompt="Bitte Passwort eingeben : "),
              "device_type": "cisco_ios",
              "session_log": "my_session.txt"}

ios_connect = ConnectHandler(**cisco_ios3)
print(ios_connect.find_prompt())

commandset = ["ip name-server 1.1.1.1", "ip name-server 1.0.0.1", "ip domain-lookup"]

output = ios_connect.send_config_set(commandset)

print(ios_connect.find_prompt())

output = ios_connect.send_command("ping www.google.com")

if "!!" in output:
    print("Ping to google.com successfully executed on cisco3")
else:
    print("Ping to google.com failed on cisco3")

ios_connect.disconnect()

