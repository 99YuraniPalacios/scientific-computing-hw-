# Jun/09/2016
# Yurani Melisa Palacios Palacios 

# La conjetura de Warin: cada numero entero impar exceding 3 es cither un numero primo o la suma de tres numeros primos

# Escribir una funcion que dado un numero entero positivo mayor que 3 decide si la conjetura de Waring es cierto.
# Debe devolver el numero si es primo, los tres primeros numeros enteros que sumen el numero 0 o si la conjetura es falsa


# The number has to be larger than 0
# f = 0 No primo 
# f = 1 Primo

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

# Program designed to test Waring's conjecture

n = input ('Numero = ')

def waring(n):

	if isprime(n) == 1:

		return n
	
	else:
		for p in range(2, n):

			if isprime(p) == 1:
			
				k = n - p

				for q in range(2, k):

					if isprime(q) == 1:

						r = k - q

						if isprime(r) == 1:
						
							return p, q, r

	return 0

g = waring(n)
print g






