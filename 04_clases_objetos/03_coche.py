class Coche:

    def __init__(self, marca, modelo, color):
        self._marca = marca
        self._modelo = modelo
        self._color = color

    def conducir(self):
        print(f'''
    Conduciendo el coche:
        Marca: {self._marca}
        Modelo: {self._modelo}
        Color: {self._color}''')

    # def get_marca(self):
    #     return self._marca

    @property #define un getter
    def marca(self):
        return self._marca

    @marca.setter #define un setter
    def marca(self, marca):
        self._marca = marca

    @property
    def modelo(self):
        return self._modelo

    @modelo.setter
    def modelo(self, modelo):
        self._modelo = modelo

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, color):
        self._color = color

if __name__ == '__main__':
    coche1= Coche('Mazda','Miata','Rojo')
    coche1.conducir()
    coche1.marca = 'Mazda2'
    coche1.modelo = 'Miata 2'
    coche1.color = 'Azul'
    coche1.conducir()

    #agregar un nuevo atributo
    setattr(coche1, 'Año', 2020)
    print(coche1.Año)

    #mostrar los atributos del objeto
    print(f'Atributos del coche1: {coche1.__dict__}')
