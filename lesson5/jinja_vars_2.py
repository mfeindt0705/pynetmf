#!/usr/bin/env python3
"""
simple exercise for jinja rendering
"""

from jinja2 import Template

bgp_config = """
router bgp {{ bgp_as }}
 bgp router-id {{ router_id }}
 bgp log-neighbor-changes
 neighbor {{ peer1 }} remote-as 44
"""

j2_template = Template(bgp_config)
output = j2_template.render(bgp_as=22, router_id="1.1.1.1", peer1="10.20.30.1")
print(output)
