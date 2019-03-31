#!/usr/bin/env python3
"""
napalm function definitions

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

from napalm import get_network_driver

# Supress SSL Certificate Warnings
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


def get_connection(my_device):
    my_device = my_device.copy()
    device_type = my_device.pop("platform")
    driver = get_network_driver(device_type)
    device = driver(**my_device)
    # open connection first
    device.open()
    return device

def get_backup(device, suffix):
    filename = device.hostname + suffix
    output = device.get_config()["running"]
    with open(filename, "w") as f:
        f.write(output)

def get_checkpoint(device, suffix):
    filename = device.hostname + suffix
    output = device._get_checkpoint_file()
    with open(filename, "w") as f:
        f.write(output)
    return None

