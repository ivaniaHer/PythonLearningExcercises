from monitor import Monitor
from teclado import Teclado
from raton import Raton

class Computadora:

    contador_computadoras = 0

    def __init__(self, nombre, monitor, teclado, raton):
        Computadora.contador_computadoras += 1
        self.id_computadora = Computadora.contador_computadoras
        self.nombre = nombre
        self.monitor = monitor
        self.teclado = teclado
        self.raton = raton

    def __str__(self):
        return f'''
{self.nombre}: {self.id_computadora}
    Monitor: {self.monitor}
    Teclado: {self.teclado}
    Raton: {self.raton}'''

if __name__ == '__main__':
    teclado1 = Teclado('Logitech', 'USB')
    raton1 = Raton('Logitech', 'USB')
    monitor1 = Monitor('Samsung', '27 pulgadas')
    computadora1 = Computadora('HP', monitor1, teclado1, raton1)
    print(computadora1)
    teclado2 = Teclado('Microsoft', 'Bluetooth')
    raton2 = Raton('Microsoft', 'Bluetooth')
    monitor2 = Monitor('LG', '24 pulgadas')
    computadora2 = Computadora('Dell', monitor2, teclado2, raton2)
    print(computadora2)