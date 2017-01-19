#!/usr/bin/python

number = input()

if number &lt; 10:
    print 1
    print number

elif number &gt;= 10:
    if number % 10 == 0:
        print 2 
        
    else:
        print 1
        print number % 10
          
        
