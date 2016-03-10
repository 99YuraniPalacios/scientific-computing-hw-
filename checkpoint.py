# RK for the 'drugs' problem

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import sys

def f(u, v):
      U = kyx * v * u - kx * u
      V = ky * v - kxy * u * v

return U, V

delta = 0.01
kx = 1.06
ky = 2.0
kxy = 0.01
kyx = 0.01
x0 = 15.0
y0 = 100.

n = 10 / delta
t = np.linspace(0, 10, num=n)
x = np.zeros(len(t))
y = np.zeros(len(t))

for j in range(len(t)):
      X, Y = f(x0, y0)
      P, Q = f(x0 + 0.5 * delta * X, y0 + 0.5 * delta * Y)
      x1 = x0 + delta * P
      y1 = y0 + delta * Q
      x[j] = x1
      y[j] = y1
      x0 = x1
      y0 = y1


plt.plot(x, y)
plt.show()
