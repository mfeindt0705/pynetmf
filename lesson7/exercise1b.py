#!/usr/bin/nv python3


from lxml import etree

f = open("show_security_zones.xml")

lines = f.read()
my_xml = etree.fromstring(lines)
bstring = etree.tostring(my_xml)
print(bstring.decode())


