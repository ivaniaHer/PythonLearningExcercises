nombre_archivo = 'mi_archivo.txt'

with open(nombre_archivo, 'a') as archivo:
    #Anexar info al archivo
    archivo.write('Anexando más información.........\n')

print('Se ha anexando la informacion al archivo: '+ nombre_archivo)