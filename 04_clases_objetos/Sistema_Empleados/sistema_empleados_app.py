from empresa import Empresa
from empleado import Empleado

print('Sistema de empleados')
empresa1 = Empresa('Tech Solutions')

#contratar empleados

empresa1.contratar_empleado('Nico', 'IT')
empresa1.contratar_empleado('Pablo', 'Marketing')
empresa1.contratar_empleado('Lauren', 'Ventas')
empresa1.contratar_empleado('Ana', 'IT')

#obtener total de empleados
print(f'Total de empleados: {Empleado.obtener_total_empleados()}')

#obtener numero de empleados en el departamento de IT

print(f'Empleados en IT: {empresa1.obtener_numero_empleados_departamento('IT')}')

#mostrar todos los empleados de la empresa

empresa1.obtener_numero_empleados_empresa()