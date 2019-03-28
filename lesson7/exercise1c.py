#!/usr/bin/env python3
"""
exercise 1c lxml

"""

from lxml import etree

f = open("show_security_zones.xml")
lines = f.read()

my_xml = etree.fromstring(lines)
print(my_xml.tag)

print(len(my_xml))
print(len(my_xml.getchildren()))

