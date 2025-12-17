class Persona:
    contador_personas = 0 #Atributo de clase

    #metodo constructor
    def __init__(self, nombre, apellido):
        Persona.contador_personas += 1
        self.id = Persona.contador_personas
        self.nombre = nombre
        self.apellido = apellido

    def mostrar_persona(self):
        print(f'ID: {self.id}, Nombre: {self.nombre}, Apellido: {self.apellido}')

    @staticmethod
    def get_contador_personas_estatico():
        print("Método estatico")
        return Persona.contador_personas

    @classmethod
    def get_contador_personas_clase(cls):
        print("Método de clase")
        return cls.contador_personas

if __name__ == '__main__':
    persona1 = Persona('Nicole', 'Hernandez')
    persona2 = Persona('Juan', 'Perez')
    persona1.mostrar_persona()
    persona2.mostrar_persona()

    print(f'Contador de objetos persona: {Persona.contador_personas}')
    print(f'Contador de objetos persona (static): {Persona.get_contador_personas_estatico()}')
    print(f'Contador de objetos persona (class): {Persona.get_contador_personas_clase()}')
