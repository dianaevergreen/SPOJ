#!/usr/bin/python

cases= input()

def sortear(array, f):
    array.reverse()
    array.append(f)
    if array == [0]*len(array):
        return "0"
    else:
        array_strings = [str(d) for d in array]
        cadena = ''.join(array_strings)
        return cadena



def resto1(array1, f1):
    pos1 = []
    for g in array1:
        if g%3 == 1:
            array1.remove(g)
            return sortear(array1, f1)
    for g in array1:
        if g%3 == 2:
             pos1.append(g)
    if len(pos1) &gt;= 2:
            array1.remove(pos1[0])
            array1.remove(pos1[1])
            return sortear(array1, f1)
    else:
        return "impossible"   
            
       
            

def resto2(array2, f2):
    pos2 = []
    for h in array2:
        if h%3 == 2:
            array2.remove(h)
            return sortear(array2, f2)

    for h in array2:
        if h%3 == 1:
            pos2.append(h)
    if len(pos2) &gt;= 2:
        array2.remove(pos2[0])
        array2.remove(pos2[1])
        return sortear(array2, f2)
    else:
        return "impossible"
            



for a in range(cases):
    strings = raw_input()
   
    numeros = [int(b) for b in strings.strip()]
    numeros.sort()

    if numeros == [0]: 
        print "0"   
        continue

    suma = 0
    for c in numeros:
        suma += c


    resto = suma % 3

        

    if 0 in numeros:
        fin  = 0
        numeros.remove(0)
    elif 5 in numeros:
        fin = 5
        numeros.remove(5)
    else:
        print "impossible"
        continue

    
    if resto == 0 and len(numeros) &gt; 0:
        print sortear(numeros, fin)
        

    else:
        if resto == 1 and len(numeros) &gt; 0:
            print resto1(numeros, fin)
        elif resto == 2 and len(numeros) &gt; 0:
            print resto2(numeros, fin)
        else:
            print "impossible"
