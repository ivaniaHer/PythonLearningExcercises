def generador(maximo):
    contador = 0
    while contador < maximo:
        yield contador
        contador += 1

var_generador = generador(5)

for valor in var_generador:
    print(valor)