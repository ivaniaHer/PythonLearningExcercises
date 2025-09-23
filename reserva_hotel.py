print('*** Sistema de Reserva de Hotel ***')

name=input('Ingrese su nombre: ')

dias_estadia=int(input('Días de estadía: '))
vista_al_mar=input('Desea vista al mar? (Si/No): ').strip().lower() == 'si'

PRECIO_CUARTO_VISTA_AL_MAR=190.50
PRECIO_CUARTO_SIN_VISTA_AL_MAR=150.50

if not vista_al_mar:
    precio_total = dias_estadia * PRECIO_CUARTO_SIN_VISTA_AL_MAR
else:
    precio_total = dias_estadia * PRECIO_CUARTO_VISTA_AL_MAR

print('-------------------- Detalles de la Reserva --------------------')
print(f'Cliente: {name}')
print(f'Días de estadía: {dias_estadia}')
print(f'Precio total ${precio_total:.2f} ')
print(f'Habitación con vista al mar: {"Sí" if vista_al_mar else "No"}')
print('------------------------------------------------------------------')
