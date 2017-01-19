#!/usr/bin/python
import sys

lines = sys.stdin.readlines()

def promedio(x):
    b =0
    for j in range(len(x)):
        b = x[j] + b
    return b/len(x)

def mayores(z, pr):
    rs = 0
    for p in range(len(z)):
        if z[p] &gt; pr:
            rs = rs + z[p] - pr
        
    return rs

counter = 0
while(lines[counter] != "-1\n"):
    
    cases = int(lines[counter])
    counter += 1
    
    l = []
    for a in range(cases):
        l.append(float(lines[counter]))
        counter += 1
    pro = promedio(l) 
    
    if pro % 1 == 0:    
        may_sum=mayores(l, pro)
        print int(may_sum)
    else:
        print -1
       