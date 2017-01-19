#!/usr/bin/python

##Spoj.com, Problem code: NY10A, 8612. Penney Game



def counter(seq):
    sequences = ('TTT', 'TTH', 'THT', 'THH', 'HTT', 'HTH', 'HHT','HHH'  )
    count_array  = [0]*8

    for i in range(38):
        for j in range(len(sequences)):
            if sequences[j] in seq[i:i+3]:
                count_array[j] += 1

    return count_array
    


def main():
    cases = input()
    ap = []
    for c in range(cases):
        n = input()
        seq = raw_input()
        ap = counter(seq)
        
        print str(c+1)+" " + ' '.join(str(a) for a in ap)
    

if __name__ == '__main__':
    main()
