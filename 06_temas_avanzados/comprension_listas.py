#Filtrar numeros por pares de una lista

numeros = range(1,10+1)

# sin comprension de listas

numeros_pares = []
for numero in numeros:
    if numero % 2 == 0:
        numeros_pares.append(numero)
print(numeros_pares)

# con comprension de listas
# sintaxis: [expresion for item in iterable if condicion]

numeros_pares_comp = [numero for numero in numeros if numero % 2 == 0]
print(numeros_pares_comp)