#!/usr/bin/python
### Prime Path  http://www.spoj.com/problems/PPATH/


def primes():
	top = 9999
	array_primes = [2,3]
	g = 5
	
	while g &lt;= top:
		flag = True
		raiz = g**0.5
		for i in array_primes:
			if i &lt;= raiz:
				if g%i == 0:
					flag = False

			else:
				break

		if flag == True:
			array_primes.append(g)

		g += 2

	return array_primes	


#def vecinos(numero, lista):
		
'''	for pos in range(4):
		for dig in range(10):
			if pos == 0 and dig == 0:
				continue
				
			if dig != int(numero[pos]):
				posible = int(numero[:pos] + str(dig) + numero[pos+1:])
				if posible in lista:
					print numero, posible

'''	
			
#Improved
def vecinos(numero, lista):
	sol = []
	num = [int(x) for x in str(numero)]
	for pos in range(4):
		for dig in range(10):
			if pos == 0 and dig == 0:
				continue
			if dig == num[pos]:
				continue
			copia = num[:]
			copia[pos] = dig
			
			possible = 1000*copia[0] + 100*copia[1] + 10*copia[2] + copia[3]
			if possible in lista:
				sol.append(possible)
	return sol
			
def BFS(mapa,n,m):
	Q = [[n,0]]
	mark = [False]*10000
	mark[n] = True

	if n == m:
		return 0

	while Q:
		current, step = Q[0]
		Q.pop(0)

		neighbors = mapa[current]	
		for i in range(len(neighbors)):
			if neighbors[i] == m:
				return step+1

			if mark[neighbors[i]] == False:
				Q.append([neighbors[i], step+ 1])
				mark[neighbors[i]] = True

	return "Impossible"

			
	
if __name__ == '__main__':
	cases = int(input())

	primos = primes()
	
	index_1st = primos.index(1009)
	p= primos[index_1st:]
	
	mapa = {}
	for cousins in p:
		mapa[cousins] = vecinos(cousins,p)


	for c in range(cases):
		n,m = [int(x) for x in raw_input().split()]

		print BFS(mapa,n,m)
			
		


