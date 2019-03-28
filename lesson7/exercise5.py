#!/usr/bin/env python3
"""
exercise 5 lxml and namespaces
"""

from lxml import etree
from pprint import pprint

def openlxml(filename):
    with open(filename, 'rb' ) as f:
        lines = f.read()
    return etree.fromstring(lines)

if __name__ == "__main__":
    filename = "show_version.xml"
    my_xml = openlxml(filename)

    # Task a
    print("")
    print("Print Namespace Map : ")
    print(my_xml.nsmap)

    # Task b
    print("")
    print("Print Processor board ID : ")
    xmldata = my_xml.find(".//{*}proc_board_id")
    print(xmldata.tag)
    print(xmldata.text)

