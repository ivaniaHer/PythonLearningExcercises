inventario = []
print('---------- SISTEMA DE INVENTARIOS ------------')
cantidad_productos = int(input('Ingrese la cantidad de productos a agregar: '))

for producto in range(cantidad_productos):
    print(f'\nProporcione los valores del producto {producto+1}:')
    nombre_producto = input('Ingrese el nombre del producto: ')
    precio = input('Ingrese el precio del producto: ')
    cantidad = input('Ingrese la cantidad del producto: ')
    detalle =  {
        'id': producto,
        'nombre': nombre_producto,
        'precio': precio,
        'cantidad': cantidad
    }
    inventario.append(detalle)
print(inventario)

busqueda_ID= int(input('Ingrese el ID del producto a buscar: '))
print(f''' 
Información del producto encontrado: 
ID = {busqueda_ID}
    Nombre: {inventario[busqueda_ID].get("nombre")}
    Precio: {inventario[busqueda_ID].get("precio")}
    Cantidad: {inventario[busqueda_ID].get("cantidad")}''')

for i,producto in enumerate(inventario):
    print(f'Producto #{i+1}:')
    for clave, valor in producto.items():
        print(f'\t{clave}: {valor}')

