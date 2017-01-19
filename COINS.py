#!/usr/bin/python

### http://www.spoj.com/problems/COINS/

coins = [0]*(1000000+1)

def millon():
	for a in range(1000000+1):
		if a &lt;= 11:
			coins[a] = a
		else:
			coins[a] = coins[a/2] + coins[a/3] + coins[a/4]
	

def change(m):

	if m &lt;= 1000000:
		return coins[m]
	
	return change(m/2) + change(m/3) + change(m/4)





if __name__ == '__main__':
	millon()
	while True:
		try:
			n = input()
			m = int(n)
			if m &lt;= 11:
				print m
			else:
				print change(m)
		except:
			break
