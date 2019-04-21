#!/usr/bin/env python3
"""
Create a new program that completes the same task as Exercise 3b except using multiple processes (i.e. a 'ProcessPoolExecutor').
"""

from concurrent.futures import ProcessPoolExecutor, as_completed
from datetime import datetime
from my_devices_mf import device_list as devices
from my_functions_mf import ssh_command
import warnings
warnings.filterwarnings(action='ignore', module='.*paramiko.*')


def main():
    start_time = datetime.now()
    max_threads = 6
    # use context manager to gracefgully cleanup the pool
    with ProcessPoolExecutor(max_threads) as pool:
        process_list = []
        for device in devices:
            new_process = pool.submit(ssh_command, device, "show version")
            process_list.append(new_process)

    # process as completed
    for new_process in as_completed(process_list):
        print("-" * 40)
        print("Result: " + new_process.result())
        print("-" * 40)
        print("\n\n")
    print("\nBenoetigte Zeit: " + str(datetime.now() - start_time))
    return None


if __name__ == "__main__":
    main()

