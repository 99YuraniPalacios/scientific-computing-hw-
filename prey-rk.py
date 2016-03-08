import numpy
import matplotlib
import matplotlib.pyplot

#Creado el 8 de Marzo de 2016
#Autora: Yurani Palacios

X0= 15
Y0= 100
Ky= 2.0
Kyx= 0.01
Kx= 1.06
Kxy=0.01
Delta= 0.1

t= range(101)
Y= range(101)
X= range(101)

def f(x):
   return ((Ky*Y0)-(Kxy*X0*Y0))
def f(y):
   return ((Ky*Y0)+(Kxy*X0*Y0))

for i in range (101):
     Y1= Y0 + Delta*f(Y0+1/2*Delta*f(Y0))
     Y0= Y1
     X1= X0 + Delta*f(Y0+1/2*Delta*f(Y0))
     X0= X1
     Y[i]= Y1
     X[i]= X1
     t[i]=i*0.1



Ynew=numpy.array(Y)
Xnew=numpy.array(X)
tnew=numpy.array(t)

print Ynew
print Xnew
print tnew

matplotlib.pyplot.plot(tnew, Ynew)
matplotlib.pyplot.plot(tnew, Xnew)
matplotlib.pyplot.show()

matplotlib.pyplot.plot(tnew, Xnew)
matplotlib.pyplot.plot(tnew, Ynew)
matplotlib.pyplot.show()

matplotlib.pyplot.plot(Ynew, Xnew)
matplotlib.pyplot.plot(Xnew, Ynew)
matplotlib.pyplot.show()
