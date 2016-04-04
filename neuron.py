# Creado el 29 de Marzo de 2016
# Autora: Yurani Melisa Palacios


import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import sys
from scipy.interpolate import interp1d

delra1 = 0.003
delta2 = 0.001

CM = 0.1 
I = 15 

V0 = -65 
VK = -77 
VNa = 50 
VL = -54.4 

gK = 36 
gNa = 120 
gL = 0.3 

n0 = 0.317
m0 = 0.05
h0 = 0.6

T = 6.3 
phi = 3 **((T-6.3)/10) 

def fan(v):
	return phi * ((0.01 * (v + 10))/(np.exp (((v+10)/10)- 1))
def fam(v):
	return phi * ((0.01 * (v + 25))/(np.exp (((v+25)/10)- 1))
def fah(v):
	return phi * (0.07 * np.exp(v/29))


def fbn(v):
	return phi * (0.125 * np.exp(v/80))
def fbm(v):
	return phi * (4 * np.exp(v/18))
def fbh(v):
	return phi * (1/(np.exp((v+30)/10)+1))

	
def fn(n):
	return fan(V0) * (1-n) - fbn(V0)*n
	
def fm(m):
	return fam(V0) * (1-m) - fbm(V0)*m
def fh(h):
	return fah(V0) * (1-h) - fbh(V0)*h

def fv(v):
	s = (I - (gK**(fn(n0)**4))*(v-VK) - (gNa**((fm(m0)**3)*fh(h0)))*(v-VNa) - ((gL)*(v-VL))) / CM
	












































