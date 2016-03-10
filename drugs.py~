import numpy 
import matplotlib
import matplotlib.pyplot 

#Creado el 25 de Febrero de 2016
#Autora: Yurani Palacios

# Asuma que originalmente se le suministra a un paciente una cantidad de aspirina de forma que su concentracion de acido acetil-salicilico en la sangre es 200 mg/ml, usando Delta=0.1horas

#Cual es la concentracion despues de 10 horas?

k=0.2
Q0=200
Delta=0.1
t= range(101)
Q= range(101)

for i in range(101):
   Q1= Q0 - Delta * k * Q0
   Q0= Q1
   Q[i]= Q1
   t[i]= i
print Q

Qnew=numpy.array(Q)
tnew=numpy.array(t)

print Qnew
print tnew

matplotlib.pyplot.plot(Qnew, tnew)
matplotlib.pyplot.show()

