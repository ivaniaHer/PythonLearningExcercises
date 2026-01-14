nombres = ['Nico', 'Meu', 'Lola']
edades = [25, 90, 19]
ciudades = ['London', 'Madrid', 'Paris']

combinados = zip(nombres, edades, ciudades)
print(combinados)
for item in combinados:
    print(item)