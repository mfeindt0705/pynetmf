#!/usr/bin/env python3
"""
exercise 2b for Arista eAPI
"""

from getpass import getpass
import pyeapi
from exercise2b_my_funcs import load_yaml, print_output

arista_file = "arista.yml"
arista_dict = load_yaml(arista_file)


def main():
    for name, values in arista_dict.items():
        values['password'] = getpass(prompt="Password :")
        connection = pyeapi.client.connect(**values)
        device = pyeapi.client.Node(connection)
        output = device.enable(["show ip arp"])
        print_output(output)


if __name__ == "__main__":
    main()



