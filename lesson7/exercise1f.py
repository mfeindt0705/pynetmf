#!/usr/bin/env python3
"""
exercise 1f lxml
"""

from lxml import etree

with open("show_security_zones.xml") as f:
    lines = f.read()
    my_xml = etree.fromstring(lines)

trust_zone = my_xml[0]

for element in trust_zone.getchildren():
    print(element.tag)

