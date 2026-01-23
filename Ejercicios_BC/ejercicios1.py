# Escribe un programa que lea un número e indique si es positivo
print('------- Ejercicio 1 -------')
num = int(input('Ingresa un número: '))
if num >= 0:
    print(f'El número: {num} es positivo')
else:
    print(f'El número: {num} es negativo')

# Pide la edad de una persona y muestra: "Eres mayor de edad" si tiene 18 o más, no mostrar nada si es menor
print('\n------- Ejercicio 2 -------')
age = int(input('Ingresa tu edad: '))
if age >= 18:
    print('Eres mayor de edad')

# Pide un número e indica si es par
print('\n------- Ejercicio 3 -------')
num2= int(input('Ingresa un número: '))
if num2 % 2 == 0:
    print(f'El número {num2} es par')

#Si la temperatura es mayor a 30 grados, muestra: "Hace mucho calor"
print('\n------- Ejercicio 4 -------')
temp = int(input('Ingresa la temperatura: '))
if temp > 30:
    print('Hace mucho calor')

#Pide un número y muestra si es par o impar
print('\n------- Ejercicio 5 -------')

num3= int(input('Ingresa un número: '))
if num3 % 2 == 0:
    print(f'El número {num3} es par')
else:
    print(f'El número {num3} es impar')

