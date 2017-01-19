#!/usr/bin/python
import sys


lines = sys.stdin.readlines()

for i in range(len(lines)):
    if  i%2 == 0 and lines[i] != "0\n":
        proxlinea= lines[i+1]
        array = [int(j) for j in proxlinea.split()]
        a = []
        d = dict()
        valores = []

        for b in range(len(array)):
            d[array[b] ] = b+1   
        valores = d.values()
        strval = [str(h) for h in valores]
        
        repinga = proxlinea.split()
        
        
        if strval == repinga:
            print "ambiguous"
        else:
            print "not ambiguous"
