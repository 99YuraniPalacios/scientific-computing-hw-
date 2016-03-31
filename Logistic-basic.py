import numpy
import matplotlib
import matplotlib.pyplot

# crear las funciones basicas para evaluar el mapa logistico
# Creado: 4-Febrero-2016
# Autora: Yurani Palacios 

t=range(50)
y=range(50)
r = 3.7
y0 = 0.1

for i in range(50):
	y1 = r * y0 * (1-y0)
	y0=y1	
	y[i]=y1
	t[i]=i
print y

ynew=numpy.array(y)
tnew=numpy.array(t)

print ynew
print tnew 

matplotlib.pyplot.plot(tnew,ynew)
matplotlib.pyplot.show()
