#!/usr/bin/env python3
"""
exercise 5 PyEZ

srx2.lasthop.io

# show version | display xml rpc
# <get-software-information>

"""

import warnings
warnings.filterwarnings(action='ignore', module='.*paramiko.*')

from getpass import getpass
from pprint import pprint
from lxml import etree
from jnpr.junos import Device
from jnpr.junos.utils.config import Config
from jnpr_devices import junos_devices

if __name__ == "__main__":
    srx_device = junos_devices[0]
    a_device = Device(**srx_device)
    a_device.open()
    a_device.timeout = 60
    # task a
    print("Print device information ")
    xml_out = a_device.rpc.get_software_information()
    print(etree.tostring(xml_out, encoding="unicode"))
    # task b
    print("Print Interface information")
    # xml_out = a_device.rpc.get_interface_information()
    # print(etree.tostring(xml_out, encoding="unicode"))
    # task c
    print("Print Interface information fe-0/0/7")
    xml_out = a_device.rpc.get_interface_information(interface_name="fe-0/0/7", terse=True, normalize=True)
    print(etree.tostring(xml_out, pretty_print=True, encoding="unicode"))
