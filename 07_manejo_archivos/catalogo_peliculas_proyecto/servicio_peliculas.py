import os.path

class ServicioPeliculas:

    def __init__(self):
        self.nombre_archivo = 'peliculas.txt'

    def agregar_pelicula(self, pelicula):
        with open(self.nombre_archivo,'a',encoding='utf-8') as archivo:
            archivo.write(f'{pelicula.nombre}\n')

    def listar_peliculas(self):
        try:
            with open(self.nombre_archivo, 'r', encoding='utf-8') as archivo:
                print(archivo.read())
        except Exception as e:
            print('Error al obtener las peliculas: '+e)

    def eliminar_archivo_peliculas(self):
        os.remove(self.nombre_archivo)
        print('Archivo eliminado',self.nombre_archivo)



