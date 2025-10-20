print('-------------- Argumentos variables --------------')
def docentes_curso(nombre_docente, curso, *args):
    print(f'\nDocente: {nombre_docente} - Curso: {curso} - Temas: {args}')
    for tema in args:
        print(f'Tema: {tema}')

docentes_curso('Nico Hernandez', 'Python', 'Funciones', 'Argumentos', 'Tuplas')
docentes_curso('Alejandra Gomez', 'JavaScript', 'Variables', 'Objetos')
docentes_curso('Luisa Martinez', 'Data Science')