# Jun/09/2016
# Yurani Melisa Palacios Palacios

# La conjetura de Legendre: Para todo entero positivo n no es un numero primo entre n ** 2 y (n + 1)**2

# Escribir una funcion que dado un numero entero positivo decide si la conjetura de Legendre es cierto. 
# Debe devolver 1 si la conjetura es cierta y 0 en otro caso

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


N = input ('Numero Entero = ') 
P = N**2
R = (N + 1)**2

def Legendre(i):

	for i in range (P, R+1):
	
		if isprime(i)==1:

			return 1

		else:
			return 0

g = Legendre(N)
print g





