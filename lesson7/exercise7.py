#!/usr/bin/env python3
"""
exercise 7 nxapi with xml


"""

import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from getpass import getpass
from nxapi_plumbing import Device
from lxml import etree

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

device = Device(
    api_format="xml",
    host="nxos1.lasthop.io",
    username="pyclass",
    password=getpass("Bitte Passwort eingeben : "),
    transport="https",
    port=8443,
    verify=False,
)

if __name__ == "__main__":
    output = device.show("show interface Ethernet2/1")

    # Task a
    print("-" * 20)
    print("Interface Report : ")
    print("Interface : {0}, State : {1}, MTU : {2}".format(output.find(".//interface").text, output.find(".//admin_state").text, output.find(".//eth_mtu").text))

    # Task b
    list_cmds = ["show system uptime", "show system resources"]
    output = device.show_list(list_cmds)
    print("")
    print("-" * 20)
    print("System Report :")
    for element in output:
        bstring = etree.tostring(element)
        print(bstring.decode())


    # Task c
    list_cmds = ["interface loopback151", "description dev01", "ip address 10.111.222.254/32"]
    output = device.config_list(list_cmds)
    bstring = etree.tostring(element)
    print(bstring.decode())


