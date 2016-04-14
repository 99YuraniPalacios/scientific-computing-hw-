# Fecha: 12 de Abril de 2016
# Autora: Yurani Melisa Palacios Palacios 

import numpy as np
import matplotlib 
import matplotlib.pyplot as plt 


# Background 

# In this ssesion we will complete our study of the 1D random walk and move on to applications in higher
# dimensions. In particular we will prepare our way to study the properties of Brownian motion 2D 

# Problems 

# 1. Modify the function "rwalk1d" that you created last session, to account for the fact that the used 
#    coin is biased 
# def rwalk1d(N, p) 

def rwalk1d (N, p):
	
	n = 0
	for i in range (N):
		r = np.random.random()
		if r < p:
			n = n + 1
		else :
			n = n - 1
	return n
		
# 2. Run n random walks in one dimension and calculate the quantities ...
#    use n= 100, N= 1000 and q= 0.5, 0.7, 0.2, what do you observe?

n = 100
N = 1000
p= (0.5, 0.7, 0.2)

suma = 0 

for i in range ():
	x[i] = rwalk1d (N, p)
		suma = suma + x[i]

Prom = suma/ float(N)
print Prom 

suma* = 0
for j in range ():
	resta [j] = (x[j] - prom) **2
	suma* = suma* 












# 3. Create an array h of n entries where the ith position is the number of times that the "drunk" i the 
#    1D random walk ends up i meters away from the center (Warning: the final position of the walker can be 
#    negative, whereas the position in the array cannot be smaller than 0.)


# 4. Plot h as a function of i. ¡¡ Explain !!
