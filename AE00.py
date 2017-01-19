#!/usr/bin/python
number = input()

counter = number
c = 1
for a in range(2,int(number**0.5)+1):
    counter = counter + number/a - c
    c += 1

print counter