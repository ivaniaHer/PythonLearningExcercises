print('-------------------- Agenda de Contactos --------------------')
agenda = {
    'Mimi' : {
        'telefono' : '11223344',
        'email': 'mimi@mail.com',
        'direccion': 'Calle sosa 12F'
    },
    'Monse': {
        'telefono' : '22334455',
        'email': 'monse@mail.com',
        'direccion': 'Pasaje las lomas 89'
    },
    'Lalo': {
        'telefono' : '33445566',
        'email': 'lalo@mail.com',
        'direccion': 'Avenida siempre viva 742'
    }

}

#Imprimir la agenda completa
print(f'Agenda completa:\n{agenda}')
print('----------------------------------------------------------')
#acceder al contacto de mimi
print(f'''Accedemos a la informacion de contacto de Mimi:
    Telefono: {agenda['Mimi']['telefono']}
    Email: {agenda['Mimi']['email']}
    Direccion: {agenda.get('Mimi').get('direccion')}
''')
#Eliminar un contacto existente y agregar uno nuevo
print('----------------------------------------------------------')
print(f'Agenda completa:\n{agenda}')
agenda.pop('Lalo')
agenda['Meu'] = {
    'telefono': '99009900',
    'email': 'meu@mail.com',
    'direccion': 'Pasaje Costa Rica'
}
print(f'Agenda después de eliminar y agregar un elemento:\n{agenda}')
#Mostrar agenda completa

for contacto, detalles in agenda.items():
    print(f'''
    Contacto: {contacto}
    Teléfono: {detalles.get('telefono')}
    Email: {detalles.get('email')}
    Direccion: {detalles.get('direccion')}
''')