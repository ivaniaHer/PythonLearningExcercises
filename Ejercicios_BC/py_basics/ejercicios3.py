# Ejercicio 1: Imprimir números del 1 al 10
for x in range(1,10+1):
    print(x)

# Ejercicio 2: Imprimir números pares del 2 al 20
for x in range(2,20+1):
    if x % 2 == 0:
        print(x)

# Ejercicio 3: Recorrer una lista de nombres
names = ['Nico','Jeanette','Nana','Lucia','Seso', 'Alexi']
for x in names:
    print(x)

# Ejercicio 4: Contar letras de una palabra
word = input('Ingresa una palabra: ')
print(f'Cantidad de letras en la palabra: {len(word)}')
# 2da forma
res = 0
for x in word:
    res +=1
print(f'Cantidad de letras en la palabra: {res}')

# Ejercicio 5: Sumar números usando bucle
sumaB = 0
while True:
    opc = int(input('Ingresa una opción: \n1. Sumar número \n2. Salir y mostrar resultado\n='))
    if opc == 1:
        num = int(input('Ingresa el número a sumar: '))
        sumaB += num
    elif opc == 2:
        print(f'La suma total fue de: {sumaB}')
        print('adios:c')
        break
    else:
        print(f'Número invalido')

# Ejercicio 6: Pedir datos hasta que el usuario escriba "salir"
lista1 = []
print('Ingresa palabras para añadir a la lista - Escribe "salir" para finalizar')
while True:
    wordL = input('Ingresa tu palabra: ')
    if wordL.lower().strip() == "salir":
        print(f'Finalizando ejecución\nLista de palabras ingresadas: {lista1}')
        break
    lista1.append(wordL)

# Ejercicio 7: Dada una lista de edades, muestra cada una
edades = [10,12,34,55,22,17]
print(f'Lista de edades')
for edad in edades:
    print(f'-{edad}')

# Ejercicio 8: Imprimir los números del 10 al 1
for x in range(10,0,-1):
    print(x)

# Ejercicio 9: Mostrar los números impares del 1 al 15
print('Número impares del 1 al 15:')
for nums in range (1,15+1):
    if nums % 2 == 1:
        print(nums)

# Ejercicio 10: Contar cuántos elementos tienen una lista sin usar len()
lista2 = [1,2,3,4,3,34,3,23,4,4,4]
contador = 0
for elemento in lista2:
    contador += 1
print(contador)
print(len(lista2))

# Ejercicio 11: Calcular la suma de todos los números de una lista
lista_numeros = [10,10,10,10,10]
suma_lista = 0
for o in lista_numeros:
    suma_lista += o
print(f'Resultado de la suma: {suma_lista}')
print(sum(lista_numeros))

# Ejercicio 12: Contar cuántos números pares hay del 1 al 50:
cont_pares = 0
for x in range (1,50+1):
    if x % 2 == 0:
        cont_pares += 1
print(f'Hay {cont_pares} pares del 1 al 50')