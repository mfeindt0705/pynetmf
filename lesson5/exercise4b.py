#!/usr/bin/env python3
"""
exercise 4 for jinja rendering
"""

from __future__ import unicode_literals, print_function
from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment

env = Environment(undefined=StrictUndefined)
env.loader = FileSystemLoader("./templates")


my_vars = [
    {"vrf_name": "blue1", "rd_num": "100:1", "ipv4": True, "ipv6": True},
    {"vrf_name": "blue2", "rd_num": "100:2", "ipv4": True, "ipv6": True},
    {"vrf_name": "blue3", "rd_num": "100:3", "ipv4": True, "ipv6": True},
    {"vrf_name": "blue4", "rd_num": "100:4", "ipv4": True, "ipv6": True},
    {"vrf_name": "blue5", "rd_num": "100:5", "ipv4": True, "ipv6": True},
]

v_vrfs = {"my_vars": my_vars}

template_file = "exercise4_template.j2"
template = env.get_template(template_file)

output = template.render(**v_vrfs)
print(output)


