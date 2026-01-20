from servicio_snacks import ServicioSnacks
from snack import Snack
class MaquinaSnacks:
    def __init__(self):
        self.servicio_snacks = ServicioSnacks()
        self.productos = []

    def maquina_snacks(self):
        salir = False
        print('========= Maquina de Snacks =========')
        self.servicio_snacks.mostrar_snacks()
        while not salir:
            try:
                opcion = self.mostrar_menu()
                salir = self.ejecutar_opcion(opcion)
            except Exception as e:
                print(f'Ocurrio un error: {e}')

    def mostrar_menu(self):
        print(f'''
        1. Comprar Snack
        2. Mostrar ticket
        3. Agregar nuevo snack al inventario
        4. Inventario snacks
        5. Salir
''')
        return  int(input('Elige una opcion: '))

    def ejecutar_opcion(self, opcion):
        if opcion == 1:
            self.comprar_snack()
        elif opcion == 2:
            self.mostrar_ticket()
        elif opcion == 3:
            self.agregar_snack()
        elif opcion == 4:
            self.servicio_snacks.mostrar_snacks()
        elif opcion == 5:
            print('Regresa pronto')
            return True
        else:
            print(f'Opcion invalida: {opcion}')
        return False

    def comprar_snack(self):
        id_snack = int(input('Que snack deseas comprar (id)'))
        snacks = self.servicio_snacks.get_snacks()
        snack = next((snack for snack in snacks if snack.id_snack == id_snack), None)
        if snack:
            self.productos.append(snack)
            print(f'Snack encontrado: {snack}')
        else:
            print(f'Id snack no encontrado: {snack}')

    def mostrar_ticket(self):
        if not self.productos:
            print(f'No hay snacks en el ticket')
            return
        total = sum(snack.precio for snack in self.productos)
        print(f'----- Ticket de venta -----')
        for producto in self.productos:
            print(f'\t{producto.nombre} - ${producto.precio:.2f}')
        print(f'\tTotal -> ${total:.2f}')

    def agregar_snack(self):
        nombre = input('Nombre del snack: ')
        precio = float(input('Precio del snack: '))
        nuevo_snack = Snack(nombre,precio)
        self.servicio_snacks.agregar_snack(nuevo_snack)
        print(f'Snack agregado correctamente.')

#principal
if __name__ == '__main__':
    maquina_snacks = MaquinaSnacks()
    maquina_snacks.maquina_snacks()