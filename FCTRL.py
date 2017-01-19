#!/usr/bin/python
import math
import sys

N=sys.stdin.readlines()
cant = int(N[0])
lista = []

if len(N)!=cant+1:
    while True:
        pass

for line in N[1:]:
    number = int(line)
    counter = 1
    dia = 0
    p = 5
    


    while (number/p) &gt;= 1 :
        

        dia += number/(p)
        p *= 5
    lista.append(dia)


print "\n".join(str(a) for a in lista)
    
