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

# Cuenta el numero de primos por debajo de un numero dado

def countprimes(v):

	i = 0

	for j in range(1, v + 1):
		
		if isprime(j) == 0 : 
			i = 1 + i

	return i


k = countprimes(0)
print k
