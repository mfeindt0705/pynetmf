#!/usr/bin/env python3
"""
exercise 4 PyEZ
"""

import warnings
warnings.filterwarnings(action='ignore', module='.*paramiko.*')

from getpass import getpass
from pprint import pprint
from jnpr.junos import Device
from jnpr.junos.utils.config import Config
from jnpr_devices import junos_devices
from jnpr_functions import gather_routes, check_connected

f_routes = "static_routes.conf"

def set_config_file(device, file, merge=True):
    cfg = Config(device)
    try:
        cfg.lock()
        print("Config lock set")
    except LockError:
        print("No config lock set possible")
    cfg.load(path=file, format="text", merge=merge)
    delta = cfg.diff()
    if delta:
        cfg.commit()
    cfg.unlock()
    return delta



def compare_routes():
    return None


if __name__ == "__main__":
    srx_device = junos_devices[0]
    a_device = Device(**srx_device)
    a_device.open()
    a_device.timeout = 60

    # task a
    if check_connected(a_device):
        print("Connect to device was successful")
    else:
        print("Connect to device was not successful")
    route_entries_1 = gather_routes(a_device)

    # task b
    print(set_config_file(a_device, f_routes, True))
    route_entries_2 = gather_routes(a_device)

