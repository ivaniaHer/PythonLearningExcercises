# definiendo una clase

class Persona:

    def __init__(self, nombre, apellido):
        #atributos de clase
        self.nombre = nombre
        self.apellido = apellido

    def mostrar_persona(self):
        print(f''' Persona: 
        Nombre: {self.nombre}
        Apellido: {self.apellido}
        ''')
# creando un objeto

if __name__ == '__main__':
    persona1 = Persona('Nico','Hernandez')
    persona1.mostrar_persona()
    print(f'Dirección de memoria de persona1: {id(persona1)}\n')
    print(f'Direccion de memoria hexadecimal de persona1: {hex(id(persona1))}\n')

    persona2 = Persona('Ana','Gomez')
    persona2.mostrar_persona()