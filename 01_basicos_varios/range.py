
for i in range(0,11,2):
    print(i, end='\t')

print('\n-------------------------------------------')
for i in range(10,20 + 1):
    print(i, end='\t')

print('\n-------------------------------------------')
for i in range(20, 30+1, 2):
    print(i,end='\t')

print('\n-------------------------------------------')
filas = int(input('Ingresa la cantidad de filas a imprimir:'))
for fila in range(1, filas+1):
        print(' '*(filas-fila), '*'*((fila*2)-1))
