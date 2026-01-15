#funcion normal sin usar lambda
from functools import reduce


def cuadrado (x):
    return x ** 2

print(cuadrado(2))

#Funciones lambda: son funciones anonimas, cortas y de una sola expresion
#Sintaxis: lambda argumentos: expresion
cuadrado_lambda = lambda x: x**2
print(cuadrado_lambda(2))

# Map y filter
# Map aplica una función a cada elemento de un iterable.
numeros = [1,2,3,4,5]
cuadrados = list(map(lambda x: x**2, numeros))
print(cuadrados)

# Filter
pares = list(filter(lambda x: x%2==0, numeros))
print(pares)

# Reduce
suma_acumulativa = reduce(lambda x,y: x+y, numeros)
print(suma_acumulativa)