#!/usr/bin/env python
"""
For one of the Cisco IOS devices, use Netmiko and the send_command() method to retrieve 'show version'. 
Save this output to a file in the current working directory.
"""

from netmiko import ConnectHandler
from getpass import getpass


