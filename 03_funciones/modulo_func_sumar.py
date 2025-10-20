def sumar(a,b):
    resultado = a + b
    return resultado
print(__name__)

def es_par(numero):
    if numero % 2 == 0:
        return True
    else :
        return False

if __name__ == '__main__':
    print(f"Funcion sumar desde el módulo: {sumar(8,398)}")