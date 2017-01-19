#!/usr/bin/python

##394. Alphacode, Problem code: ACODE


def main():
    n = int(input())

    while(n != 0):
        array_num= []
        array_num= [int(x) for x in str(n)]
        
        array_res = [0]*(len(array_num) + 1)
        if array_num[-1] != 0 :
            array_res[len(array_num)] = 1
            array_res[len(array_num)-1] = 1
        else:
            array_res[len(array_num)] = 1
            array_res[len(array_num)-1] = 0
        
        for i in range(len(array_num)-2,-1,-1):
            if array_num[i] == 0:
                continue

            if int(str(array_num[i])+str(array_num[i+1])) &lt;= 26:
                array_res[i] = array_res[i+1] + array_res[i+2]
            else:
                array_res[i] = array_res[i+1] + 0
        print array_res[0]
        n = int(input())

        
      
    

if __name__ == '__main__':
    main()

