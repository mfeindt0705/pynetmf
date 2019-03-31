#!/usr/bin/env python3
"""
exercise 2 napalm

"""

from pprint import pprint

from napalm_devices import d_devices, network_devices
from napalm_functions import get_connection



if __name__ == "__main__":
    for my_device in network_devices:
        print("")
        print("Open device connection")
        device = get_connection(my_device)
        try:
            output = device.get_ntp_peers()
            pprint(output)
            device.close()
        except NotImplementedError as error:
            error = "NotImplementedError"
            print(f"ExceptionError : {error}")
            device.close()

