#!/usr/bin/python

## http://www.spoj.com/problems/INVCNT/

## Inversion Count



def mergesort(numbers):

	if len(numbers) == 1:
		return numbers, 0
	else:

		l = len(numbers) / 2

		left, invr = mergesort(numbers[:l])
		right, invl = mergesort(numbers[l:])
		sol = []
		inv = 0
		r_index = 0
		l_index = 0
		while r_index &lt; len(right) and l_index &lt; len(left):
			if right[r_index] &lt; left[l_index]:
				sol.append(right[r_index])
				r_index += 1
				inv += len(left) - l_index
				
			else:
				sol.append(left[l_index])
				l_index += 1
		#if r_index &lt; len(right):
			#sol.extend(right[r_index:])
		while r_index &lt; len(right):
			sol.append(right[r_index])
			r_index += 1
			
		#if l_index &lt; len(left):
			#sol.extend(left[l_index:])
		while l_index &lt; len(left):
			sol.append(left[l_index])
			l_index += 1

		return sol, inv + invl + invr

		


if __name__ == '__main__':
	import sys
	INP = sys.stdin.readlines()
	idx = 0
	cases = int(INP[idx])
	idx += 1
	#blank = raw_input()
	idx += 1

	for c in range(cases):
		numbers = []
		no = int(INP[idx])
		idx += 1
		for n in range(no):
			numbers.append(int(INP[idx]))
			idx += 1
		#blank = raw_input()
		idx += 1
		print mergesort(numbers)[1]



