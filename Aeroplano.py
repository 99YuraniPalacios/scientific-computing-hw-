# Jun/15/2016
# Yurani Melisa Palacios Palacios 

import numpy 
import matplotlib.pyplot # as plt
# from matplotlib import pyplot

T = 100
dt = 0.02
N = int (T/dt)+1
t = numpy.linspace(0.0, T, N) # 

z0 = 100 # Altura
b0 = 10 # Velocidad ascendente resultante
zt = 100 # Altura de equilibrio 
g = 9.81 # Gravedad

u = numpy.array([z0, b0]) # Lista 

# Inicializar una matriz para contener los valores de elevacion cambiantes
z = numpy.zeros(N)
z[0] = z0

# Tiempo de ciclo usando el metodo de Euler
for n in range (1, N):
	u = u + dt * numpy.array([u[1], g*(1-u[0]/zt)])
	z[n] = u[0]


matplotlib.pyplot.plot(t,z,'b' )
matplotlib.pyplot.show()

