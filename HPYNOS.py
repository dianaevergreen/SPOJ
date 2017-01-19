#!/usr/bin/python

## 7733. Happy Numbers I, Problem code: HPYNOS



def happy_number(num):
    resultado, counter = 0, 0
    while int(num) != 4:
        for n in num:
            resultado += int(n)**2  
             
        counter += 1

        if resultado == 1:
            return counter
        else:
            num = str(resultado)
            resultado = 0

    return -1
        


def main():
    
    number = str(input())
    print happy_number(number)
    


if __name__ == '__main__':
    main()


