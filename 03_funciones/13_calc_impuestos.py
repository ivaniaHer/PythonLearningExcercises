print('------- Calculadora de Impuestos -------\n')

def validar(prompt):
    while True:
        try:
            monto = float(input(prompt))
            if monto < 0:
                print('Error: El monto no puede ser negativo. Inténtalo de nuevo.\n')
                continue
            return monto
        except ValueError:
            print('Error: Debes ingresar un número válido.\n')

pago_monto = validar(prompt='Ingresa el monto del pago: $')
impuesto_monto = validar(prompt='Ingresa el porcentaje de impuesto (por ejemplo, para 15% ingresa 15): ')

def calcular_impuestos(pago,impuesto):
    total_con_impuesto = pago + (pago * (impuesto / 100))
    print(f'\nEl monto total con impuesto es: ${total_con_impuesto:.2f}\n')

calcular_impuestos(pago_monto, impuesto_monto)

