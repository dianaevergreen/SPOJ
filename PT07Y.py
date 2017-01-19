# your code goes here
#!/usr/bin/python

## http://www.spoj.com/problems/PT07Y/

def Isit(a,nodes,n,m):

	sol = []
	for i in range(len(a)):
		if nodes[a[i][0]] == False or nodes[a[i][1]] == False:
			nodes[a[i][0]] = True
			nodes[a[i][1]] = True
		else:
			return "NO"
	return "YES"
			 
		

if __name__ == '__main__':
	n, m = [int(x) for x in raw_input().split()]
	nodes = [False]*(n+1)

	if n == m + 1:
		
		a = []
		for mm in range(m):
			a.append([int(x) for x in raw_input().split()])
		
		print Isit(a,nodes,n,m)
			
	else:
		
		a = []
		for mm in range(m):
			a.append([int(x) for x in raw_input().split()])
		
		print "NO"
		