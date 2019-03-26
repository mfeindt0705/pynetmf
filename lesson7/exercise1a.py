#!/usr/bin/env python3
"""
Using the show_security_zones.xml file, read the file contents and parse the file using etree.fromstring(). 
Print out the newly created XML variable and also print out the variable's type. 

"""

from lxml import etree

print("parse method")
f = open("show_security_zones.xml")
my_xml = etree.parse(f)
root = my_xml.getroot()
print(root)
print(type(root))


print("fromstring method")
f = open("show_security_zones.xml")

lines = f.read()
my_xml = etree.fromstring(lines)
print(my_xml)
print(type(my_xml))
