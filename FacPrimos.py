# Jun/09/2016
# Yurani Melisa Palacios Palacios

# Problema avanzado
# Disenar un algoritmo para factorizar un numero entero en sus factores primos. 
# (Sugerencia: utilizar el metodo de factorizacion de Euler)

def factorizar(n):
    #almacenamos los resultados
    #de la factorizacion en una lista
    l = []
    num1 = n
    #mientras podamos dividir por 2
    #el dos es un factor
    while num1 % 2 == 0:
        l.append(2)
        num1 /= 2
    #ahora probamos con los impares
    #empezando por el 3
    cuenta = 3
    raiz = int(math.sqrt(num1))
    while cuenta <= raiz and num1 > 1:
        if num1 % cuenta == 0:
            l.append(cuenta)
            num1 /= cuenta
        else:
            cuenta += 2
    if num1 > 1:
        l.append(num1)
    return l

g = factorizar(34)
print g






