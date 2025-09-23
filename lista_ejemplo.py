mi_lista = [1, 2, 3, 4, 5]
print(mi_lista)
mi_lista.append(6)
print(f'Agregamos un elemento al final de la lista: {mi_lista}')
mi_lista[2] = 10
print(f'Cambiar el valor del indice 2: {mi_lista}')
mi_lista.insert(2,20)
print(f'Insertar un valor en el indice 2: {mi_lista}')
mi_lista.remove(1)
print(f'Eliminar el valor 1 de la lista: {mi_lista}')
mi_lista.pop()
print(f'Eliminar el ultimo valor de la lista: {mi_lista}')
mi_lista.pop(2)
print(f'Eliminar el valor del indice 2: {mi_lista}')
del mi_lista[0]
print(f'Eliminar el valor del indice 0: {mi_lista}')
sublista = mi_lista[1:3]
print(f'Crear una sublista desde el indice 1 hasta el 3 (sin incluir el 3): {sublista}')
