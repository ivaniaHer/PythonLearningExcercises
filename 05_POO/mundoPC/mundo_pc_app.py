print('-------- Mundo PC --------')

from computadora import Computadora
from monitor import Monitor
from teclado import Teclado
from raton import Raton
from orden import Orden

teclado1 = Teclado('Dell', 'USB')
raton1 = Raton('Logitech', 'Bluetooth')
monitor1 = Monitor('Samsung', '23 pulgadas')
computadora1 = Computadora('DELL', monitor1, teclado1, raton1)

teclado2 = Teclado('Microsoft', 'Bluetooth')
raton2 = Raton('Microsoft', 'Bluetooth')
monitor2 = Monitor('LG', '24 pulgadas')
computadora2 = Computadora('ASUS', monitor2, teclado2, raton2)

computadora3 = Computadora('Ryzen', monitor1, teclado2, raton1)

computadoras1 = [computadora1, computadora2]


orden1 = Orden(computadoras1)
orden1.agregar_computadora(computadora3)
print(orden1)