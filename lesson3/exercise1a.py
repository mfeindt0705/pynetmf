#!/usr/bin/env python
"""
Using the below ARP data, create a five element list. 
Each list element should be a dictionary with the following keys: "mac_addr", "ip_addr", "interface". 
At the end of this process, you should have five dictionaries contained inside a single list. 
Protocol  Address      Age  Hardware Addr   Type  Interface
Internet  10.220.88.1   67  0062.ec29.70fe  ARPA  Gi0/0/0
Internet  10.220.88.20  29  c89c.1dea.0eb6  ARPA  Gi0/0/0
Internet  10.220.88.22   -  a093.5141.b780  ARPA  Gi0/0/0
Internet  10.220.88.37 104  0001.00ff.0001  ARPA  Gi0/0/0
Internet  10.220.88.38 161  0002.00ff.0001  ARPA  Gi0/0/0
"""

import re
from pprint import pprint

arp_entries = """
Protocol  Address      Age  Hardware Addr   Type  Interface
Internet  10.220.88.1   67  0062.ec29.70fe  ARPA  Gi0/0/0
Internet  10.220.88.20  29  c89c.1dea.0eb6  ARPA  Gi0/0/0
Internet  10.220.88.22   -  a093.5141.b780  ARPA  Gi0/0/0
Internet  10.220.88.37 104  0001.00ff.0001  ARPA  Gi0/0/0
Internet  10.220.88.38 161  0002.00ff.0001  ARPA  Gi0/0/0
"""

arp_entries = arp_entries.strip()
arp_lines = arp_entries.splitlines()

new_arp_list = []
for arp in arp_lines:
    if re.search(r"^Protocol", arp):
        continue
    arp_entry = arp.split()
    _, ipaddress, _, macaddress, _, interface = arp_entry
    new_entry = {"ip_address": ipaddress, "mac_addr": macaddress, "interface": interface}
    new_arp_list.append(new_entry)

print("*" * 12)
pprint(new_arp_list)
print("*" * 12)


