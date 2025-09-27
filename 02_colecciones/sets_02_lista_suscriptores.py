print('_____________Lista de suscriptores_____________')

suscriptores = set()

#agregar suscriptores
num_suscriptores = int(input('¿Cuantos suscriptores desea agregar?: '))
for _ in range(num_suscriptores):
    suscriptor = input('Ingrese el correo del suscriptor: ')
    if suscriptor in suscriptores:
        print('El suscriptor ya existe.')
    else:
        suscriptores.add(suscriptor)
print(f'La lista de suscriptores inicial es: {suscriptores}')

#nuevo suscriptor
nuevo_suscriptor = input('Ingrese el correo del nuevo suscriptor: ')
if nuevo_suscriptor in suscriptores:
    print('El suscriptor ya existe.')
else:
    suscriptores.add(nuevo_suscriptor)
    print('Suscriptor agregado exitosamente.')
print(f'La lista de suscriptores actualizada es: {suscriptores}')

#eliminar suscriptor
eliminar_suscriptor = input('Ingrese el correo del suscriptor a eliminar: ')
if eliminar_suscriptor in suscriptores:
    suscriptores.remove(eliminar_suscriptor)
    print(f'El suscriptor "{eliminar_suscriptor}" se ha eliminado exitosamente.')
else:
    print(f'El suscriptor "{eliminar_suscriptor}" no existe.')

#imprimir lista final de suscriptores
print('\nLa lista final de suscriptores es:')
for suscriptor in suscriptores:
    print('-',suscriptor)