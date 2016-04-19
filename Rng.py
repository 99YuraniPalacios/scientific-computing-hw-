# Fecha: 19 de Abril 2016
# Autora: Yurani Melisa Palacios Palacios 

import numpy as np
import matplotlib 
import matplotlib.pyplot as plt 

# Brownian 

# Background 
 
numpy.random.uniform(a, b)
numpy.random.binomial(N, p)
numpy.random.normal(mu, sigma)
numpy.histogram(x, bins=<bins>)


# Problem 1
# Investigate the use of the functions sum and numpy.cumsum


# Problem 2
# Create a function that returns a Brownian random walk in 1 dimension with n steps.
# Assume that every point in the walk the next step follows the distribution N(0.1).
# As before, we will start our walks from x = 0

# brownian(n)
# For the example use n = 200

n = 200 
N = 0.1
x = 0 

def brownian(n):



# Problem 3
# At a given time t (iteration) calculate the distance to the center s. Calculate[s^2]
# for N random walks an plot it as a function of t. Use N = 100


# Problem 4
# The diffusion coefficient D is defined such that ([s^2]=2Dt). 
# Find D for this walk (hint: use the function scipy.stats.linregress) D = 0.61
