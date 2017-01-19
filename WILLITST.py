#!/usr/bin/python

##Problem code: WILLITST##

n = int(input())

if n == 1:
    print "NIE"

while n &gt; 1:
    if n % 2 != 0:
        print "NIE"
        break
    else:
        n = n / 2
        if(n == 1):
            print "TAK"

    
     
