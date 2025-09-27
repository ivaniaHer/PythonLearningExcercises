print("------------- Combinacion de listas y tuplas -------------")


productos = [
    ('C001', 'Camiseta', 19.99),
    ('C002', 'Cardigan', 30.00),
    ('C003', 'Jeans', 35.99)
]
#Imprimir información de productos
precio_total = 0
print('Información de productos:')
for producto in productos:
    id, descripcion, precio = producto
    print(f'Producto: id = {id}, Descripcion = {descripcion}, Precio = ${precio}')
    precio_total += precio
print(f'El precio total es: ${precio_total:.2f}')
