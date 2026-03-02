from p_01_db.zona_fit_db.cliente_DAO import Cliente_DAO
from p_01_db.zona_fit_db.cliente import Cliente


ejecutar = True
while ejecutar:
    print("""
-------- Sistema de gestion de clientes --------
    1. Listar clientes
    2. Agregar un cliente
    3. Modificar cliente
    4. Eliminar cliente
    5. Salir
    """)
    opc = int(input('Ingresa el numero con la opcion a realizar: '))
    match opc:
        case 1:
            print('LISTADO DE CLIENTES REGISTRADOS')
            lista_clientes = Cliente_DAO.seleccionar()
            for cliente in lista_clientes:
                print(cliente)
        case 2:
            print('AGREGAR UN CLIENTE')
            nombre = input('Nombre: ')
            apellido = input('Apellido: ')
            membresia = int(input('Membresia: '))
            cliente_nuevo = Cliente(nombre=nombre, apellido=apellido, membresia=membresia)
            print(f'Clientes agregados correctamente: {Cliente_DAO.insertar(cliente_nuevo)}')
        case 3:
            print("MODIFICAR UN CLIENTE")
            id = int(input('Id:'))
            nombre = input('Nombre: ')
            apellido = input('Apellido: ')
            membresia = int(input('Membresia: '))
            cliente_modificado = Cliente(id=id, nombre=nombre, apellido=apellido, membresia=membresia)
            print(f'Clientes modificados correctamente: {Cliente_DAO.actualizar(cliente_modificado)}')
        case 4:
            print('ELIMINAR CLIENTE')
            id = int(input('Ingresa el id del cliente al eliminar: '))
            cliente_eliminar = Cliente(id=id)
            print(f'Clientes eliminados correctamente: {Cliente_DAO.eliminar(cliente_eliminar)}')
        case 5:
            print('Bye')
            ejecutar = False

        case _:
            print('Opcion Invalida')
