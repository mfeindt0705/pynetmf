#!/usr/bin/env python3
"""
exercise 3 for Arista eAPI
"""

import pyeapi
from getpass import getpass
from pprint import pprint
from exercise2b_my_funcs import load_yaml, print_routes


def main():
    arista_file = "arista.yml"
    arista_dict = load_yaml(arista_file)
    password = getpass(prompt="Password :")
    for name, values in arista_dict.items():
        values['password'] = password
        connection = pyeapi.client.connect(**values)
        device = pyeapi.client.Node(connection)
        output = device.enable(["show ip route"])
        #pprint(output)
        print_routes(output)

if __name__ == "__main__":
    main()

