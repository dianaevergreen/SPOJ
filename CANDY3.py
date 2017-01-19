#!/usr/bin/python

cases = int(input())

for a in range(cases):
    nada = raw_input()
    children = int(input())

    suma = 0
    for i in range(children):
        suma = suma + int(input())
        
    if suma % children == 0:
        print "YES"
    else:
        print "NO"

