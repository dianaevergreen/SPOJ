#!/usr/bin/python

import sys

lines = sys.stdin.readlines()

numbers = [float(a) for a in lines]

for b in numbers:
    if(b != 0):
        r = b/3.14159265358979323846264
        area= 3.14159265358979323846264*(r**2)/2
        print("%.2f" % area)
    
