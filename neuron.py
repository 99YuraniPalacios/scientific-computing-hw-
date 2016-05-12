# Creado el 29 de Marzo de 2016
# Autora: Yurani Melisa Palacios

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import sys
#from scipy.interpolate import interp1d

#Declarando constantes:
delta1 = 0.003
delta2 = 0.001

CM = 0.1 
I = 15. 

V0 = -65.	
VK = -77. 	
VNa = 50. 	
VL = -5.44	

gK = 36. 
gNa = 120. 
gL = 0.3 

n0 = 0.317
m0 = 0.05
h0 = 0.6

T = 6.3  
phi = 3. **((T-6.3)/10.) 


def fan(v):								
	Alphan = phi * (0.01 * (v + 10.)/(np.exp ((v+10.)/10.)-1.))
	return Alphan
	
def fam(v):
	Alpham = phi * (0.01 * (v + 25.)/(np.exp ((v+25.)/10.)-1.))
	return Alpham

def fah(v):
	Alphah = phi * (0.07 * np.exp(v/20))
	return Alphah

def fbn(v):
	Bethan = phi * (0.125 * np.exp(v/80.))
	return Bethan
def fbm(v):
	Betham = phi * (4. * np.exp(v/18.))
	return Betham
def fbh(v):
	Bethah = phi * (1./(np.exp((v+30.)/10.) + 1.))
	return Bethah

#Definiendo funciones n, m, h:
def fn(n):
	N = fan(V0) * (1-n) - fbn(V0)*n
	return N
def fm(m): 
	M = fam(V0) * (1-m) - fbm(V0)*m
	return M
def fh(h):
	H = fah(V0) * (1-h) - fbh(V0)*h
	return H 


#Definiendo funcion V:
def fv(v):
	Na = gNa  *  (fm(m0)**3.)  *  fh(h0)  *  (v-VNa)
	K =  gK   *  (fn(n0)**4.)  *  (v-VK)
	L =  gL   *  (v-VL)
	ActionPotencial = (I - K - Na - L) / CM
	return ActionPotencial

#Estableciendo parametros:

t1 = np.linspace(0, 5, num=3000, endpoint=True)
t2 = np.linspace(0, 5, num=500, endpoint=True)
n = np.zeros(len(t1))
m = np.zeros(len(t1))
h = np.zeros(len(t1))
V = np.zeros(len(t2))

n[0] = n0
m[0] = m0
h[0] = h0
V[0] = V0
 	

for i in range(len(t1)):

	n1 = n0 + delta1 * fn(n0 + 0.5 * delta1 * fn(n0))
	n0 = n1

	m1 = m0 + delta1 * fm(m0 + 0.5 * delta1 * fm(m0))  
	m0 = m1

	h1 = h0 + delta1 * fh(h0 + 0.5 * delta1 * fh(h0))
	h0 = h1

	n[i] = n1
	m[i] = m1
	h[i] = h1
for i in range(len(t2)):
	
	V1 = V0 + delta2 * fv(V0 + 0.5 * delta2 * fv(V0)) 
	V0 = V1

	V[i] = V1

#Graficando:
plt.plot(t1,n, 'r', label ='n')
plt.plot(t1,m, 'g', label ='m')
plt.plot(t1,h, 'b', label ='h')
plt.legend()
plt.show()

plt.plot(t2,V)
plt.xlabel('t')
plt.ylabel('V')
plt.show()










































