import numpy as np
import matplotlib.pyplot as plt
import primes

"""
k = primes.isprime(13)
print k

k = primes.waring(23)
print k

k = primes.waring(33)
print k

n = input('enter an odd number larger than 3: ')
f = primes.waring(n)
print f
"""

n = 2000
x = np.zeros(n, dtype=int)
y = np.zeros(n, dtype=int)
for k in range(n):

	x[k] = k
	y[k] = primes.countprimes(k)

plt.plot(x, y, 'k', linewidth=4)

# add approximation
x1 = np.linspace(2, n, num = 200)
y1 = x1 / np.log(x1)
plt.plot(x1, y1, 'b', linewidth=4)

plt.show()
