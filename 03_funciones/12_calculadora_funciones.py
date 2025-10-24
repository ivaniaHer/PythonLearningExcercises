print('---------- Calculadora Simple ----------\n')

def calculadora():
    while True:
        print('Menú de Operaciones:\n')
        print('1. Sumar')
        print('2. Restar')
        print('3. Multiplicar')
        print('4. Dividir')
        print('5. Salir\n')

        try:
            opcion = input_opcion()

            if opcion == 5:
                print('\nSaliendo de la calculadora. ¡Hasta luego!')
                break
            a = float(input('Ingresa el primer número: '))

            if opcion == 4:
                b = input_float('Ingresa el segundo número: ', non_zero=True)
            else:
                b = float(input('Ingresa el segundo número: '))

        except ValueError:
            print('Error: Debes ingresar un número válido entre 1 y 5.\n')
            continue

        match opcion:
            case 1:
                resultado = sumar(a, b)
                print(f'El resultado de la suma es: {resultado}\n')
            case 2:
                resultado = restar(a,b)
                print(f'El resultado de la resta es: {resultado}\n')
            case 3:
                resultado = multiplicar(a,b)
                print(f'El resultado de la multiplicación es: {resultado}\n')
            case 4:
                resultado = dividir(a,b)
                if resultado is not None:
                    print(f'El resultado de la división es: {resultado}\n')
            case _:
                print('Error: Opción no válida. Por favor, ingresa un número entre 1 y 5.\n')

def input_opcion(prompt='Selecciona una opción (1-5): '):
    while True:
        try:
            opc = int(input(prompt))
            if 1 <= opc <= 5:
                return opc
            else:
                print('Error: Debes ingresar un número válido entre 1 y 5.\n')
        except ValueError:
            print('Error: Debes ingresar un número válido entre 1 y 5.\n')

def input_float(prompt='Ingresa un numero: ', non_zero=False):
    while True:
        try:
            valor = float(input(prompt))
            if non_zero and valor == 0:
                print('Error: El valor no puede ser cero.\n')
                continue
            return valor
        except ValueError:
            print('Error: Debes ingresar un número válido.\n')

def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b
def dividir(a, b):
    if b == 0:
        print('\nERROR: No se puede dividir entre cero!!!!!\n')
        return None
    return a / b

calculadora()