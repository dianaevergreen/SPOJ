#!/usr/bin/python

### http://www.spoj.com/problems/NAKANJ/ 


def moves(row, col):
	a_posiciones = []
	movr = [-1, -2, -2, -1, 1, 2, 2, 1]
	movc = [-2, -1, 1, 2, 2, 1, -1, -2]

	for mov in range(len(movr)):
		row_t = row + movr[mov]
		col_t = col + movc[mov]
		if row_t &gt;= 0 and row_t &lt; 8 and col_t &gt;= 0 and col_t &lt; 8:
			a_posiciones.append((row_t, col_t))
	return a_posiciones


 
		
def moving(r1,c1):
	P = [[-1 for x in range(8)] for y in range(8)]
	mark = [[False for x in range(8)] for z in range(8)] 
	
	Q = [[r1,c1,0]]
	
	P[r1][c1] = 0
	mark[r1][c1] = True
	
	while Q:
		current_row, current_col, steps = Q.pop(0)
		a_moves = moves(current_row, current_col)
		
		for i in a_moves:
			c_r, c_c = i
			if mark[c_r][c_c] == False:
				Q.append([c_r,c_c,steps+1])
				P[c_r][c_c] = steps+1
				mark[c_r][c_c] = True

	return P
	

if __name__ == '__main__':
	steps_matrix_all_cells = []	
	for i in range(8):
		steps_matrix_all_cells.append([])
		for j in range(8):
			steps_matrix_all_cells[i].append(moving(i,j))
				
	import sys
	IN = sys.stdin.readlines()
	idx = 0	
	
	cases = int(IN[idx])
	idx+=1

	
	for c in range(cases):
		
		
		pos1,pos2 = IN[idx].split()
		idx+=1

		row1, col1 = pos1
		row2, col2 = pos2

		r1 = ord(row1) - 97
		c1 = int(col1) - 1

		r2 = ord(row2) - 97
		c2 = int(col2) - 1

		print steps_matrix_all_cells[r1][c1][r2][c2]

		
		
