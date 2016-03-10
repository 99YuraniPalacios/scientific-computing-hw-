import numpy
import matplotlib
import matplotlib.pyplot 

#Creado el 8 de Marzo de 2016
#Autora: Yurani Melisa Palacios Palacios 

K=0.2
Y0=200
Delta=0.1
t= range(101)
Y= range(101)

def f(x):
   return -K*x

for i in range(101):
      Y1= Y0 + Delta *f(Y0+1/2*Delta*f(Y0))
      Y0= Y1
      Y[i]= Y1
      t[i]= i*Delta

print Y

Ynew=numpy.array(Y)
tnew=numpy.array(t)

print Ynew
print tnew

matplotlib.pyplot.plot(tnew, Ynew)
matplotlib.pyplot.show()
