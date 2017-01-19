#!/usr/bin/python

cases = input()

for a in range(cases):
    a_needed = raw_input()
    a_stamps = raw_input()
        
    need = [int(n) for n in a_needed.split()]

    array = [int(c) for c in a_stamps.split()]
    array.sort()
    array.reverse()
    acumulator = 0
    counter = 0

    if(sum(array) &lt; need[0]):
        lst = ["Scenario #", str(a+1), ":"]
        print "".join(lst)
        print "impossible\n"
    else:
        for b in array:
            if(need[0] &gt; acumulator):
                acumulator += b 
                counter += 1
        lst = ["Scenario #", str(a+1), ":"]
        print "".join(lst)
        print counter, "\n"
    