#!/usr/bin/python

## http://www.spoj.com/problems/BITMAP/ ##

def bitmap(mtx,n,m):
	Q = []
	for a in range(n):
		for b in range(m):
			if mtx[a][b] == 1:
				Q.append([a,b])

	movR = [1,-1,0,0]
	movC = [0,0,1,-1]

	while Q:
		i,j = Q[0]
		Q.pop(0)

		for mov in range(4):
			it = movR[mov] + i
			jt = movC[mov] + j
			if it &gt;= 0 and it &lt; n and jt &gt;= 0 and jt &lt; m:
				if mtx[it][jt] == 0:
					mtx[it][jt] = mtx[i][j] + 1
					Q.append([it,jt])
	
	for a in range(n):
		for b in range(m):
			mtx[a][b] += -1

	return mtx



if __name__ == '__main__':
	cases = int(input())
	for c in range(cases):
		if c!=0:
			raw_input()
		n, m = [int(x) for x in raw_input().split()]
		matrix =[]
		for a in range(n):
			matrix.append([int(x) for x in list(raw_input())])
		matrix_sol = bitmap(matrix,n,m)

		for a in range(n):
			for b in range(m):
				print matrix_sol[a][b],
			print 
	