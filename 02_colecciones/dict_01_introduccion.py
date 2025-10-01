print('-------------Diccionarios en Python-------------')
persona = {
    'nombre':'Nico',
    'edad': 20,
    'is_married': True,
    'ciudad': 'San Salvador'
}
print(f'Recuperando el diccionario completo:\n{persona}')
print(f'\nRecuperando un valor por su llave:')
print(f'Nombre: {persona['nombre']}')
print(f'Edad: {persona.get('edad')}')
print(f'Married: {persona.get("is_married")}')

#Iterar sobre un diccionario
print('\nIterando sobre un diccionario:')
for llave, valor in persona.items():
    print(f'Llave: {llave} => Valor: {valor}')

#Iterar solo los valores
print('\nIterando solo los valores:')
for valor in persona.values():
    print(f'Valor: {valor}')

#Iterar solo las llaves
print('\nIterando solo las llaves:')
for llave in persona.keys():
    print(f'Llave: {llave}')