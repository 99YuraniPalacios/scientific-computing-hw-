# Jun/15/2016
# Yurani Melisa Palacios Palacios 

import numpy as np
# import matplotlib.pyplot as plt 
from matplotlib import pyplot
from math import sin, cos, log 


g = 9.8 # Gravedad 
v_t = 30.0 # Velocidad de ajuste 
C_D = 0.025 #(1/40) Coeficiente de arratre 
C_L = 1 # Por conveniencia C_L = 1

v0 = v_t 
theta = 0
x0 = 0
y0 = 1000 # Altura inicial 

T = 100
dt = 0.1
N = int (T/dt)+1
t = np.linspace(0.0, T, N) 

u = np.array([v0, theta, x0, y0]) # Lista 

x = np.zeros(N)
y = np.zeros(N)
x[0] = x0
y[0] = y0

for n in range (1, N):
	f1 = -g*sin(u[1])-((C_D/C_L)*(g/v_t**2)*u[0]**2)
	f2 = -g/u[0]*cos(u[1])+((g/v_t**2)*u[0])
	f3 = u[0]*cos(u[1])
	f4 = u[0]*sin(u[1])

	u = u + dt * np.array([f1,f2,f3,f4])
	x[n] = u[2]
	y[n] = u[3]

pyplot.figure(figsize=(10,4)) # Ajusta el tamano de la grafica si quiero volverlo mas cuadrado
# pyplot.ylim(40,160) # Limite de rango en el eje y
pyplot.tick_params(axis="both", labelsize=14)
pyplot.xlabel("x", fontsize=14)
pyplot.ylabel("y", fontsize=14)
pyplot.plot(x,y, 'b--');
pyplot.show()


