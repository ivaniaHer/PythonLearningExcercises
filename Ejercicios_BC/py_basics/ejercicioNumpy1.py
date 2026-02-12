import numpy as np
numeros=np.array([1,2,3,4,5,6,7,8,9,10])
print(type(numeros))
print(numeros+10)
print(numeros*2)

# Range
rango = np.arange(1,11)
print(rango)

# Estadistica
print(f'Suma: {np.sum(numeros)}')
print(f'Promedio: {np.mean(numeros)}')
print(f'Máximo: {np.max(numeros)}')
print(f'Mínimo: {np.min(numeros)}')

ceros = np.zeros(6)
unos = np.ones(9)

# Arreglos
matriz = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])
print(matriz)
print(matriz*5)
print(matriz[2,2]) # [fila,columna]
