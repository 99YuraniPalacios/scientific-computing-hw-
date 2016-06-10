# Jun/09/2016
# Yurani Melisa Palacios Palacios

# Problema avanzado
# Disenar un algoritmo para factorizar un numero entero en sus factores primos. 
# (Sugerencia: utilizar el metodo de factorizacion de Euler)

def isprime(u):

	h = 0
	if u == 1:
		f = 0

	else:

		for k in range(2, u):
			if u % k == 0:
				h = 1
				break

		if h == 1:
			f = 0
		else:
			f = 1

	return f

N = input('Numero Entero = ')
num = N
x = 2

while (N !=1):
	if (N % x == 0):
		print (str(x))
		N = N / x
	else:
		x = x + 1
	


