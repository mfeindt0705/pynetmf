#!/usr/bin/env python3
"""
Complete the same task as Exercise 1b except this time use "legacy" threads to create a solution
"""

from __future__ import print_function, unicode_literals
import threading
from datetime import datetime
from my_devices_mf import device_list as devices
from my_functions_mf import show_version2
import warnings
warnings.filterwarnings(action='ignore', module='.*paramiko.*')


def main():
    """
    Use threads and Netmiko to connect to each of the devices. Execute
    'show version' on each device. Record the amount of time required to do this.
    """
    start_time = datetime.now()
    for device in devices:
        my_thread = threading.Thread(target=show_version2, args=(device,))
        my_thread.start()
        
    main_thread = threading.main_thread()
    for some_thread in threading.enumerate():
        if some_thread != main_thread:
            print(some_thread)
            some_thread.join()

    print("\nBenoetigte Zeit: " + str(datetime.now() - start_time))
    return None


if __name__ == "__main__":
    main()
