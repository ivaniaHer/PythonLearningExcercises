print('------------ Potencia de un número con recursividad ------------')

def potencia_recursiva(base, exponente):
    if exponente == 0:
        print(f'{base}^{exponente} = 1')
        return 1
    else:
        potencia_parcial = base * potencia_recursiva(base, exponente - 1)
        print(f'{base}^{exponente} = {potencia_parcial}')
        return potencia_parcial

base = int(input('Ingrese la base: '))
exponente = int(input('Ingrese el exponente: '))
resultado = potencia_recursiva(base, exponente)