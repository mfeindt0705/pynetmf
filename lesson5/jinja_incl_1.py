#!/usr/bin/env python3
"""
simple exercise for jinja rendering
"""

from __future__ import unicode_literals, print_function
from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment

env = Environment(undefined=StrictUndefined)
env.loader = FileSystemLoader(".")

template_vars = {}

template_file = "incl_template_1.j2"
template = env.get_template(template_file)
output = template.render(**template_vars)
print(output)

