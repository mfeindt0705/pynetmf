#!/usr/bin/env python3
"""
exercise 4 lxml
"""

from lxml import etree
from pprint import pprint

def openlxml(filename):
    with open(filename) as f:
        lines = f.read()
    return etree.fromstring(lines)


if __name__ == "__main__":
    filename = "show_security_zones.xml"
    my_xml = openlxml(filename)

    # Task a
    xml_data = my_xml.find("zones-security")
    print("Find tag of the first zones-security element")
    print("-" * 20)
    print(f"Tag is : {xml_data.tag}")
    print("")
    print("Find tag of all child elements of the first zones - security element")
    print("-" * 20)
    for child in xml_data:
        print(child.tag)

    # Task b
    print("")
    xml_data = my_xml.find(".//zones-security-zonename")
    print(f"Zonename String : {xml_data.text}")

    # Task c
    print("")
    xml_data = my_xml.findall(".//zones-security-zonename")
    for element in xml_data:
        print(f"Zonename String : {element.text}")

