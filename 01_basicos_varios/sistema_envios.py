print('---------Sistema de Envios---------')
envio_nacional = 10
envio_internacional = 20
costo_total = None

#Validar tipo de envío
while True:
    tipo_envio = input('Ingrese el tipo de envío (Nacional/Internacional): ').strip().lower()
    if tipo_envio in ['nacional', 'internacional']:
        break
    else:
        print('Tipo de envío no válido. Por favor, ingrese "Nacional" o "Internacional".')
#Validar peso
while True:
    try:
        peso = float(input('Ingrese el peso del paquete en kilogramos: '))
        if peso<0:
            print('El peso no puede ser negativo. Por favor, ingrese un valor válido.')
        else:
            break
    except ValueError:
        print('Entrada no válida. Por favor, ingrese un número.')

#Calcular costo total
if tipo_envio == 'nacional':
    costo_total = peso * envio_nacional
else:
    costo_total = peso * envio_internacional

print(f'El costo total del envío es: {costo_total}')