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

# Pide una nota y muestra "Aprobado" si la nota es mayor o igual a 60, "Reprobado" en caso contrario
print('\n------- Ejercicio 6 -------')
grade = int(input('Ingresa una nota: '))
if grade >= 60:
    print('Aprobado')
else:
    print('Reprobado')

#Pide la edad y muestra "Acceso permitido" si tiene 18 o más, y denegado si es menor
print('\n------- Ejercicio 7 -------')
edad7 = int(input('Ingresa tu edad: '))
if edad7 >= 18:
    print('Acceso permitido')
else:
    print('Acceso denegado')

#Define una contraseña fija y pide al usuario que ingrese una. Muestra si es correcta o incorrecta
print('\n------- Ejercicio 8 -------')
PASS='elote123'
pass_user = input('Ingresa la contraseña: ')
if pass_user == PASS:
    print('Contraseña correcta')
else:
    print('Contraseña Incorrecta')

# Pide una nota y clasifica: 90 o más = excelente, 60 a 89 = aprobado, menor a 60 = reprobado
print('\n------- Ejercicio 9 -------')
nota9 = int(input('Ingresa la nota a clasificar: '))
if nota9>= 90:
    print('Excelente')
elif 60 <= nota9 <= 89:
    print('Aprobado')
elif nota9<60:
    print('Reprobado')
else:
    print('Valor inválido')

#Pide un número del 1 al 7 y muestra el dia correspondiente cuando 1=lunes, 2=martes etc
print('\n------- Ejercicio 10 -------')
day_num = int(input('Ingresa un numero para indicar el día: '))

match day_num:
    case 1:
        print('Lunes')
    case 2:
        print('Martes')
    case 3:
        print('Miércoles')
    case 4:
        print('Jueves')
    case 5:
        print('Viernes')
    case 6:
        print('Sábado')
    case 7:
        print('Domingo')
    case _:
        print('Número inválido')