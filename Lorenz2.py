# Jun/13/2016
# Yurani Melisa Palacios Palacios 

# Atractor de Lorenz modificado 

import numpy as np
import matplotlib.pyplot as plt


def f(t, x, y, z):

	sigma = 10.
	rho = 28.
	beta = 2.667	

	dx_dt = sigma * (y - x)
	dy_dt = x * (rho - z) - y
	dz_dt = x * y - beta * z

	return dx_dt, dy_dt, dz_dt

def lorenz(x0, y0, z0, delta, tmax):

	Nmax = int(tmax / delta) + 1

	t = range(Nmax)
	x = range(Nmax)
	y = range(Nmax)
	z = range(Nmax)

	x[0] = x0
	y[0] = y0
	z[0] = z0
	t0 = 0

	for n in range(1, Nmax):

		dx_dt, dy_dt, dz_dt = f(t0, x0, y0, z0)
	
		x1 = x0 + (dx_dt) * delta
		y1 = y0 + (dy_dt) * delta
		z1 = z0 + (dz_dt) * delta
		t1 = t0 + delta
	

		x0 = x1
		y0 = y1	
		z0 = z1	
		t0 = t1

		x[n] = x0
		y[n] = y0
		z[n] = z0	
		t[n] = t0

	return t, x, y, z

delta = 0.0001
tmax = 100

t0, x0, y0, z0 = lorenz(0.2, 1.0, 1.05, delta, tmax)
t1, x1, y1, z1 = lorenz(0.0, 1.0, 1.05, delta, tmax)

plt.plot(x0, z0, 'r')
#plt.plot(t1, z1, 'k')

plt.show()
