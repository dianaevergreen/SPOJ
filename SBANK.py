#!/usr/bin/python

def bank(cuentas):

	solucion = []
	repeticion = []
	
	cuentas.sort()
	cuentas.append(None)	

	i = 0
	j = 1

	
	while j &lt; len(cuentas) and i &lt; len(cuentas) :
		counter = 1
		if cuentas[i] != cuentas[j]:
			solucion.append(cuentas[i])
			repeticion.append(1)
			i = j
			j += 1
		else:
			solucion.append(cuentas[i])
			while j &lt; len(cuentas) and cuentas[i] == cuentas[j]:
				counter += 1
				j += 1
			i = j
			j += 1
			repeticion.append(counter)
	return solucion, repeticion	

if __name__ == '__main__':
	cases = int(input())

	for a in range(cases):
		no_cuentas = []
		cant_cuentas = int(input())
		for b in range(cant_cuentas):
			no_cuentas.append(raw_input())
		if a != cases - 1:
			white_space = raw_input()
		sol, rep = bank(no_cuentas)	
		
		for c in range(len(sol)):
			print sol[c], rep[c]

		if a != cases - 1:
			print ""
				