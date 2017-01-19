#!/usr/bin/python
import sys

n = sys.stdin.readlines()

cases = n[0]
lista = []
resultado = []

for i in n[1:]:
    lista = i.split()
    primero = int(lista[0])
    segundo = int(lista[1])

    if(primero - segundo &lt; 3 and primero &gt;= segundo):
        if (primero % 2 != 0 and segundo  % 2 != 0): 
            resultado.append(primero + segundo - 1)
        elif (primero % 2 == 0 and segundo  % 2 == 0):
            resultado.append(primero + segundo)
        else:
            resultado.append("No Number")
    else:
        resultado.append("No Number")
        
for b in resultado:
    print b    
    