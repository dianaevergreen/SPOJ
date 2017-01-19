#!/usr/bin/python

## SPOJ Code: STPAR ##

def parade(mobiles):
	cant = len(mobiles)
	queue = []
	stack = []	

	counter = 1

	for a in range(cant):
		if mobiles[a] != counter:
			stack.insert(0,mobiles[a])
#			print queue, stack
		else:
			queue.append(mobiles[a])
			counter += 1
		#	print queue, stack			
			while len(stack) &gt; 0 and stack[0] == counter:
				queue.append(stack.pop(0))
				counter += 1
#				print queue, stack
#	print queue, stack
	return queue + stack

if __name__ == '__main__':
	cases = int(input())
	while cases != 0:
		mobiles_order = []
		mobiles_order = [int(x) for x in raw_input().split()]
		r =parade(mobiles_order)
		mobiles_order.sort()
		if r == mobiles_order:
			print "yes"
		else:
			print "no"
		cases = int(input())
		
