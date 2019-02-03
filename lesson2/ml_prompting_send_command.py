"""
exercise demonstrating the send_command mnethod using the expect_string parameter
"""

from netmiko import ConnectHandler
from getpass import getpass

device1 = {
    "host": "cisco3.lasthop.io",
    "username": "pyclass",
    "password": getpass(),
    "device_type": "cisco_ios",
}

net_connect = ConnectHandler(**device1)
print(net_connect.find_prompt())

command = "delete flash:/cisco_file.txt"
output = net_connect.send_command(
    command, expect_string=r"cisco_file.txt", strip_prompt=False, strip_command=False
)
output = net_connect.send_command(
    "cisco_file.txt", expect_string=r"confirm", strip_prompt=False, strip_command=False
)
output = net_connect.send_command(
    "y", expect_string=r"#", strip_prompt=False, strip_command=False
)
print(output)
net_connect.disconnect()
