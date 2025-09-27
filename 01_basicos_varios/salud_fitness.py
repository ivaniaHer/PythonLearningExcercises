print('****** Aplicación de Salud y Fitness *****')

### CONSTANTES
META_PASOS_DIARIOS = 10000
CALORIAS_POR_PASO = 0.04

nombre = input('Ingrese su nombre: ').strip()
pasos_diarios = int(input('Ingrese el número de pasos caminados hoy: '))

calorias_quemadas = pasos_diarios * CALORIAS_POR_PASO

cumplio_meta = 'Si' if pasos_diarios > META_PASOS_DIARIOS else 'No'

print(f'\nHola {nombre},')
print(f'Has caminado {pasos_diarios} pasos hoy.')
print(f'Has quemado aproximadamente {calorias_quemadas:.2f} calorías.')
print(f'¿Cumpliste tu meta diaria de {META_PASOS_DIARIOS} pasos? {cumplio_meta}')