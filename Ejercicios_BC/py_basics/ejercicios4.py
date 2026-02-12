def saludar():
    print('Ola')


def saludar2(name):
    print(f'Hola {name}!!')


saludar()
saludar2('Nico')


def numeros_(inicio, fin):
    lista = []
    print(
        f'Hola! Imprimiré los números primos en los intervalos que indicaste\nEntre {inicio} y {fin} se encuentran los siguientes numeros primos:')
    for numAct in range(inicio, fin):
        if numAct < 2:
            continue
        es_primo = True
        for x in range(2, numAct):
            if numAct % x == 0:
                es_primo = False
                break
        if es_primo:
            lista.append(numAct)
    print(lista)


numeros_(1, 10)


def es_par(num):
    if num % 2 == 0:
        return True
    else:
        return False


print(f'El número 4 es par: {es_par(4)}')


def numeros(n_ini,n_final):
    print(f'Números entre {n_ini} - {n_final}')
    for i in range(n_ini,n_final+1):
        print(i, end=' ')

numeros(4,10)

multiplicar = lambda a,b: a*b
print(multiplicar(2,3))

