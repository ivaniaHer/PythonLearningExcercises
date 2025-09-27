password = ""

while len(password) < 6:
    password = input('Ingresa una contraseña (mínimo 6 caracteres): ')
    if len(password) < 6:
        print('Contraseña demasiado corta. Inténtalo de nuevo.')