#!/usr/bin/python

## 1163. Java vs C ++  Problem code: JAVAC
import re

n = str(raw_input())
cadena = []

while n != 'Error!':
    if '_' in n:  # Es java
        
        cadena = [x for x in n.split('_')]
        res = cadena.pop(0)

        for a in cadena:
            res = res + a[0].upper() + a[1:]

        print res 
        

    else:  # Es C
        cadena = re.sub('([a-z0-9])([A-Z])', r'\1_\2', n).lower()
        print cadena



    n = str(raw_input())
