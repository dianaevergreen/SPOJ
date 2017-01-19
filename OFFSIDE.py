#!/usr/bin/python

### Problem code: OFFSIDE ###

import sys

lines = sys.stdin.readlines()
counter = 0

for n in lines:
    l = [int(c) for c in n.split()]
    
    if counter == 0:
        if l[0] == 0 and l[1] == 0:
            break
        else:
          counter += 1
          continue

    elif counter == 1:
        counter += 1
        l.sort()
        a = l
        

    elif counter == 2:
        counter = 0
        l.sort()
        d = l
        if a[0] &lt; d[1]:
            print "Y"
        else:
            print "N"
       
