#!/usr/bin/env python3
"""
Using the "ThreadPoolExecutor" in Concurrent Futures execute "show version" on each of the devices defined in my_devices.py. 
Use the 'wait' method to ensure all of the futures have completed. 
Print the total execution time required to accomplish this task.
"""

from concurrent.futures import ThreadPoolExecutor, wait
from datetime import datetime
from my_devices_mf import device_list as devices
from my_functions_mf import ssh_command
import warnings
warnings.filterwarnings(action='ignore', module='.*paramiko.*')


def main():
    start_time = datetime.now()
    max_threads = 6
    pool = ThreadPoolExecutor(max_threads)
    thread_list = []
    for device in devices:
        new_thread = pool.submit(ssh_command, device, "show version")
        thread_list.append(new_thread)
    # wait until all started threads are done
    wait(thread_list)

    for new_thread in thread_list:
        print("-" * 40)
        print("Result: " + new_thread.result())
        print("-" * 40)
        print("\n\n")        
    print("\nBenoetigte Zeit: " + str(datetime.now() - start_time))
    return None


if __name__ == "__main__":
    main()

