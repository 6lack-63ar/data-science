# -*- coding: utf-8 -*-
"""
Created on Sat Jan 14 13:04:08 2023

@author: B3ar
"""

def myfunc(k):
    return lambda a :a*k
trippler = myfunc(3)
qud = myfunc(4)

print("trippler :",trippler(10))
print("quad :",qud(4))