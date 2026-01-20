import os.path
from snack import Snack

class ServicioSnacks:
    NOMBRE_ARCHIVO = 'snacks.txt'

    def __init__(self):
        self.snacks = []
        # Revisar si ya existe el archivo, obtener snacks de ser así. O cargar snacks iniciales
        if os.path.isfile(self.NOMBRE_ARCHIVO):
            self.snacks = self.obtener_snacks()
        else:
            self.cargar_snacks_iniciales()

    def cargar_snacks_iniciales(self):
        snacks_iniciales = [
            Snack('Papitas', 2),
            Snack('Coca', 1),
            Snack('Sandwich', 3)
        ]
        self.snacks.extend(snacks_iniciales)
        self.guardar_snacks_archivo(snacks_iniciales)

    def guardar_snacks_archivo(self,snacks):
        try:
            with open(self.NOMBRE_ARCHIVO, 'a') as archivo:
                for snack in snacks:
                    archivo.write(snack.escribir_snack()+'\n')
        except Exception as e:
            print('Error al guardar snacks')

    def obtener_snacks(self):
        snacks = []
        try:
            with open(self.NOMBRE_ARCHIVO, 'r') as archivo:
                for linea in archivo:
                    id_snack,nombre,precio = linea.strip().split(',')
                    snack = Snack(nombre,float(precio))
                    snacks.append(snack)
        except Exception as e:
            print('Error al leer el archivo de snacks:'+{e})
        return snacks

    def agregar_snack(self, snack):
        self.snacks.append(snack)
        self.guardar_snacks_archivo([snack])

    def mostrar_snacks(self):
        print('----------------- Snacks en el inventario -----------------')
        for snack in self.snacks:
            print(snack)

    def get_snacks(self):
        return self.snacks