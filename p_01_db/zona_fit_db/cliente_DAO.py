from p_01_db.zona_fit_db.cliente import Cliente
from p_01_db.zona_fit_db.conexion import Conexion

class Cliente_DAO:
    SELECCIONAR = "SELECT * FROM cliente"
    INSERTAR = "INSERT INTO cliente(nombre, apellido, membresia) VALUES (%s, %s, %s)"
    ACTUALIZAR = "UPDATE cliente SET nombre = %s, apellido = %s, membresia = %s WHERE id = %s"
    ELIMINAR = "DELETE FROM cliente WHERE id = %s"


# Metodo para seleccionar y convertir los registros a objetos de tipo cliente
    @classmethod
    def seleccionar(cls):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            cursor.execute(cls.SELECCIONAR)
            registros = cursor.fetchall()
            clientes = []
            for registro in registros:
                registro = Cliente(registro[0], registro[1], registro[2], registro[3])
                clientes.append(registro)
            return clientes
        except Exception as e:
            print(f'Ocurrio un error al obtener la informacion {e}')
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)

# Metodo para insertar un nuevo cliente a partir de la creacion de un objeto tipo Cliente
    @classmethod
    def insertar(cls, cliente):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            valores = (cliente.nombre, cliente.apellido, cliente.membresia)
            cursor.execute(cls.INSERTAR, valores)
            conexion.commit()
            return cursor.rowcount
        except Exception as e:
            print(f'Ocurrio un error al insertar la informacion {e}')
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)

    @classmethod
    def actualizar(cls,cliente):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            valores = (cliente.nombre, cliente.apellido, cliente.membresia, cliente.id)
            cursor.execute(cls.ACTUALIZAR, valores)
            conexion.commit()
            return cursor.rowcount
        except Exception as e:
            print(f'Ocurrio un error al actualizar el registro {e}')
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)

    @classmethod
    def eliminar(cls,cliente):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            cliente_id = (cliente.id,)
            cursor.execute(cls.ELIMINAR, cliente_id)
            conexion.commit()
            return cursor.rowcount
        except Exception as e:
            print(f'Ocurrio un error al eliminar el registro: {e}')
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)

if __name__ == '__main__':
    # insertar
    # cliente1 = Cliente(nombre="Lucia", apellido="Galdamez", membresia=124)
    # print(f'Cliente insertado: {cliente_DAO.insertar(cliente1)}')

    # actualizar
    cliente_act = Cliente_DAO.actualizar(Cliente(id=10, nombre='Lucila', apellido='Gomez', membresia=126))
    print(f'Cliente actualizado: {cliente_act}')

    #eliminar
    cliente_eliminar = Cliente_DAO.eliminar(Cliente(id=9))
    print(f'Cliente eliminado: {cliente_eliminar}')

    # seleccionar
    clientes = Cliente_DAO.seleccionar()
    for cliente in clientes:
        print(cliente)

