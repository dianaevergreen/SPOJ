#!/usr/bin/python
import sys


pila = []
arreglo = []

n = sys.stdin.readlines()

cases = n[0]


for lines in n[1:]:
    caracteres = list(lines)
    
    for a in range(len(caracteres)):
        if caracteres[a].isalpha():     #si es una letra ponlo en el arreglo
            arreglo.append(caracteres[a])
       
        elif caracteres[a] == "+" :
            pila.append(caracteres[a])

        elif caracteres[a] == "-" :
            pila.append(caracteres[a])

        elif caracteres[a] == "*": 
            pila.append(caracteres[a])

        elif caracteres[a] == "^":
            pila.append(caracteres[a])

        elif caracteres[a] == "/":
            pila.append(caracteres[a])

        elif caracteres[a] == ")":
            arreglo.append(pila.pop())
    listilla = ''.join(arreglo)
    pila = []
    arreglo = []
    print listilla




                      

