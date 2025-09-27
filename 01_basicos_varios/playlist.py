print('-------------Un playlist de canciones-------------')
lista_reproduccion = []

num_canciones = int(input('¿Cuántas canciones quieres agregar a la lista de reproducción? : '))
for i in range(num_canciones):
    cancion = input(f'Ingresa el nombre de la canción {i+1}: ')
    lista_reproduccion.append(cancion)


# ordenar lista
#lista_reproduccion.sort(reverse=True)
lista_reproduccion.sort( )


print('\nLista de reproducción ordenada:\n')
for cancion in lista_reproduccion:
    print('- ',cancion)
