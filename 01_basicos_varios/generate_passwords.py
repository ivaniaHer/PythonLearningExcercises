import bcrypt

# Define las contraseñas que quieres hashear
passwords_to_hash = ['testPasswordNico', 'demoMimi']

# Genera los hashes usando bcrypt
hashed_passwords = []
for pwd in passwords_to_hash:
    hashed = bcrypt.hashpw(pwd.encode('utf-8'), bcrypt.gensalt())
    hashed_passwords.append(hashed.decode('utf-8'))
    print(f'Contraseña: {pwd} -> Hash: {hashed.decode("utf-8")}')