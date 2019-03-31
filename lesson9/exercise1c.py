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
    my_device = my_device.copy()
    device_type = my_device.pop("platform")
    driver = get_network_driver(device_type)
    device = driver(**my_device)
    # open connection first
    device.open()
    return device


if __name__ == "__main__":
    for my_device in d_devices.values():
        print("")
        print("Open device connection")
        device = get_connection(my_device)
        print("")
        output = device.get_facts()
        pprint(output)
        device.close()




