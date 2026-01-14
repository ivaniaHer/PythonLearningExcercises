class Animal:
    def comer(self):
        print('Como muchas veces al día')
    def dormir(self):
        print('Duermo muchas horas al día')

class Perro(Animal):
    def hacer_sonido(self):
        print('Puedo ladrar')
    # Sobrescribimos el method dormir
    def dormir(self):
        print('Duermo 15 horas al día')

print('Clase padre, Animal:')
animal1 = Animal()
animal1.comer()
animal1.dormir()
print('\nClase hija, Perro:')
perro1 = Perro()
perro1.comer()
perro1.dormir()
perro1.hacer_sonido()