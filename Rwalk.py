# Fecha: 7 de Abril 2016
# Autora: Yurani Melisa Palacios 

# Create a funtion=> def rwalk1d(N):

# That returns the final positions of a random walker after N iterations. After each position, the new step 
# is chosen using a fair-coin 


import numpy as np
import matplotlib 
import matplotlib.pyplot as plt 

def rwalk1d (N, P):
	
	n = 0
	for i in range (N):
		r = np.random.random()
		if r < p:
			n = n + 1
		else :
			n = n - 1
	return n
		

