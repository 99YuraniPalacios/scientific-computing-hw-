# Jun/08/2016
# Yurani Melisa Palacios Palacios 

# Decide si un numero es primo
# El numero debe ser mayor que 0

h = 0

N = input('Numero Entero = ')

if N == 1:
	print 'No es primo'

else:

	for k in range(2, N):
		if N % k == 0:
			h = 1
			break

	if h == 1:
		print 'No es primo'
	else:
		print 'Es primo'
