nombre_archivo = 'mi_archivo.txt'

# Leer un archivo con readlines

with open(nombre_archivo, 'r') as archivo:
 #  print(archivo.readlines())
    lineas = archivo.readlines()
    for linea in lineas:
        print(linea.strip())

# leer usando read()
print('\nMetodo read')
with open(nombre_archivo, 'r') as archivo:
    print(archivo.read())