#!/usr/bin/env python3
"""
Using your TextFSM template and the 'show interface status' data from exercise2, 
create a Python program that uses TextFSM to parse this data. In this Python program, 
read the show interface status data from a file and process it using the TextFSM template. 
From this parsed-output, create a list of dictionaries. 
"""

from pprint import pprint
import textfsm

vtemplate = "ex2_1.template"
vfilename = "ex1_show_int_status.txt"

# read the input file as a string !
with open(vfilename, 'r') as f:
    show_int_data = f.read()

with open(vtemplate, 'r') as t:
    re_table = textfsm.TextFSM(t)

fsm_results = re_table.ParseText(show_int_data)

pprint(fsm_results)

dict_keys = re_table.header
vlist = []

for entry in fsm_results:
    entry_dict = dict(zip(dict_keys, entry))
    vlist.append(entry_dict) 

print()
print("*" * 12)
pprint(vlist)
print("*" * 12)

