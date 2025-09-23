calificaciones = []

num_calificaciones = int(input('Cuantas calificaciones deseas ingresar?: '))

#pedir calificaciones
for i in range(num_calificaciones):
    calificacion = float(input(f'Calificcion {i+1}: '))
    calificaciones.append(calificacion)
#calcular promedio
promedio = sum(calificaciones) / num_calificaciones

print('Las calificaciones ingresadas son: ', calificaciones)
print(f'El promedio de las calificaciones es: {promedio:.2f}')
