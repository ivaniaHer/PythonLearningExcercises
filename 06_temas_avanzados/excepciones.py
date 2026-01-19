def dividir(numerador, denominador):
    try:
        if denominador == 0:
            raise Exception('El denominador no puede ser igual a cero')
        resultado = numerador / denominador
        print(f'Resultado: {resultado}')
    except Exception as e:
        print(f'Ocurrió un error: {e}')
    else:
        print(f'No ocurrió ningún error')
    finally:
        print(f'Se terminó de procesar la operación\n')

dividir(10,2)
dividir(10,0)