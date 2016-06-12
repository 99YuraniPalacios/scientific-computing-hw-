# Jun/10/2016
# Yurani Melisa Palacios Palacios 

import numpy as np
import mpmath
import scipy.integrate as integrate


def f(x):
	return 1 / np.log(x)

a = 2.0
b = 10.0
N = 1000

d = (b - a) / N
A = 0
for k in range(N):
	
	a1 = a + k * d
	b1 = a1 + d

	A += (b1 - a1) * (f(a1) + f(b1)) / 2.
	
print 'we calculated = ', A
print 'mpmath calculated = ', mpmath.li(b, offset = True)
print 'scipy calculated = ', integrate.quad(f, 2, 10)
