# Jun/13/2016
# Yurani Melisa Palacios Palacios 

import numpy as np
import matplotlib.pyplot as plt 
 
def Rk4(f, t0, y0, h, N):

    t = t0 + arange(N+1)*h
    y = zeros((N+1, size(y0)))
    y[0] = y0

    for n in range(N):

        xi1 = y[n]
        f1 = f(t[n], xi1)
        xi2 = y[n] + (h/2.)*f1
        f2 = f(t[n+1], xi2)
        xi3 = y[n] + (h/2.)*f2
        f3 = f(t[n+1], xi3)
        xi4 = y[n] + h*f3
        f4 = f(t[n+1], xi4)
        y[n+1] = y[n] + (h/6.)*(f1 + 2*f2 + 2*f3 + f4)

    return y

def lorenzPlot():
    y = Rk4(fLorenz, 0, array([0,2,20]), .01, 10000)
    fig = figure()
    ax = Axes3D(fig)
    ax.plot(*y.T)

def fLorenz(t,Y): 
  
    def Y(x,y,z):
        return array([10*(y-x), x*(28-z)-y, x*y-(8./3.)*z])

#plt.plot(x0, z0, 'r')
#plt.plot(t1, z1, 'k')

plt.show()
