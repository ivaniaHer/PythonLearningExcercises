print('------------ Argumentos por nombres ------------')
def persona (nombre, apellido=None, edad=0):
    print(f'Nombre: {nombre}\nApellido: {apellido}\nEdad: {edad}')

print("Llamada normal:")
persona('Nico', 'Hernandez', 20)
print("\nLlamada con argumentos por nombre:")
persona(edad=20, nombre='Nico', apellido='Hernandez')
print('\nLlamada con parametros incompletos:')
persona(nombre='Nico')
