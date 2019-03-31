#!/usr/bin/env python3
"""
exercise 4 napalm
"""

from pprint import pprint

from napalm_devices import d_devices, network_devices, l_platforms
from napalm_functions import get_connection, get_checkpoint

platform = "nxos"

if __name__ == "__main__":
    my_device = d_devices[platform]
    print("")
    print("Open device connection")
    device = get_connection(my_device)

