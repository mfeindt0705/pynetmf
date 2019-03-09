#!/usr/bin/env python3
"""
exercise3 for jinja rendering

"""

from __future__ import unicode_literals, print_function
from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment

env = Environment(undefined=StrictUndefined)
env.loader = FileSystemLoader("./templates")

template_file = "exercise3_template.j2"

template_vars = {"vrf_name": "blue",
                 "rd_num": "100",
                 "ipv4": True,
                 "ipv6": False,
                 }

template = env.get_template(template_file)

output = template.render(**template_vars)

print(output)



