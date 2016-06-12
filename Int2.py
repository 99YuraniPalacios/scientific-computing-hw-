# Jun/12/2016
# Yurani Melisa Palacios Palacios 

# Integration, being as important as it is, has several highly efficient implementations available for us. 
# Among them are the ones found in scipy 
# "Integracion, siendo tan importante como lo es, tiene varias implementaciones altamente eficientes disponibles para nosotros.
#  Entre ellos se encuentran los que se encuentran en scipy"

import numpy as np
import mpmath
import scipy.integrate as integrate

def function (x):

	return 1 / np.log(x)

result = integrate.quad( function, 2, 10)

print result
print mpmath.li (10, ofsset=True)

