#!/usr/bin/env python3
"""
exercise 2a for jinja rendering

"""

from __future__ import unicode_literals, print_function
from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment
from pprint import pprint

env = Environment(undefined=StrictUndefined)
env.loader = FileSystemLoader("./templates")

template_file = "exercise2_template_a.j2"

nxos_1 = {
    "intf_name": "Ethernet2/1",
    "ipv4": "10.1.100.1",
    "mask": "24"
}

nxos_2 = {
    "intf_name": "Ethernet2/1",
    "ipv4": "10.1.100.2",
    "mask": "24"
}

template_vars = (nxos_1, nxos_2)

template = env.get_template(template_file)
for fvars in template_vars:
    output = template.render(**fvars)
    print("NXOS Rendering")
    print(output)
    print("")

