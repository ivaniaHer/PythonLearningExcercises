salir = False

while not salir:
    print('''--------Calculadora--------
    Operaciones que puedes realizar:
    1. Suma
    2. Resta
    3. Multiplicacion
    4. Division
    5. Salir''')

    opc = int(input('Elige una opcion (1-4): \n'))

    if 1<= opc <=4:
        operando1= float(input('Ingresa el primer operando: '))
        operando2= float(input('Ingresa el segundo operando: '))


    if opc == 1:
        print(f'{operando1} + {operando2} = {operando1 + operando2}\n ')
    elif opc == 2:
        print(f'{operando1 } - {operando2} = {operando1 - operando2}\n ')
    elif opc == 3:
        print(f'{operando1} * {operando2} = {operando1 * operando2}\n ')
    elif opc == 4:
        if operando2 == 0:
            print('Operando Inválido: No se puede dividir entre 0\n ')
        else:
            print(f'{operando1} / {operando2} = {operando1 / operando2}\n ')
    elif opc == 5:
        print('Gracias por usar la calculadora. ¡Hasta luego!')
        salir = True
    else:
        print('Opcion invalida, por favor ingresa una opcion del 1 al 5\n ')