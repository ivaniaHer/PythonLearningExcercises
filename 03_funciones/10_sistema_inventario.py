print('=========== Bienvenido al sistema de inventario ===========')

inventario = [
    {'id': 1, 'nombre': 'Laptop', 'cantidad': 10, 'precio': 800.00},
    {'id': 2, 'nombre': 'Mouse', 'cantidad': 50, 'precio': 20.00},
    {'id': 3, 'nombre': 'Teclado', 'cantidad': 30, 'precio': 35.00},
]

def sistema_inventario():
    while True:
        print('\n --- Selecciona una opción ---')
        print("""\t1. Mostrar inventario
    2. Agregar nuevo producto
    3. Buscar producto por ID
    4. Salir del sistema""")

        try:
            opcion = int(input('Ingrese el número de la opción deseada (1-4): '))
        except ValueError:
            print('Error: Debes ingresar un número válido entre 1 y 4.')
            continue

        match opcion:
            case 1:
                mostrar_inventario(inventario)
            case 2:
                agregar_producto(inventario)
            case 3:
                buscar_producto_por_id(inventario)
            case 4:
                print('Saliendo del sistema de inventario. ¡Hasta luego!')
                break
            case _:
                print('Error: Opción no válida. Por favor, ingresa un número entre 1 y 4.')

def mostrar_inventario(lista):
    print('\n----- INVENTARIO DE PRODUCTOS -----\n')
    for producto in lista:
        print(f'''ID: {producto.get("id")}
Nombre: {producto.get("nombre")}
Cantidad: {producto.get("cantidad")}
Precio: ${producto.get("precio")}\n''')

def agregar_producto(lista):
    print('\n ----- AGREGAR NUEVO PRODUCTO -----\n')

    try:
        nombre = input('Nombre: ')
        cantidad = int(input('Cantidad: '))
        precio = float(input('Precio: $'))
    except ValueError:
        print('Valor ingresado no válido. Asegúrate de ingresar números para cantidad y precio.')
        return

    nuevo_id = max([p['id'] for p in lista], default=0) + 1
    detalle_producto = {
        'id': nuevo_id,
        'nombre': nombre,
        'cantidad': cantidad,
        'precio': precio
    }
    lista.append(detalle_producto)
    print(f'Producto "{nombre}" agregado exitosamente al inventario.')

def buscar_producto_por_id(lista):
    print('\n ----- BUSCAR PRODUCTO POR ID -----\n')

    try:
        id_producto = int(input('Ingresa el ID del producto a buscar: '))
    except ValueError:
        print('Error: Debes ingresar un número válido para el ID.')
        return

    for producto in lista:
        if producto.get('id') == id_producto:
            print(f'''Producto encontrado:
    ID: {producto.get("id")}
    Nombre: {producto.get("nombre")}
    Cantidad: {producto.get("cantidad")}
    Precio: ${producto.get("precio")}''')
            break
    else:
        print(f'No se encontró ningún producto con ID {id_producto}.')

sistema_inventario()