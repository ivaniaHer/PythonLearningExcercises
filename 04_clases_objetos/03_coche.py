class Coche:

    def __init__(self, marca, modelo, color):
        self.marca = marca
        self._modelo = modelo
        self.__color = color

    def conducir(self):
        print(f'Conduciendo el coche:\nMarca: {self.marca}\nModelo: {self._modelo}\nColor: {self.__color}')

if __name__ == '__main__':
    coche1= Coche('Mazda','Miata','Rojo')
    coche1.conducir()
    coche1.marca = 'Mazda'
    coche1._