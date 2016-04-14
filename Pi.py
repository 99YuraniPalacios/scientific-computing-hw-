# Fecha: 5 de Abril de 2016
# Autora: Yurani Melisa Palacios

# A random walk is the process in which an objects wander away from its starting position, by taking random 
# directions in every step. A simple example is in one dimension (1D). Imagine a point initially placed at 
# the origin, it can move either to the left or to he righ, the actual decision is random -e.g. based on a 
# the result of tossing a coin-

import numpy as np
import matplotlib 
import matplotlib.pyplot as plt 

# Problem 1
# Firs we will get familiar with the use of random numbers. Evaluate the statement " print numpy.random.random()"
# a few times and explain the result 

print np.random.random()


# Problem 2 
# Now execute 

np.random.seed(0)
print np.random.random()

# Problem 3 
# As an example we will evalute the value of phi. Remember that the are of a circle of radius R if phiR**2. Let
# us ussume that R=1 and choose a box og length L=3
# Now imagine you throw N darts that randomly hit the square. It is easy to realize that if n is the number of 
# darts that fall inside the circle, then ... 
# from which we can get the value of pi. Create a funtion that finds the value of pi using this method. Use 
# N= 100.1000.10000
R= 1
L= 3
N= 10000

def fpi (L,R,N):
	x= np.linspace(0,1, num= N, endpoint= 'true')
	y= np.zeros(len(x))
	n= 0
	for i in range (len(x)):
		x[i]= L/2 - np.random.random()* 3
		y[i]= np.random.uniform(-1.5, 1.5)
		
		if (np.sqrt(x[i]**2 + y[i]**2))<=R:
			n= n+1
	
	pi=((L/R)**2)*((n/float(N)))	
	print  pi
	
fpi (3, 1, 10000)
	


#MODULO RANDOM EN PYTHON
#######################################################################ut
#Modulo Random #
#El modulo random proporciona un generador de numeros aleatorios. #
#######################################################################
# RANDRANGE #
# El numero aleatorio que nos devuelve tiene que estar dentro #
# de un rango ingresado por nosotros. #
# random.randrange([start,] stop [,step]) #
# print random.randrange(10) #Numero aleatorio entre 0 y 9 #
# print random.randrange(1, 12, 2) #Pueden ser (1, 3, 5, 7, 9, 11) #
#######################################################################
# RANDINT #
# A diferencia de randrange, randint incluye al stop dentro del rango #
# random.randint(a, b) #
# print random.randint(0,5)#La salida va a ser: 0, 1, 2, 3, 4 o 5 #
#######################################################################
# CHOICE(secuencia) #
# #Devuelve un elemento aleatorio de una secuencia no vacia. #
# random.choice(["rojo", "negro", "verde"]) #
# lista = [2, 190, False, "hola", "pelota", 123] #
# random.choice(lista) #
#######################################################################
# RANDOM #
# Devuelve un numero aleatorio de punto flotante entre 0.0 y 1.0 #
# random.random() #
# random.random() * 100 #Nos devuelve un numero de punto flotante #
# entre 0.0 y 100.0 #
#######################################################################
# UNIFORM #
# Devuelve un numero de punto flotante entre a y b: #
# random.uniform(a, b) #
# #random.uniform(1, 2) #Devuelve un numero aleatorio entre 1.0 y 2.0 #
#######################################################################
# SHUFFLE #
# La funcion shuffle mezcla aleatoriamente el orden de los elementos. #
#random.shuffle(a) #
# a = [1, 2, 3, 4, 5] #
# random.shuffle(a) #
# print a #
# [3, 2, 4, 5, 1] #
#######################################################################





