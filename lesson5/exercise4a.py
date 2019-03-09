#!/usr/bin/env python3
"""
exercise 4 for jinja rendering
"""

from __future__ import unicode_literals, print_function
from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment

env = Environment(undefined=StrictUndefined)
env.loader = FileSystemLoader("./templates")


my_vrfs = [
    {"vrf_name": "blue1", "rd_num": "100:1", "ipv4": True, "ipv6": True},
    {"vrf_name": "blue2", "rd_num": "100:2", "ipv4": True, "ipv6": True},
    {"vrf_name": "blue3", "rd_num": "100:3", "ipv4": True, "ipv6": True},
    {"vrf_name": "blue4", "rd_num": "100:4", "ipv4": True, "ipv6": True},
    {"vrf_name": "blue5", "rd_num": "100:5", "ipv4": True, "ipv6": True},
]

template_file = "exercise3_template.j2"

for vvrf in my_vrfs:
    template = env.get_template(template_file)
    output = template.render(**vvrf)
    print(output)

