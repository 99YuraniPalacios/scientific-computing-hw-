# Fecha: 3 de Mayo 2016
# Autora: Yurani Melisa Palacios Palacios 

import numpy as np
import matplotlib 
import matplotlib.pyplot as plt 

# PROBLEMS 

#1. Create a square grid of size n xn, n = 100. Use the function numpy.zeros() to do that. note that 
# initially all cells are goingto have the value 0, which we will interpret as having white color 
# w = numpy.zeros([n, n], dtype = numpy.int8)

n = 100
w = np.zeros ([n, n], dtype = np.int8)

Blanco = 0
Negro = 1

Oeste = 0
Sur = 1
Este = 2
Norte = 3

#2. We will make use of the following notation for the directions (0: east), (1: south), (2: west) and 
# (3: north). Design a function that given a direction d and the color c of the cell in which the ant 
# is stading, decides the next direction along which the ant will move.
# def next direction (d, c)

# 0 = Este, 1 = Sur, 2 = Oeste, 3 = Norte 
 
def nextdirection (d, c): 
	if c == Negro :
		if d == Norte:
			d == Este
		if d == Sur:
			d == Oeste
		if d == Este:
			d == Sur
		if d == Oeste:
			d == Norte
		
	else :
		if d == Este:
			d == Norte	
		if d == Oeste:
			d == Sur
		if d == Sur:
			d == Este
		if d == Norte:
			d == Oeste
	return d


#3. Write a function that given a that given a direction of motion d and a position on the grid (i, j), 
# returns the next position to wich the ant will move 
# def moveforward (i, j, d): 

def moveforward (i, j, d):
 
	i1 = 0
	j1 = 0

	if d == Este :
		#k[i, j+1]= 1
		i1, j1 = i, j+1
	if d == Oeste:
		#k[i, j-1]= 1
		i1, j1 = i, j-1
	if d == Norte :
		#k[i-1, j]= 1
		i1,j1 = i1, i-1
	if d == Sur :
		#k[i+1, j]= 1 
		i1,j1 = i+1, j1	
	
	return i1, j1

#4. Desing a function that takes care of the boundary problem. That is, if the next position to which
# the ant will move is not a valid index, the function will return 1 (0, otherwise).
# def validindex (i, j, n):


def validindex (i, j, n):

	if i1 < 0 or j1< 0 or i1 >=n or j1>=n:
		return 1
	else:
		return 0


x = [Este, Oeste, Norte, Sur]
a = np.random.choice(x)

i = n/2
j = n/2

for t in range (20000):
	c = w[i,j]
	newd = nextdirection (a, c)
	a = newd
	i1, j1 = moveforward(i,j,newd)
	validar = validindex(i,j,n)

	if validar == 1:
		break
	else:
		if w[i,j] == 0:
			w[i,j] = 1
		else:
			w[i,j] = 0
		i = i1
		j = j1

#5. Starting with i = n/2, j = n/2 and d= 0, simulate 20000 steps of the ant, or until it leaves the grid 

#6. Plot the final configuration of the grid 
# plt.imshow(w, interpolation='none', cmap= plt.cm.Greys, estent= (0, n, 0, n))

 #plt.imshow(k, interpolation='none', cmap=plt.cm.Greys, extent=(0,n,0,n))
 #plt.show()

plt.imshow(w, interpolation = 'none', cmap = plt.cm.Greys, extent = (0,n,0,n))
plt.show()
