#!/usr/bin/env python3
"""
exercise 2b for jinja rendering

"""

from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment

env = Environment(undefined=StrictUndefined)
env.loader = FileSystemLoader("./templates")

template_file = "exercise2_template_b.j2"

nxos_1 = {
    "intf_name": "Ethernet2/1",
    "ipv4": "10.1.100.1",
    "mask": "24",
    "local_as": "22",
    "peer_ip": "10.1.100.2",
    "hostname": "NXOS1"
}

nxos_2 = {
    "intf_name": "Ethernet2/1",
    "ipv4": "10.1.100.2",
    "mask": "24",
    "local_as": "22",
    "peer_ip": "10.1.100.1",
    "hostname": "NXOS2"
}

template_vars = (nxos_1, nxos_2)

#template = env.get_template(template_file)

for fvars in template_vars:
    print("New rendering for {0:s}".format(fvars["hostname"]))
    template = env.get_template(template_file)
    output = template.render(**fvars)
    print(output)
    print("")

