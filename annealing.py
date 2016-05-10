# Fecha : 26 de Abril 2016 
# Autora: Yurani Melisa Palacios Palacios 

import numpy as np
import matplotlib 
import matplotlib.pyplot as plt 

# Problems 

# 1. Created a funcion called cost that returns the cost for a given solution. In this cae,
# the cost is given by Eq.(2)
# cost (solution)

def cost(solution):
	Eq2 = np.exp(-(solution -1) **2) * np.sin(8 * solution) + 1

	return Eq2 
 
# 2. Make a plot of the cost for solutions in the range -3 o 3, and identify a range for the
# optimal value.

x= np.linspace(-3, 3, num= 100, endpoint= 'true')
y= range (len(x))

for i in range (len(x)):
	y[i] = cost (x[i]) 

plt.plot (x, y)
plt.show()

# 3. Create a function that returns the a new solution given a possible one
# def neighbor (solution):
#	step_size = 1.0
#	return (2 * np.random.random() - 1) * step_size + solution 

def neighbor (solution):
	step_size = 1.0
	
	return (2 * np.random.random() - 1) * step_size + solution 

# 4. Start with a randomly selected solution in the range found in step 2. FixT = 1 and Tmin = 10^-5

c = np.random.uniform (0, 2)
T = 1
Tmin = (1 ** -5)
c2 = cost (c)

# 5. Generate a new solution with the function neighbor

# for j in range (100):
# 	c2 = neighbor(c)

# 6. Decide which of the two solutions is the best one based on what we discussed earlier (See Eq. 1)

# for k in range (100):
#	Eq1 = ((c - c2) / T)

# 7. Repeat steps 5 & 6 100 times

# 8. Decrease T by a factor of 0.9, and repeat steps 5-7 until the temperature drops below Tmin 
while T > Tmin :
	for j in range (100):
		c2 = neighbor(c)

		u = random.uniform()
		Eq1 = ((c - c2) / T)

		if cost(c2)<cost(c):
			c = c2
		else :
			if Eq1 > u:
				c = Eq1		
	T = fT * T
print "Optimal solution :%f" % (c)
print "Cost of optimal solution: %f" % (c2)
