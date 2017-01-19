#!/usr/bin/python

import sys

lines = sys.stdin.readlines()

num = int(lines[0])
cases = []
lista = []
lim = 31623
 
lista = [True for i in range(lim+1)]
primos = [2]
primotes = []

def isprimo(x):
    if x == 1:
        return False
    if x==2: return True
    if x%2==0:
        return False
    if x &lt;= lim:
        global lista
        return lista[x]
    global primos
    for p in primos:
        if x % p == 0:
            return False
        
        if p*p &gt; x:
            break
    return True        

    
for a in range(3,lim+1,2):
    if(lista[a]):
        primos.append(a)
        for b in range(2*a,lim+1,a):
            lista[b] = False
             


counter = 0
for i in lines[1:]:
    if(counter &gt; 0):
        print ""
    counter += 1

    [n,m] = [int(x) for x in i.split()]
#    for g in range(n,m+1):
#        if isprimo(g):
#            print g
    print "\n".join([str(g) for g in range(n,m+1) if isprimo(g)])
 
