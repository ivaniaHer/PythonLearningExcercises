# Añadir otra columna
import pandas as pd

datos = pd.read_csv("datos_bc_test.csv")
datos["country"]=['Guatemala','Mexico','China','Canada','USA','Argentina','Spain','Andorra','Puerto Rico', 'Croatia','Guatemala','Mexico','China','Canada','USA','Argentina','Spain','Andorra','Puerto Rico', 'Croatia']
datos["salary"]=[444,555,666,333,455,664,223,566,885,323,568,323,567,234,234,234,754,435,345,653]
# Crea una nueva columna basada en otra
datos["anual_salary"]=datos["salary"]*12
# Incrementa todos los valores de una columna en un porcentaje
datos["salary"] = datos["salary"] * 1.10 # Aumentamos el salario en el 10%
# Cambia el nombre de una columna
renaming_column=datos.rename(columns={"first_name": "name"})
print(f'\nCAMBIANDO NOMBRE DE COLUMNA (first_name to name):\n{renaming_column.columns}')
# Elimina una columna que no sea necesaria
gender_drop = renaming_column.drop(columns=["gender"])
print(f'ELIMINANDO COLUMNA "Gender"\n{gender_drop.columns}')

# Ordena el DataFrame por una columna específico
datos_sorted_by_anual_salary=gender_drop.sort_values(by="anual_salary", ascending=False)

print(f'\nDATA INICIAL:\n{datos.head(6)}')
print(f'\nDATA MODIFICADA: \n{datos_sorted_by_anual_salary.head(6)}')
#datos_sorted_by_anual_salary.to_csv("datos_actualizados.csv", index=False)
