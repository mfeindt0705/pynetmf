#!/usr/bin/env python3
"""
exercise 1 PyEZ
"""

from getpass import getpass
from pprint import pprint
from jnpr.junos import Device
from jnpr.junos.utils.config import Config
import warnings
warnings.filterwarnings(action='ignore', module='.*paramiko.*')

from jnpr_devices import junos_devices

juniper_srx = junos_devices[0]
a_device = Device(**juniper_srx)
a_device.open()

print("")
print("Print device facts : ")
pprint(a_device.facts)
print("-" * 20)
print("")
print(f"SRX Hostname : {a_device.facts['hostname']}")

