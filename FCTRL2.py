#!/usr/bin/python
import sys

n = sys.stdin.readlines()
lista = []


def factorial(x):
    if (x &lt;= 1):
        return 1
    else:
        return factorial(x-1) * x



cant = int(n[0])

if len(n) != cant+1:
    while True:
        pass

for line in n[1:]:
    l =int(line)
    f = factorial(l)
    lista.append(f)


print "\n".join(str(d) for d in lista)