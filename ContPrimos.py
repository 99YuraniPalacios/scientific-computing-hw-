# Jun/09/2016
# Yurani Melisa Palacios Palacios

# Problema Avanzado 

# La funcion de conteo primer (pi (n)) se define como el numero de primos no mayor que n. 
# Haz un diagrama de pi para n <= 2000 y sobre parcela de las aproximaciones

# Pista: la funcion de Li (x) esta contenido en el paquete de mpmath

import numpy as np
import matplotlib.pyplot as plt
import ModPrimes as Mod
import mpmath as mp 

n = 100
x = np.zeros(n, dtype=int)
y = np.zeros(n, dtype=int)
for k in range(n):

	x[k] = k
	y[k] = Mod.countprimes(k)

plt.plot(x, y, 'k', linewidth=4)

# Anadir aproximacion 

x1 = np.linspace(2, n, num = 200)
y1 = x1 / np.log(x1)

plt.plot(x1, y1, 'b', linewidth=4)
plt.show()

# Anadir 2 aproximacion

# from mpmath import mp

mp.dps = 100

x2 = lambda ((x1/np.log(x1)), x, 100)

plt.plot(x2,'b', linewidth=4)
plt.show()

#mp.quad(lambda x: mp.exp(n))





