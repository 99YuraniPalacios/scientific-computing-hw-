# Jun/10/2016
import numpy as np

# function designed to calculate areas using monter-carlo
# integration

def function(x):
	y = 1 / np.log(x)
	return y

Ntot = 10000000
a = 2
b = 100
h = 1.6

c = 0
for i in range(Ntot):

	x = np.random.uniform(a, b)
	y = np.random.uniform(0, h)

	if y < function(x):
		c += 1

A = (c / float(Ntot)) * (b - a) * h
print A
