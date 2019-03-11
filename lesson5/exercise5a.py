#!/usr/bin/env python3
"""
exercise 5 for jinja 
"""

from __future__ import unicode_literals, print_function

from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment

env = Environment(undefined=StrictUndefined)
env.loader = FileSystemLoader("./templates")

template_file = "exercise5_template_cisco3.j2"

my_vars = {"ntp1": "130.126.24.24",
           "ntp2": "152.2.21.1",
           "offset": "-8",
           "timezone": "PST",
           "timezone_summer": "PDT",
           }

template = env.get_template(template_file)
output = template.render(**my_vars)
print(output)

