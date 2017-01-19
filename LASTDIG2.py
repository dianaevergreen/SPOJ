#!/usr/bin/python

# 3442. The last digit  Problem code: LASTDIG
import math
cases = int(input())

for c in range(cases):
    (a, b) = (int(x) for x in raw_input().split())
    if b == 0:
        print 1
    else:    
        a = a%10
        b = b%4
        if b==0:
            b = 4
        print pow(a,b)%10
