mes = int(input('Ingrese el mes (1-12): '))

if mes in [12, 1, 2]:
    estacion = 'Invierno'
elif mes in [3,4,5]:
    estacion = 'Primavera'
elif mes in [6,7,8]:
    estacion = 'Verano'
elif mes in [9,10,11]:
    estacion = 'Otoño'
else:
    estacion = 'desconocida'

print(f'La estacion es: {estacion}')