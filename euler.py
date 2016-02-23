# 23 de febrero 
# Este es el codigo del dia de hoy en clase de Carlos, realizado por Yurani Palacios 
 
import numpy 
import matplotlib
import matplotlib.pyplot 
 
def funciong (r,t):
    return -r*t

def funcionf (z,delta,r):
    return z+delta*funciong(z,r)

y0=0.1
delta=0.01
r=2.0
u=funcionf(y0,delta,r)
print u 


n=100
t=range(n)
y=range(n)

for i in range(n):
    y1=funcionf(y0,delta,r)
    y[i]=y1

