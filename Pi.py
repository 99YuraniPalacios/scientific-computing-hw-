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
	plt.plot(x,y)
	plt.show()

fpi (3, 1, 10000)
	







