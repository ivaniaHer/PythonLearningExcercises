from random import randint

random_number = randint(1, 50)
intentos = 0
num = None
while num != random_number:
    num = int(input('Adivina el número entre 1 y 50:'))
    intentos += 1
    if num > random_number:
        print('El número secreto es menor. Intenta de nuevo.')
    elif num < random_number:
        print('El número secreto es mayor. Intenta de nuevo.')
    else:
        print(f'¡Felicidades! Has adivinado el número {random_number} en {intentos} intentos.')