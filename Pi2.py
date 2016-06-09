# Jun/09/2016
# Yurani Melisa Palacios 

# Calculates the value of pi using random numbers

import numpy as np

Ntot = 1000000
ncirc = 0

np.random.seed(10)
for i in range(Ntot):
	
	x = np.random.uniform(0, 1)
	y = np.random.uniform(0, 1)

	if np.sqrt((x - 0.5)**2 + (y - 0.5)**2) < 0.5:
		ncirc += 1

pi = (ncirc / float(Ntot)) / (0.5)**2

print pi, np.pi
