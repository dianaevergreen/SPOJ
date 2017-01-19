#!/usr/bin/python



def main():
    cases = int(input())

    for i in range(cases):
        (a,b,c,d) = [float(x) for x in raw_input().split()]
    

        s = (a + b + c + d)/2
        answ = ((s-a)*(s-b)*(s-c)*(s-d))**0.5
        print answ



if __name__ == '__main__':
    main()
    

