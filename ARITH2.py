#!/usr/bin/python

## 4452. Simple Arithmetics II  Problem code: ARITH2

cases = int(input())

for a in range(cases):
    blank = raw_input()
    data = [str(x) for x in raw_input().split()]

    numeros = []
    signos = []
    
    for e in range(len(data)):
        if e % 2 == 0:
            numeros.append(int(data[e]))
        else:
            signos.append(data[e])
    res = numeros[0]
    for i in range(0,len(numeros)-1):
        if signos[i] == '+':
            res = res + numeros[i+1]
        elif signos[i] == '-':
            res = res - numeros[i+1]
        elif signos[i] == '/':
            res = res / numeros[i+1]
        elif signos[i] == '*':
            res = res * numeros[i+1]

    print res

    
