#!/usr/bin/env python3
"""
NAPALM using nxos_ssh has the following data structure in one of its unit tests (the below data is in JSON format).  
{
    "Ethernet2/1": {
        "ipv4": {
            "1.1.1.1": {
                "prefix_length": 24
            }
        }
    },
    "Ethernet2/2": {
        "ipv4": {
            "2.2.2.2": {
                "prefix_length": 27
            }, 
            "3.3.3.3": {
                "prefix_length": 25
            }
        }
    }, 
    "Ethernet2/3": {
        "ipv4": {
            "4.4.4.4": {
                "prefix_length": 16
            }
        }, 
        "ipv6": {
            "fe80::2ec2:60ff:fe4f:feb2": {
                "prefix_length": 64
            }, 
            "2001:db8::1": {
                "prefix_length": 10
            }
        }
    }, 
    "Ethernet2/4": {
        "ipv6": {
            "fe80::2ec2:60ff:fe4f:feb2": {
                "prefix_length": 64
            }, 
            "2001:11:2233::a1": {
                "prefix_length": 24
            }, 
            "2001:cc11:22bb:0:2ec2:60ff:fe4f:feb2": {
                "prefix_length": 64
            }
        }
    } 
}
Read this JSON data in from a file.

From this data structure extract all of the IPv4 and IPv6 addresses that are used on this NXOS device. 
From this data create two lists: 'ipv4_list' and 'ipv6_list'. 
The 'ipv4_list' should be a list of all of the IPv4 addresses including prefixes; 
the 'ipv6_list' should be a list of all of the IPv6 addresses including prefixes.
"""

import json

ipv4_list = []
ipv6_list = []

filename = "nxosinterfaces.json"
with open(filename, 'r') as f:
    ip_data = json.load(f)

for key1, ip_item1 in ip_data.items():
    for key2, ip_item2 in ip_item1.items():
        for key3, ip_item3 in ip_item2.items():
            new_ip = ""
            new_ip = str(key3) + "/" + str(ip_item3['prefix_length'])
            if key2 == 'ipv4':
                ipv4_list.append(new_ip)
            else:
                ipv6_list.append(new_ip)

print(ipv4_list)
print(ipv6_list)
