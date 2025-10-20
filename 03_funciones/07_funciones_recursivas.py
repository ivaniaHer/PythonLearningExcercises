print('------------ Funciones recursivas ------------')

# definir la funcion recursiva
def funcion_recursiva(numero):
    if numero ==1: # caso base
        print(numero, end=' ')
    else: #caso recursivo
        funcion_recursiva(numero - 1)
        print(numero, end=' ')

funcion_recursiva(10)
