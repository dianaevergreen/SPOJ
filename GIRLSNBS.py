#!/usr/bin/python

def intercalar(g, b):
    if g &gt; b:
        maxi = g
        mini = b
    else:
        mini = g
        maxi = b

    resto = maxi % (mini+1)
    resultado = maxi / (mini+1)

    if resto == 0:
        return resultado
    else:
        
        return resultado +1
        


def main():

    n = [int(x) for x in raw_input().split()]

    while n[0] != -1 and n[1] != -1:
        g = n[0]
        b = n[1]    

        res = intercalar(g, b)
        print res

        n = [int(x) for x in raw_input().split()]


if __name__ ==  '__main__':
    main()
    


