#!/usr/bin/env python3
"""
exercise 6 nx-api with json

Create an nxapi_plumbing "Device" object for nxos1. 
The api_format should be "jsonrpc" and the transport should be "https" (port 8443). 
Use getpass() to capture the device's password. 
Send the "show interface Ethernet2/1" command to the device, parse the output
print out the following information:
Interface: Ethernet2/1; State: up; MTU: 1500

"""

import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from getpass import getpass
from nxapi_plumbing import Device
from pprint import pprint

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

device = Device(
    api_format="jsonrpc",
    host="nxos1.lasthop.io",
    username="pyclass",
    password=getpass("Bitte Passwort eingeben : "),
    transport="https",
    port=8443,
    verify=False,
)

if __name__ == "__main__":
    output = device.show("show interface Ethernet2/1")
    pprint(output)
    vinterface = output['TABLE_interface']['ROW_interface']
    print("-" * 20)
    print("Interface Report")
    print(f"Interface: {vinterface['interface']}; State: {vinterface['admin_state']}; MTU: {vinterface['eth_mtu']}")
