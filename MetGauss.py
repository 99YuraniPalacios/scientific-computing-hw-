# Jun/12/2016
# Yurani Melisa Palacios Palacios 

# Advance Problem 
# Design al algorithm to implement the method of Gaussian quadrature. Use to create a function that calculates Li(x) 
# Diseno al algoritmo para implementar el metodo del cuadratura de Gauss. Se utiliza para crear una funcion que calcula Li(x)

import math as mt

a = 0
b = 2

w1 = 0.555555555
w2 = 0.888888888
w3 = 0.555555555

z1 = 0.774593669
z2 = 0.0
z3 = 0.774593669

Delta_x = (b - a)/2

def evaluar(n):

	if n ==1:
		g = ((b-a/2 * z1) + (b+a/2))

	if n ==2:
		g  = ((b-a/2 * z1) + (b+a/2))

	if n ==3:
		g  = ((b-a/2 * z1) + (b+a/2))

	return g

	
m = evaluar(1)
n = evaluar(2)
l = evaluar(3)

def f(p):
	q = mt.sin(mt.e**p)

	return q

m1 = f(m)
n1 = f(n)
l1 = f(l)

Sf = Delta_x * ((w1 * m1)+(w2 * n1)+(w3*l1)) 

print 'El area aproximada es',Sf







