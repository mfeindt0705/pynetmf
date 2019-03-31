#!/usr/bin/env python
from getpass import getpass
from pprint import pprint
from napalm import get_network_driver

# Supress SSL Certificate Warnings
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


cisco3 = dict(
    hostname="cisco3.lasthop.io",
    device_type="ios",
    username="pyclass",
    password=getpass(),
    optional_args={},
)

nxos1 = dict(
    hostname="nxos1.lasthop.io",
    device_type="nxos",
    username="pyclass",
    password=getpass(),
    optional_args={"port": 8443},
)

# device_type = cisco3.pop("device_type")
device_type = nxos1.pop("device_type")

driver = get_network_driver(device_type)
# device = driver(**cisco3)
device = driver(**nxos1)

print()
print("\n\n>>>Test device open")
device.open()

print()
output = device.get_facts()
pprint(output)
print()

