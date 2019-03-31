#!/usr/bin/env python3
"""
exercise 4 napalm
"""

from pprint import pprint

from napalm_devices import d_devices, network_devices, l_platforms
from napalm_functions import get_connection, get_checkpoint

platform = "nxos"
suffix = "_checkpoint.txt"
nxos1_conf_merge = "nxos1.lasthop.io_replace.txt"

if __name__ == "__main__":
    my_device = d_devices[platform]
    print("")
    print("Open device connection")
    device = get_connection(my_device)
    print(get_checkpoint(device, suffix))
    print(">>>Load config change (replace)")
    device.load_replace_candidate(filename=nxos1_conf_merge)
    print(device.compare_config())
    device.discard_config()
    device.close()

