#!/usr/bin/env python3
"""
exercise 1 napalm
"""

from napalm import get_network_driver
from pprint import pprint

from napalm_devices import d_devices

# Supress SSL Certificate Warnings
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

def get_connection(my_device):
    device_type = my_device.pop("platform")
    driver = get_network_driver(device_type)
    device = driver(**my_device)
    device.open()
    return device


if __name__ == "__main__":
    my_device = d_devices["cisco"]
    # device_type = my_device.pop("platform")
    # device_type = my_device["platform"]
    # driver = get_network_driver(device_type)
    # device = driver(**my_device)
    print("")
    print("Open device connection")
    device = get_connection(my_device)
    print("")
    output = device.get_facts()
    pprint(output)
    device.close()

