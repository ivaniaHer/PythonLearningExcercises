class Animal:
    def hacer_sonido(self):
        print('Hago sonido')

class Perro(Animal):
    def hacer_sonido(self):
        print('Puedo ladrar')

class Gato(Animal):
    def hacer_sonido(self):
        print('Puedo maullar')

def hacer_sonido_animal(animal):  # ducktyping
    animal.hacer_sonido()

print('Animal (padre):')
animal1 = Animal()
hacer_sonido_animal(animal1)

print('\nPerro (hijo):')
perro1 = Perro()
hacer_sonido_animal(perro1)

print('\nGato (hijo):')
gato1 = Gato()
hacer_sonido_animal(gato1)