#!/usr/bin/env python3
"""
simple exercise using the pyeapi Arista module
"""

import pyeapi

device1 = pyeapi.connect_to("arista8")
#device2 = pyeapi.connect_to("arista7")
print(device1)

