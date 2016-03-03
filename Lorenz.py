import numpy
import matplotlib
import matplotlib.pyplot

#Creado el 3 de Marzo de 2016
#Autora: Yurani Palacios 

# Atractor de Lorenz

X0= 0.2
Y0= 1.0
Z0= 1.05
Sigma= 10
Rho= 28
Beta= 2.667
Delta= 0.01

t= range(10001)
X= range(10001)
Y= range(10001)
Z= range(10001)

X[0]= X0
Y[0]= Y0
Z[0]= Z0

for i in range (1, 10001):
  X1= (Delta*Sigma*Y0)-(Delta*Sigma*X0)+X0
  Y1= (Delta*X0*Rho)-(Delta*X0*Z0)-(Delta*Y0)+Y0
  Z1= (Delta*X0*Y0)-(Delta*Beta*Z0)+Z0
  X0= X1
  Y0= Y1
  Z0= Z1
  X[i]=X1
  Y[i]=Y1
  Z[i]=Z1
  t[i]= i*Delta

Xnew=numpy.array(X)
Ynew=numpy.array(Y)
Znew=numpy.array(Z)
tnew=numpy.array(t)

print Xnew
print Ynew
print Znew
print tnew

matplotlib.pyplot.plot(Xnew, Znew)
matplotlib.pyplot.show()
