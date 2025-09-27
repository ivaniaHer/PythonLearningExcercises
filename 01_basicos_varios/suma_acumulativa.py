numbers = [1,2,3,4,5]
sum_acumulativa = 0
for num in numbers:
    print(f'{sum_acumulativa} + {num} = ', end='')
    sum_acumulativa += num
    print (sum_acumulativa)

print('SEGUNDA SUMA ACUMULATIVA')

num_max = 5
num_ini = 1
sum_acumulativa_2 = 0

while num_ini <= num_max:
    print(f'Suma acumulativa: {sum_acumulativa_2} + {num_ini} = ', end='')
    sum_acumulativa_2 += num_ini
    print(sum_acumulativa_2)
    num_ini+=1