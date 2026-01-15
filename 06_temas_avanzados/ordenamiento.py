# sintaxis sorted(iterable, key=None, reverse=False)

empleados = ['Pedro', 'Nara', 'Juan']

empleado_ordenados = sorted(empleados, reverse=True)
print(empleado_ordenados)

empleados_dict = [
    {'nombre': 'Juan', 'salario': 3000},
    {'nombre': 'Nara', 'salario': 3500},
    {'nombre': 'Pedro', 'salario': 2500}
]
empleados_ordenados_salario = sorted(empleados_dict, key=lambda x: x['salario'])
print(empleados_dict)
print(empleados_ordenados_salario)