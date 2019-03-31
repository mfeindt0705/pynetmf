#!/usr/bin/env python3
"""
exercise 3 napalm
"""

from pprint import pprint

from napalm_devices import d_devices, network_devices, l_platforms
from napalm_functions import get_connection


cisco3_conf_merge = "cisco3.lasthop.io-loopbacks.txt"
arista1_conf_merge = "arista1.lasthop.io-loopbacks.txt"

d_conf_merge = {"cisco": cisco3_conf_merge,
                "arista": arista1_conf_merge}



if __name__ == "__main__":
    for platform in l_platforms:
        file_conf_merge = d_conf_merge[platform]
        my_device = d_devices[platform]
        print("")
        print("Open device connection")
        device = get_connection(my_device)
        print("")
        # output = device.get_facts()
        # pprint(output)
        # device.close()
        print(">>>Load config change (merge) - no commit")
        device.load_merge_candidate(file_conf_merge)
        print(device.compare_config())
        print(">>>Discard config change (merge)")
        device.discard_config()
        # print(">>>Load config change (merge) - commit")
        # device.commit_config()
        device.close()

