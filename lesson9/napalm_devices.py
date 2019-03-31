#!/usr/bin/env python3
"""
napalm device definitions

Parameters:
hostname – (str) IP or FQDN of the device you want to connect to.
username – (str) Username you want to use
password – (str) Password
platform - (str) device platform
timeout – (int) Time in seconds to wait for the device to respond.
optional_args – (dict) Pass additional arguments to underlying driver

cisco3
nxos1
arista1

"""

from getpass import getpass

password = getpass("Bitte Passwort eingeben : ")
username = "pyclass"
cisco3 = {
    "hostname": "cisco3.lasthop.io",
    "username": username,
    "password": password,
    "platform": "ios",
}

arista1 = {
    "hostname": "arista1.lasthop.io",
    "username": username,
    "password": password,
    "platform": "eos",
}

nxos1 = {
    "hostname": "nxos1.lasthop.io",
    "username": username,
    "password": password,
    "platform": "nxos",
    "optional_args": {"port": 8443},
}


# device definitions as a list
l_devices = [nxos1, cisco3, arista1]

# device definitions as a dict
d_devices = {"cisco": cisco3,
             "nxos": nxos1,
             "arista": arista1,
             }

# List of devices (only cisco3 and arista1)
network_devices = [cisco3, arista1]

# list of device platforms
l_platforms = ["cisco", "arista"]

