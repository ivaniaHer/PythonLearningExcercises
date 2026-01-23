from servicio_peliculas import ServicioPeliculas

class CatalogoPeliculas:
    def __init__(self):
        self.servicio_peliculas = ServicioPeliculas()

    def catalogo_peliculas(self):
        salir = False
        print('-------- Catalogo de peliculas ---------')
        self.servicio_peliculas.mostrar_peliculas()
        while not salir:
            try:
                opcion = self.menu_peliculas()
                salir = self.ejecutar_opcion(opcion)
            except Exception as e:
                print(e)

    def ejecutar_opcion(self, opcion):
        if opcion == 1:
            self.servicio_peliculas.mostrar_peliculas()
        elif opcion == 2:
            self.agregar_peliculas()
        elif opcion == 3:
            self.servicio_peliculas.eliminar_archivo_peliculas()
        elif opcion == 4:
            print('Regresa pronto')
            return True
        else:
            print('Opcion Invalida')
        return False

    def agregar_peliculas(self):
        nombre = input('Nombre de la pelicula: ')
        self.servicio_peliculas.agregar_pelicula(nombre)
        print('Pelicula agregada correctamente')

    def menu_peliculas(self):
        print('''
        Menú de peliculas\n
        1 - Listar Peliculas
        2 - Agregar peliculas
        3 - Eliminar archivo de peliculas
        4 - Salir 
        ''')
        return int(input('Elige una opcion'))


catalogo_peliculas = CatalogoPeliculas()
catalogo_peliculas.catalogo_peliculas()