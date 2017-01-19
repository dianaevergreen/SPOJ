#!/usr/bin/python

### 1724. Counting Triangles Problem code: TRICOUNT ##

cases =  int(input())
    

for a in range(cases):
    n = int(input())

    if n % 2 == 0:
        res = (n*(n+2)*(2*n+1))/8
        print res
    else:
        res = (n*(n+2)*(2*n+1)-1)/8
        print res
