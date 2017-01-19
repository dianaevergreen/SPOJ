#!/usr/bin/python

import sys

lines = sys.stdin.readlines()

cases = lines[0]

for a in lines[1:]:
    if a.strip():
        cad = a.split()

        if "machula" in cad[0]:
            scnd = int(cad[2])
            thrd = int(cad[4])
            frst = thrd - scnd

        if "machula" in cad[2]:
            frst = int(cad[0])
            thrd = int(cad[4])
            scnd = thrd - frst

        if "machula" in cad[4]:
            frst = int(cad[0])
            scnd = int(cad[2])
            thrd = scnd + frst

        print frst, "+", scnd, "=", thrd