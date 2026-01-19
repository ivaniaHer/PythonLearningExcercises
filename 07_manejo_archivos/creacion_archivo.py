nombre_archivo = 'mi_archivo.txt'

with open(nombre_archivo, 'w') as archivo:
    archivo = open(nombre_archivo, 'w')
    archivo.write('Hi, how are you?')
    archivo.write('\nI am adding information to the file...\n')

#archivo = open(nombre_archivo, 'w')
#archivo.write('Hi, how are you?')
#archivo.write('\nI am adding information to the file...\n')
#archivo.close()

print(f'Se creo el archivo: {nombre_archivo}')