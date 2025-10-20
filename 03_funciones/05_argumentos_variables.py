print('-------------- Argumentos variables --------------')
def docentes_curso(nombre_docente, curso, *args):
    print(f'\nDocente: {nombre_docente} - Curso: {curso} - Temas: {args}')
    for tema in args:
        print(f'Tema: {tema}')

docentes_curso('Nico Hernandez', 'Python', 'Funciones', 'Argumentos', 'Tuplas')
docentes_curso('Alejandra Gomez', 'JavaScript', 'Variables', 'Objetos')
docentes_curso('Luisa Martinez', 'Data Science')

print('\n-------------- Suma con argumentos variables --------------')

def suma(*args):
    total = 0
    for numero in args:
        total += numero
    return total

print(f'Resultado de la suma {suma(8,7,8,8,5,6,9,5,3,1,8,5)}')

def alumnos_curso(curso, *args):
    print(f'\nCurso: {curso}\nAlumnos inscritos:')
    for alumno in args:
        print(f'- {alumno}')

alumnos_curso('Python', 'Ana', 'Luis', 'Carlos')
alumnos_curso('JavaScript', 'Marta', 'Sofia')