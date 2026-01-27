from servicio_peliculas import ServicioPeliculas
from pelicula import Pelicula

class CatalogoPeliculas:
    def __init__(self):
        self.servicio_peliculas = ServicioPeliculas()

    def agregar_peliculas(self):
        nombre = input('Nombre de la pelicula: ')
        self.servicio_peliculas.agregar_pelicula(nombre)
        print('Pelicula agregada correctamente')

    def menu_peliculas(self):
        while True:
            try:
                print('''
    Menú de peliculas\n
    1 - Agregar Peliculas
    2 - Listar peliculas
    3 - Eliminar archivo de peliculas
    4 - Salir 
                        ''')
                opc = int(input('Escribe la opción a realizar (1-4)'))
                if opc == 1:
                    nombre_peli = input('Ingresa el nombre de la pelicula:')
                    pelicula = Pelicula(nombre_peli)
                    self.servicio_peliculas.agregar_pelicula(pelicula)
                elif opc == 2:
                    self.servicio_peliculas.listar_peliculas()
                elif opc == 3:
                    self.servicio_peliculas.eliminar_archivo_peliculas()
                elif opc == 4:
                    print('AdiOs')
                    break
                else:
                    print(f'Opcion invalida')
            except ValueError:
                print('Error: Introduce un número válido')
            except Exception as e:
                print(f'Ocurrio un error: {e}')

app = CatalogoPeliculas()
app.menu_peliculas()