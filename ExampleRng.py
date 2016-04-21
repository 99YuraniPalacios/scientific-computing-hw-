import numpy as np
import matplotlib 
import matplotlib.pyplot as plt 

#np.random.uniform(a, b)
#np.random.binomial(N, p)
#np.random.normal(mu, sigma)



#n = 50000

#xu = np.random.uniforme(-20, 20, n)
#xb = np.random.binomial(200, 0.25, n)
#xn = np.random.normal(0.0, 10, n)

#bins = 30

#y1, x1 = np.histogram(xu, bins=bins, density=true)
#y2, x2 = np.histogram(xu, bins=bins, density=true)
#y3, x3 = np.histogram(xu, bins=bins, density=true)

#x1 = x1[0 : -1] + 0.5 * (x1[1] - x1[0])
#x2 = x2[0 : -1] + 0.5 * (x2[1] - x2[0])
#x3 = x3[0 : -1] + 0.5 * (x3[1] - x3[0])

#plt.plot (x1, y1, 'b-')
#plt.plot (x2, y2, 'r-')
#plt.plot (x3, y3, 'g-')
	

import numpy as np

a = [4,6,12]

np.cumsum(a)

plt.plot(a)
plt.show()
