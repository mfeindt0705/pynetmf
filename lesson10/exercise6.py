#!/usr/bin/env python3
"""
Create a new program that completes the same task as Exercise 3b except using multiple processes (i.e. a 'ProcessPoolExecutor').
"""

from concurrent.futures import ProcessPoolExecutor, as_completed
from datetime import datetime
from my_devices_mf import device_list
from my_functions_mf import ssh_command
import warnings
warnings.filterwarnings(action='ignore', module='.*paramiko.*')
from pprint import pprint

def main():
    start_time = datetime.now()
    max_threads = 6
    cmd_list = []
    for device in device_list:
        cmd_list.append("show ip arp")
    # use context manager to gracefgully cleanup the pool
    with ProcessPoolExecutor(max_threads) as pool:
        results_generator = pool.map(ssh_command, device_list, cmd_list)

    # process as completed
    for result in results_generator:
        print("-" * 40)
        pprint(result)
        print("-" * 40)
        print("\n\n")        
    print("\nBenoetigte Zeit: " + str(datetime.now() - start_time))
    return None


if __name__ == "__main__":
    main()

