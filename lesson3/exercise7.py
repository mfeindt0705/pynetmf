#!/usr/bin/env python3

"""

From this BGP configuration, retrieve all of BGP peer IP addresses and their corresponding remote-as. 
Return a list of tuples. The tuples should be (neighbor_ip, remote_as). 
Print your data-structure to standard output.

Your output should look similar to the following. Use ciscoconfparse to accomplish this. 
​BGP Peers: 
[('10.220.88.20', '42'), ('10.220.88.32', '43')]

"""

from netmiko import ConnectHandler
from ciscoconfparse import CiscoConfParse


bgp_config = """
router bgp 44
 bgp router-id 10.220.88.38
 address-family ipv4 unicast
 !
 neighbor 10.220.88.20
  remote-as 42
  description pynet-rtr1
  address-family ipv4 unicast
   route-policy ALLOW in
   route-policy ALLOW out
  !
 !
 neighbor 10.220.88.32
  remote-as 43
  address-family ipv4 unicast
   route-policy ALLOW in
   route-policy ALLOW out
"""

bgp_peers = []
bgp_config = bgp_config.splitlines()
bgp_parse = CiscoConfParse(bgp_config)
bgp_neighbors = bgp_parse.find_objects_w_child(parentspec=r"\sneighbor", childspec=r"\sremote-as")
for neighbor in bgp_neighbors:
    str_neighbor = neighbor.text.strip()
    _, ip_neighbor = str_neighbor.split()
    for cmd in neighbor.re_search_children(r"\sremote-as"):
        str_remote_as = cmd.text.strip()
        _, remote_as = str_remote_as.split()
    new_peer = (ip_neighbor, remote_as)
    bgp_peers.append(new_peer)

print()
print("*" * 12)
print(bgp_peers)
print("*" * 12)

