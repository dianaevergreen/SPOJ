#!/usr/bin/python

num = input()
array1 = []
array2 = []
totalarray = []
array = []

for i in range(num):
    p = input()
    array1 = [int(x) for x in raw_input().split()]
    array2 = [int(x) for x in raw_input().split()]
    array1.sort()
    array2.sort()   
    
    for a in range(p):
        totalarray.append(array1[a]* array2[a])
        
    x = 0
    for b in totalarray:
        x = x + b
       

    print x
    totalarray = []
     