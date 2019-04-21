#!/usr/bin/env python3
"""
Create a Python script that executes "show version" on each of the network devices defined in my_devices.py. 
This script should execute serially
"""

from datetime import datetime
from netmiko import ConnectHandler
from my_devices_mf import device_list as devices
import warnings
warnings.filterwarnings(action='ignore', module='.*paramiko.*')


def show_version(device):
    net_connect = ConnectHandler(**device)
    # send show version and wait for prompt
    output = net_connect.send_command_expect("show version")
    net_connect.disconnect()
    return output

def ssh_command(device, show_command):
    net_connect = ConnectHandler(**device)
    # send show command and wait for prompt
    output = net_connect.send_command_expect(show_command)
    net_connect.disconnect()
    return output


def main():
    """
    Use Netmiko to connect to each of the devices. Execute
    'show version' on each device. Record the amount of time required to do this
    """
    start_time = datetime.now()
    for device in devices:
        print()
        print('#' * 40)
        output = ssh_command(device, "show version")
        print(output)
        print()
        print('#' * 40) 
    print("\nBenoetigte Zeit: " + str(datetime.now() - start_time))
    return None


if __name__ == "__main__":
    main()

