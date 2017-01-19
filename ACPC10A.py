#!/usr/bin/python

import sys

lines = sys.stdin.readlines()

for n in lines:
    a = [float(c) for c in n.split()]


    first = a[1] - a[0]
    scnd = a[2] - a[1]

    if first == scnd:
        print "AP", int(a[2] + scnd)

    first = a[1] / a[0]
    scnd = a[2] / a[1]

    if first == scnd:
        print "GP", int(a[2] * scnd)