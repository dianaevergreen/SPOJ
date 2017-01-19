#!/usr/bin/python

def division(n):
   
    piv = 1    
    counter = 1
    
    if n == 1:
        return 'Y'
    elif n &lt; piv:
        return 'N'
    else:
        while piv &lt; n:
            piv = counter*6 + piv
            counter +=1
            if piv == n:
                return 'Y'
        return 'N'



def main():
    n = int(input())

    while n != -1 :
    
        res = division(n)
        print res


        n = int(input())


if __name__ == '__main__':
    main()
