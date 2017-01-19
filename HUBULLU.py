#!/usr/bin/python

cases = int(input())
winner = []

for c in range(cases):
    winner = raw_input().split()
    if winner[1] == '0':
        print "Airborne wins."
    else:
        print "Pagfloyd wins."
