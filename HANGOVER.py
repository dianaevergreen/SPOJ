#!/usr/bin/python

import sys

lines = sys.stdin.readlines()



for a in lines:
    x=float(a)
    if(x != 0.00):
        counter = 1.00
        float(counter)
        h = 0.00
        float(h)
        while h &lt; x:
            h += 1.00/(counter + 1.00)
            
            counter += 1.00

        print int(counter)- 1, "card(s)"
        

