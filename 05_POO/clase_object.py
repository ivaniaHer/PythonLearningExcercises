class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    def __str__(self):
        return f'''
Persona
    Nombre: {self.nombre}
    Apellido: {self.apellido}
    Dir.mem: {super.__str__(self)}'''

persona1 = Persona('Nico', 'Hernandez')
print(persona1)
