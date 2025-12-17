from libro import Libro

class Biblioteca:

    def __init__(self, nombre):
        self._nombre = nombre
        self._libros = []

    @property
    def nombre(self):
        return self._nombre

    @property
    def libros(self):
        return self._libros

    def agregar_libro(self, libro):
        self.libros.append(libro)

    def mostrar_libro(self, libro):
        print(f'Libro => Titulo: {libro.titulo}, Autor: {libro.autor}, Género: {libro.genero}')

    def buscar_libro_por_autor(self, autor):
        print(f'\nLibros del autor: {autor}')
        for libro in self.libros:
            if libro.autor.lower()== autor.lower():
                self.mostrar_libro(libro)

    def buscar_libro_por_genero(self, genero):
        print(f'\nLibros del género: {genero}')
        for libro in self.libros:
            if libro.genero.lower()== genero.lower():
                self.mostrar_libro(libro)

    def mostrar_todos_los_libros(self):
        for libro in self._libros:
            self.mostrar_libro(libro)

