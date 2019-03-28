#!/usr/bin/env python3
"""
exercise 3 xmltodict
"""

import xmltodict

def openxmlasdict(filename):
    with open(filename) as f:
        xmldata = f.read().strip()
    return xmltodict.parse(xmldata)

def forceopenxmlasdict(filename, force_list=None):
    with open(filename) as f:
        xmldata = f.read().strip()
    return xmltodict.parse(xmldata, force_list=force_list)


if __name__ == "__main__":
    sec_zones = openxmlasdict("show_security_zones.xml")
    sec_zones_trust = openxmlasdict("show_security_zones_trust.xml")
    print("Security Zones :")
    print(type(sec_zones['zones-information']['zones-security']))
    print("Security Zones Trust :")
    print(type(sec_zones_trust['zones-information']['zones-security']))
    print("Security Zones Trust Force:")
    sec_zones_trust_force = forceopenxmlasdict("show_security_zones_trust.xml", force_list={"zones-security": True})
    print(type(sec_zones_trust_force['zones-information']['zones-security']))

