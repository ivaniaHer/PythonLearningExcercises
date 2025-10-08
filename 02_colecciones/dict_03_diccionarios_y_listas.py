print('Listas y diccionarios')
personas = [
    {
        'nombre':'Matias',
        'apellido': 'Dominguez',
        'edad': 19
    },
    {
        'nombre': 'Regina',
        'apellido':'Reyes',
        'edad': 23
    }
]
print(personas)
print(f'''
Nombre: {personas[0].get('nombre')}
Apellido: {personas[0].get('apellido')}
Edad: {personas[0].get('edad')}
''')

# Iterar en los elementos de la lista
for contador,persona in enumerate(personas):
    print(f'Persona {contador} - {persona}\nDetalles:')
    for clave,valor in personas[contador].items():
        print(f'''\t{clave}: {valor}''')