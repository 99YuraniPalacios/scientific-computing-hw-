def minimo (x,y):
    if x<y:
       return x
    else:
       return y

s= minimo (2, 7)

def mcd (x,y):
    m=minimo(x,y)
    for i in range (m,0,-1):
        if x%i==0 and y%i==0:
           return i 


def arecoprime (a,b):
    m=mcd(a,b)
    if m==1:
       return 1
    else:
       return 0

print arecoprime(23,7)
