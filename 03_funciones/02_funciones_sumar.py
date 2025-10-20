from modulo_func_sumar import sumar, es_par

print(__name__)
if __name__ == '__main__':
    print('\nFuncion de sumar')
    resultado = sumar(8,93)
    print(f'Resultado de la funcion sumar: {resultado}')

if __name__ == '__main__':
    numero = int(input('\nIngrese un número para verificar si es par o impar: '))
    if es_par(numero):
        print(f'El número {numero} es par.')
    else:
        print(f'El número {numero} es impar.')
