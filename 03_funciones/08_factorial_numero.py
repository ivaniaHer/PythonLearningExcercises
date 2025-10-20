print('------------- Calcular factorial de un número -------------')

def factorial_recursiva(numero):
    if numero == 0 or numero == 1:
        print(f'Resultado factorial parcial de {numero} = 1')
        return 1
    else:
        factorial_parcial = numero * factorial_recursiva(numero - 1)
        print(f'Resultado factorial parcial de {numero} = {factorial_parcial}')
        return factorial_parcial

numero = int(input('Ingrese un número para calcular su factorial: '))
resultado = factorial_recursiva(numero)
print(f'Resultado factorial de {numero} es: {resultado}')