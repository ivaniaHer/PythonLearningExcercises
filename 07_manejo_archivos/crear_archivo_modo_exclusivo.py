nombre_archivo = 'mi_archivo.txt'

try:
    with open(nombre_archivo, 'x' ) as archivo:
        archivo.write('Escritura en modo exclusivo\n')
        archivo.write('Espero sea util\n')
    print(f'Se ha creado el archivo correctamente')
except FileExistsError:
    print(f'El archivo "{nombre_archivo}" ya existe')