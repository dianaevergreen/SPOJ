#!/usr/bin/python
import sys

lines = sys.stdin.readlines()
array1 = []
array2 = []
arrayfinal = []
lineas = []
l = []
arreglete = []

c = 0

while c &lt; len(lines):
    
    if lines[c].strip() != "0" and len(lines) &gt; 1:
        num = int(lines[c])
        c += 1
        l = lines[c]
        lineas = list(l)
        

        m = len(lineas)
        p = 0
        boolie = True

        while p &lt; m-1:
            if(boolie):
                for b in range(num):
                    array1.append(lineas.pop(0))
                    
                    
                boolie = False
                p += num

            else:
                for d in range(num):
                    array2.append(lineas.pop(0))
                    
                
                array2.reverse()
                
                boolie = True
                p += num
            arrayfinal.extend(array1)
            arrayfinal.extend(array2)
            array1 = []
            array2 = []
                
        c += 1
        
        
        
        qq = 0
        vv = 0
        qtip = len(arrayfinal)/num    #largo
        
        while(qq &lt; num):
            while(vv &lt; qtip):
                arreglete.append(arrayfinal[vv*num + qq])   
                
                
                vv += 1    
            qq += 1
            vv = 0
            

        aa=''.join(arreglete)
        print aa
        arreglete = []
        arrayfinal = []
    else:
        sys.exit()
        