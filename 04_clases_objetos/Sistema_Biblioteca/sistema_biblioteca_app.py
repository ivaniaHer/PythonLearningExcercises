print('------------ Sistema de Biblioteca ------------')

from biblioteca import Biblioteca
from libro import Libro

biblioteca1 = Biblioteca('Internacional Library')

# agregar libros
libro1 = Libro('Pachinko', 'Min Jin Lee', 'Novela')
libro2 = Libro('1984', 'George Orwell', 'Ciencia Ficción')
libro3 = Libro('Pet Sematary', 'Stephen King', 'Terror')
libro4 = Libro('The Shining', 'Stephen King', 'Terror')
libro5 = Libro('To Kill a Mockingbird', 'Harper Lee', 'Novela')

# agregar libros a la biblioteca

biblioteca1.agregar_libro(libro1)
biblioteca1.agregar_libro(libro2)
biblioteca1.agregar_libro(libro3)
biblioteca1.agregar_libro(libro4)
biblioteca1.agregar_libro(libro5)


biblioteca1.mostrar_todos_los_libros()
biblioteca1.buscar_libro_por_autor("Stephen King")
biblioteca1.buscar_libro_por_genero("Novela")