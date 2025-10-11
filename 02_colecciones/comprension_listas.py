numeros = [1,2,3,4,5]
cuadrados = [x**2 for x in numeros]
print(cuadrados)

# Lista de numeros pares
numeros = range(1,10+1)
pares = [x for x in numeros if x%2==0]
print(pares)

# Lista de saludos
nombres = ['Maria','Lola', 'Vero','Sami']
saludando = [f'Hola {nombre}' for nombre in nombres]
print(saludando)