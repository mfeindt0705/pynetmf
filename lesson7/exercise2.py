#!/usr/bin/env python3
"""
exerrcise 2 

2a. Using xmltodict, load the show_security_zones.xml file as a Python dictionary. Print out this new variable and its type. 
Note, the newly created object is an OrderedDict; not a traditional dictionary.

2b. Print the names and an index number of each security zone in the XML data from Exercise 2a. 
Your output should look similar to the following (tip, enumerate will probably help): 
Security Zone #1: trust
Security Zone #2: untrust
Security Zone #3: junos-host


"""

from pprint import pprint
import xmltodict

with open("show_security_zones.xml") as f:
    xmldata = f.read().strip()
    my_xml = xmltodict.parse(xmldata)

print("New variable and its type :")
print(type(my_xml))
print(my_xml)
print("*" * 20)

xml_data = my_xml['zones-information']['zones-security']

print("New Security Zone and its name :")
for idx, vdict in enumerate(xml_data):
    print("Security Zone #{0} with name {1}".format(idx, vdict['zones-security-zonename']))

print("*" * 20)

print("New Security Zone and its name :")
for idx, vdict in enumerate(xml_data):
    print(f"Security Zone #{idx} with name {vdict['zones-security-zonename']}")

print("*" * 20)

