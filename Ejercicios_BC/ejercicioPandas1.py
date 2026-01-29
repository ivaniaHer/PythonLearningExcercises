import pandas as pd

datos = pd.read_csv("datos_bc_test.csv")
print(datos.head())
print(datos.info())
print(datos.columns)
print(datos.shape)

mujeres = datos[datos['gender']=="Female"]
hombres = datos[datos['gender']=="Male"]

conteo_genero = datos["gender"].value_counts()
print(mujeres)
print(hombres)
print(conteo_genero)
