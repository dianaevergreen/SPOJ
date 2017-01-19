#!/usr/bin/python

elements = input()
lista = []
otralista = []
otramas = []
for i in range(0,elements):
    k = str(raw_input())
    lista.append(k.split())

for f in range(0,len(lista)):
    otramas = lista[f]
    primero = otramas[0][::-1]
    segundo =otramas[1][::-1]
    p = int(primero)
    s = int(segundo)
    suma = p + s
    cadena = str(suma)
    cad = cadena[::-1]
    print int(cad)
    


    