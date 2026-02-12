# Ejercicio 1 Función que recibe un número y diga si es par o impar
def par_impar(num):
    if num%2==0:
        print(f'{num} es par =D')
    else:
        print(f'{num} es impar =D')

par_impar(2)
par_impar(7)

# Ejercicio 2 Función que calcule el área de un círculo
import math

def area_circulo(radio):
    area = math.pi*(radio ** 2)
    print(f'El área del círculo cuyo radio es {radio} es: {area:.2f}')
    return area

area_circulo(4)

# Ejercicio 3: Función que recibe una lista y devuelva el mayor valor

def valor_max (lista):
    mayor = 0
    for x_value in lista:
        if x_value >= mayor:
            mayor = x_value
    return mayor

lista_valor_max = []
while True:
    x = input(f'Ingresa un elemento para agregar a la lista, escribe "salir" para terminar de añadir: ')
    if x.strip().lower() == 'salir':
        break
    else:
        try:
            num_x= int(x)
            lista_valor_max.append(num_x)
        except Exception as e:
            print(f'Ingresa un valor válido: (numero ó "salir"): {e}')

x_mayor = valor_max(lista_valor_max)
print(f'El valor mayor dentro de la lista es: {x_mayor}\nLista proporcionada: {lista_valor_max}')


# Ejercicio 4: Función que valide una contraseña


def pass_validation(pswrd, conf):
    if conf == pswrd:
        print('Validación correcta')
    else:
        print('Las contraseñas no coinciden')

contraseña = input(f'Ingresa una contraseña:')
validacion = input(f'Repite tu contraseña:')

pass_validation(contraseña,validacion)