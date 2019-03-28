#!/usr/bin/env python3
"""
exercise 3 PyEZ
"""

import warnings
warnings.filterwarnings(action='ignore', module='.*paramiko.*')

from getpass import getpass
from pprint import pprint
from jnpr.junos import Device
from jnpr.junos.utils.config import Config
from jnpr_devices import junos_devices



if __name__ == "__main__":
    srx_device = junos_devices[0]
    a_device = Device(**srx_device)
    a_device.open()
    a_device.timeout = 60
    cfg = Config(a_device)
    cfg.lock()
    cfg.load("set system host-name test123", format="set", merge=True)
    print(cfg.diff())
    cfg.rollback(0)
    cfg.unlock()

