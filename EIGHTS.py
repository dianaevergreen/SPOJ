#!/usr/bin/python

import sys

lines = sys.stdin.readlines()

cases = lines[0]

def menor4(x):
    if x == 1:
        
        return 192
    elif x == 2:
        return 442
    elif x == 3:
        return 692
    elif x == 4 or x == 0:
        return 942
    


for i in lines[1:]:
    a  = int(i)
    if a &lt;= 4:
        print menor4(a)
    else:
        pref = a/4
        pos=str(menor4(a % 4))
        if a % 4 ==0:
            pref = pref - 1
            prefx = str(pref)
            
        else:
            
            prefx = str(pref)
            
        
        print ''.join((prefx,pos))