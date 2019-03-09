#!/usr/bin/env python3
"""
exercise 1 jinja rendering
"""

from __future__ import unicode_literals, print_function
from jinja2 import FileSystemLoader, StrictUndefined, Template
from jinja2.environment import Environment

env = Environment(undefined=StrictUndefined)
env.loader = FileSystemLoader("./templates")

template_bgp = """
router bgp {{ local_as }}
  neighbor {{ peer1_ip }} remote-as {{ peer1_as }}
    update-source loopback99
    ebgp-multihop 2
    address-family ipv4 unicast
  neighbor {{ peer2_ip }} remote-as {{ per2_as}}
    address-family ipv4 unicast
"""

template_file = "exercise1_template.j2"

template_vars = { 
    "local_as": 10,
    "peer1_ip": "10.1.20.2",
    "peer1_as": 20,
    "peer2_ip": "10.1.30.2",
    "peer2_as": 30
}


template = env.get_template(template_file)
output = template.render(**template_vars)
print("First Rendering")
print(output)

bgp_template = Template(template_bgp)
output = bgp_template.render(**template_vars)
print("Second Rendering")
print(output)
