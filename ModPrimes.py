# The number has to be larger than 0
# f = 0 no prime
# f = 1 prime
def isprime(u):

	h = 0
	if u == 1:
		f = 0

	else:

		for k in range(2, u):
			if u % k == 0:
				h = 1
				break

		if h == 1:
			f = 0
		else:
			f = 1

	return f

# Program designed to test Waring's conjecture
def waring(n):


	if isprime(n) == 1:

		return n
	
	else:

		for p in range(2, n):

			if isprime(p) == 1:
			
				k = n - p

				for q in range(2, k):

					if isprime(q) == 1:

						r = k - q

						if isprime(r) == 1:
						
							return p, q, r

	return 0

# counts the number of primes below a given number
def countprimes(v):

        i = 0

        for j in range(1, v + 1):
                
                if isprime(j) == 1 : 
                        i = 1 + i

        return i

