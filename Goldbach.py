# Jun/08/2016
# Yurani Melisa Palacios Palacios

# Decide si un numero es primo
# El numero debe ser mayor que 0

# f = 1 No primo
# f = 0 Primo

def isprime(u):

	h = 0
	if u == 1:
		f = 1

	else:

		for k in range(2, u):
			if u % k == 0:
				h = 1
				break

		if h == 1:
			f = 1
		else:
			f = 0

	return f

# Decide si un numero puede escribirse como la suma de dos numeros primos

f = 0
N = input('Numero Entero = ')

for k in range(2, N):
	
	
	if isprime(k) == 0 : # Culpa de David 

		j = N - k
		
		if isprime(j) == 0 : # Culpa de David otra vez 
			print  k, j
			f = 1

if f == 1:
	print 'Es posible'
else:
	print 'No es posible'

