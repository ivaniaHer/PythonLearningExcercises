from p_01_db.zona_fit_db.cliente import Cliente
from p_01_db.zona_fit_db.conexion import Conexion

class cliente_DAO:
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

if __name__ == '__main__':
    clientes = cliente_DAO.seleccionar()
    for cliente in clientes:
        print(cliente)