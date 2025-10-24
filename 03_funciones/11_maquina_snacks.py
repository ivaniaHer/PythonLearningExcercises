print('------------ Máquina de Snacks ------------')

snacks = [
    {'id': 1, 'nombre': 'Papas Fritas', 'precio': 1.50},
    {'id': 2, 'nombre': 'Galletas', 'precio': 1.00},
    {'id': 3, 'nombre': 'Chocolate', 'precio': 2.00},
    {'id': 4, 'nombre': 'Refresco', 'precio': 1.75},
]

carrito = []


def maquina_snacks():
    total_compra = 0.0
    while True:
        print('\n Menú de Opciones:')
        print('1. Mostrar snacks disponibles')
        print('2. Comprar snack')
        print('3. Mostrar ticket')
        print('4. Salir')
        try:
            opc=int(input('Selecciona una opción (1-4): '))
        except ValueError:
            print('Error: Debes ingresar un número válido entre 1 y 4.')
            continue
        match opc:
            case 1:
                mostrar_snacks(snacks)
            case 2:
                total_compra = comprar_snacks(snacks, carrito, total_compra)
            case 3:
                mostrar_ticket(carrito, total_compra)
            case 4:
                print('Gracias por usar la máquina de snacks. ¡Hasta luego!')
                break
            case _:
                print('Error: Opción no válida. Por favor, ingresa un número entre 1 y 4.')

def mostrar_snacks(lista_snacks):
    print('\n--- Snacks Disponibles ---\n')
    for snack in lista_snacks:
        print(f'ID: {snack.get("id")}\n'
              f'Nombre: {snack.get("nombre")}\n'
              f'Precio: ${snack.get("precio")}\n')

def comprar_snacks(lista_snacks, carrito_compra, compra):
    try:
        snack_id = int(input('Ingresa el ID del snack que deseas comprar: '))
    except ValueError:
        print('Error: Debes ingresar un número válido para el ID del snack.')
        return compra

    for snack in lista_snacks:
        if snack.get('id') == snack_id:
            precio_raw = snack.get('precio',0)
            try:
                precio = float(precio_raw)
            except (ValueError, TypeError):
                print('Error: El precio del snack no es válido.')
                return compra

            carrito_compra.append(snack)
            compra += precio
            print(f'Snack "{snack.get("nombre")}" agregado al carrito.')
            break
    else:
        print('Error: Snack con el ID ingresado no encontrado.')
    return compra


def mostrar_ticket(carrito_compra, compra):
    print('\n--- Ticket de Compra ---\n')
    if not carrito_compra:
        print('El carrito está vacío. No hay snacks comprados.')
    else:
        for snack in carrito_compra:
            print(f'Nombre: {snack.get("nombre")} - ${snack.get("precio")}')
    print('Total a pagar: ${:.2f}'.format(compra))

    return

maquina_snacks()