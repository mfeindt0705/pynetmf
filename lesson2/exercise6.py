#!/usr/bin/env python3
"""
Using SSH and netmiko connect to the Cisco4 router. 
In your device definition, specify both an secret and a session_log. 

Execute the following sequence of events using Netmiko:
a. Print the current prompt using find_prompt()

b. Execute the config_mode() method and print the new prompt using find_prompt()

c. Execute the exit_config_mode() method and print the new prompt using find_prompt()

d. Use the write_channel() method to send the 'disable' command down the SSH channel. 
   Note, write_channel is a low level method so it requires that you add a newline to the end of your 'disable' command.

e. time.sleep for two seconds and then use the read_channel() method to read the data that is currently available on the SSH channel. 
   Print this to the screen.

f. Execute the enable() method and print your now current prompt using find_prompt(). 
   The enable() method will use the 'secret' defined in your device definition. 
    This 'secret' is the same as the standard lab password.

g. After you are done executing your script, look at the 'my_output.txt' file to see what is included in the session_log.

"""

from netmiko import ConnectHandler
from getpass import getpass
from datetime import datetime
import time

password = getpass(prompt="Bitte Passwort eingeben : ")

cisco_ios4 = {"host": "cisco4.lasthop.io",
              "username": "pyclass",
              "password": password,
              "device_type": "cisco_ios",
              "session_log": "my_session.txt",
              "secret": password}

ios_connect = ConnectHandler(**cisco_ios4)
print("Current prompt :" + str(ios_connect.find_prompt()))
ios_connect.config_mode()
print("Current prompt :" + str(ios_connect.find_prompt()))
ios_connect.exit_config_mode()
print("Current prompt :" + str(ios_connect.find_prompt()))
ios_connect.write_channel("disable\n")
print("Current prompt :" + str(ios_connect.find_prompt()))
time.sleep(2)
output = ios_connect.read_channel()
print(output)
ios_connect.enable()
print("Current prompt :" + str(ios_connect.find_prompt()))


ios_connect.disconnect()

