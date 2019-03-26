#!/usr/bin/env python3
"""
exercise 3 xmltodict
"""

import xmltodict

def openxmlasdict(filename):
    with open(filename) as f:
        xmldata = f.read().strip()
    return xmltodict.parse(xmldata)

sec_zones = openxmlasdict("show_security_zones.xml")
sec_zones_trust = openxmlasdict("show_security_zones_trust.xml")

print("Security Zones :")
print(type(sec_zones['zones-information']['zones-security']))


print("Security Zones Trust :")
print(type(sec_zones_trust['zones-information']['zones-security']))

