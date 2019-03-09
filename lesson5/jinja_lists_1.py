#!/usr/bin/env python3
"""
simple exercise jinja rendering
"""
from __future__ import unicode_literals, print_function
from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment
from pprint import pprint

env = Environment(undefined=StrictUndefined)
env.loader = FileSystemLoader(".")

# create the interface list
base_intf = "GigabitEthernet0/1/"
intf_list = []
for intf_number in range(24):
    intf_name = f"{base_intf}{intf_number}"
    intf_list.append(intf_name)

# generate a dict from the interface list
intf_vars = {"intf_list": intf_list}

template_file = "list_template_1.j2"
template = env.get_template(template_file)
output = template.render(**intf_vars)
pprint(output)

