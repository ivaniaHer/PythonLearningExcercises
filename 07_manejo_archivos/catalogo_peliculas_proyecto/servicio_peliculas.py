# Entidad pelicula con atributo nombre
#Servicio peliculas tener nombre archivo const
# metodo agregarpelicula / listar_peliculas / eliminar achivo peliculas
#Appcatalogo peliculas Menu: agregar/listar/eliminar/salir
#validacion en opciones
import os.path
from pelicula import Pelicula

#os.remove(namefile)

class ServicioPeliculas:
    NOMBRE_ARCHIVO = 'cartelera.txt'

    def __init__(self):
        self.peliculas = []
        if os.path.isfile(self.NOMBRE_ARCHIVO):
            self.peliculas = self.listar_peliculas()
        else:
            self.cargar_pelis_iniciales()

    def eliminar_archivo_peliculas(self):
        os.remove(self.NOMBRE_ARCHIVO)

    def cargar_pelis_iniciales(self):
        pelis_iniciales = [
            'Everything Everywhere All At Once',
            'Perfect Days',
            'Paprika'
        ]
        self.peliculas.extend(pelis_iniciales)
        self.guardar_pelis_archivo(pelis_iniciales)

    def guardar_pelis_archivo(self, peliculas):
        try:
            with open(self.NOMBRE_ARCHIVO, 'a') as archivo:
                archivo.write(Pelicula.escribir_pelicula()+'\n')
        except Exception as e:
            print(e)

    def agregar_pelicula(self, pelicula):
        self.peliculas.append(pelicula)
        self.guardar_pelis_archivo([pelicula])

    def listar_peliculas(self):
        peliculas = []
        try:
            with open(self.NOMBRE_ARCHIVO, 'r') as archivo:
                for linea in archivo:
                    nombre = linea.strip()
                    pelicula = Pelicula(nombre)
                    peliculas.append(pelicula)
        except Exception as e:
            print('Error al obtener las peliculas: '+e)
        return peliculas

    def mostrar_peliculas(self):
        for pelicula in self.peliculas:
            print(pelicula)



