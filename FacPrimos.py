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

#N = input('Numero Entero = ')
#num = N
#x = 2

#while (N !=1):
#	if (N % x == 0):
#		print (str(x))
#		N = N / x
#	else:
# 		x = x + 1
	

n = input('Numero Entero: ') # Se pide por pantalla que se ingrese el numeo entero.

def factor(n): #funcion que permite hallar y retornar los factores primos
	l = [] #almacenamos los resultados de la factorizacion en una lista
	llena = n #Se crea un acumulador

	for i in range(n): #mientras podamos dividir por 2 el dos es un factor, asi que se agrega a la lista.
		if llena % 2 == 0:
			l.append(2)
			llena /= 2
	impar =  3
	for j in range(n):  #ahora probamos con los impares, empezando por el 3
		if llena % impar == 0:
			l.append(impar)
			llena /= impar
		else:
			impar += 2
	return l

print factor(n)


