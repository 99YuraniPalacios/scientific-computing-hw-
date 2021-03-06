# Fecha: 19 de Abril 2016
# Autora: Yurani Melisa Palacios Palacios 

import numpy as np
import matplotlib 
import matplotlib.pyplot as plt 

# Brownian 

# Background 
 
# numpy.random.uniform(a, b)
# numpy.random.binomial(N, p)
# numpy.random.normal(mu, sigma)
# numpy.histogram(x, bins=<bins>)


# Problem 1
# Investigate the use of the functions sum and numpy.cumsum


# Problem 2
# Create a function that returns a Brownian random walk in 1 dimension with n steps.
# Assume that every point in the walk the next step follows the distribution N(0.1).
# As before, we will start our walks from x = 0

# brownian(n)
# For the example use n = 200

np.random.seed (0)
n = 200 
N = 0.1
x = 0 

def brownian(n):

	walk = np.random.normal (0.1, 200)
	x = np.append (0, np.cumsum (walk))
	x [0] = 0

	return x

x = brownian (200)

plt.plot (x)
plt.show()

# Problem 3
# At a given time t (iteration) calculate the distance to the center s. Calculate[s^2]
# for N random walks an plot it as a function of t. Use N = 100

N = 100
n = 200

y = np.zeros (n + 1)

for i in range(N):
	x  = brownian(n)
	y = y + x**2

y /= float (N)
t = range (n + 1)


plt.plot (t, y, 'r-')
plt.show()

# Problem 4
# The diffusion coefficient D is defined such that ([s^2]=2Dt). 
# Find D for this walk (hint: use the function scipy.stats.linregress) D = 0.61

slope, intercept, r_value, p_value, std_err = scipy.stats.linregress (t, s2) 
print 'Diffusion Coefficient D=', 0.5 * slope
