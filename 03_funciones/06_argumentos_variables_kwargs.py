print('Argumentos variables en forma de diccionario (kwargs)')

def docentes_curso(nombre_docente, *args, **kwargs):
    print(f'\nDocente: {nombre_docente}\nCurso: {args}\nMas info:')
    for clave, valor in kwargs.items():
        print(f'- {clave}: {valor}')

docentes_curso('Nico Hernandez', 'Python', 'Figma', experiencia='2 años', nivel='Intermedio')

print('\n-------------- Imprimir detalles de una persona usando kwargs --------------')

def imprimir_detalles(**kwargs):
    print('\nDetalles de la persona:')
    for clave, valor in kwargs.items():
        print(f'- {clave}: {valor}')

imprimir_detalles(nombre='Nico', apellido = 'Hernandez', edad=30, profesion='Desarrollador')
imprimir_detalles(nombre='Ana', ciudad='Madrid', hobby='Fotografía')