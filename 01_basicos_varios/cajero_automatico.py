saldo = 1000.00

salir = False

while not salir:
    print(f'''--------Cajero Automatico--------'
Operaciones que puedes realizar:
    1. Consultar saldo
    2. Retirar
    3. Depositar
    4. Salir''')
    opcion = int(input('Elige una opcion (1-4): '))

    if opcion == 1:
        print(f'Tu saldo es: ${saldo}\n')
    elif opcion == 2:
        monto = float(input('Ingresa el monto a retirar:'))
        if monto > saldo:
            print(f'''OPERACIÓN FALLIDA: Fondos insuficientes
                  Tu saldo es: ${saldo} \n''')
        else:
            saldo -= monto
            print(f'Tu nuevo saldo es: ${saldo}\n')
    elif opcion ==3:
        monto = float(input('Ingresa el monto a depositar:'))
        saldo += monto
        print(f'Tu nuevo saldo es: ${saldo}\n')
    elif opcion ==4:
        print('Gracias por usar el cajero automatico. ¡Hasta luego!')
        salir = True
