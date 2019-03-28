#!/usr/bin/env python3
"""
exercise 1d lxml

"""

from lxml import etree

f = open("show_security_zones.xml")
lines = f.read()
my_xml = etree.fromstring(lines)

print(my_xml.getchildren()[0].tag)
print(my_xml[0].tag)

