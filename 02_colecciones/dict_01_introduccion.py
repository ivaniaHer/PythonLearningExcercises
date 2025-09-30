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