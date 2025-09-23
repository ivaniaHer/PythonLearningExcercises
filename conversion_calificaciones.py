print(f'Bienvenido al sistema de conversión de calificaciones')

nota = float(input('Ingrese la calificación numérica (0-10):'))
letra = None

if 9 <= nota <= 10:
    letra = 'A'
elif 8 <= nota < 9:
    letra = 'B'
elif 7 <= nota < 8:
    letra = 'C'
elif 6<= nota < 7:
    letra = 'D'
elif 0 <= nota < 6:
    letra = 'F'
else:
    letra = 'Valor desconocido'

print(f'La calificación en letra es: {letra}')