my_set = {1,2,3,4,5}
print(f'Set inicial: {my_set}')
my_set.add(6) #agregar un elemento
my_set.add(7)
my_set.add(6) #no agrega el elemento porque ya existe
print(f'Set despues de agregar elementos: {my_set}')

#Eliminar elementos
my_set.remove(1)
print(f'Set despues de eliminar el elemento 1: {my_set}')

#Iterar sobre un set
for elemento in my_set:
    print(elemento, end=' ')

# Comprobar si un valor existe en un set
print(f'Existe el valor 1 en el set: {1 in my_set}')
print(f'Existe el valor 2 en el set: {1 in my_set}')

# Obtener la longitud de un set
print(f'Longitud del set: {len(my_set)}')