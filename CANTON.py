#!/usr/bin/python

import sys

lines = sys.stdin.readlines()

cases = lines[0]


for i in lines[1:]:
    a = 1
    b = 0
    while b &lt; int(i):
        b += a  
        a += 1   ## Fila a- 1
    fila = a - 1
    pos = b - int(i)
    
    if fila % 2 == 0:
        x = 1
        y = fila
        while(pos + 1 &lt; fila): 
            
            pos += 1
            x += 1
            y -= 1
        print  "TERM %d IS %d/%d" % (int(i),x,y)
    else:
        y = 1
        x = fila
        while(pos &gt; 0):
            pos -= 1
            
            y += 1
            x -= 1  
        print  "TERM %d IS %d/%d" % (int(i),y,x)
              
        
               