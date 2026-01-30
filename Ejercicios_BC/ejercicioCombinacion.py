import pandas as pd
import numpy as np

from Ejercicios_BC.ejercicioPandas1 import conteo_genero

df = pd.read_csv('personas.csv')

print(df.info())
print(df.shape)
print(df["pais"].unique())
edades = df["edad"].values
promedio = np.mean(edades)
print(f'Edad mínima: {np.min(edades)}')
print(f'Edad máxima: {np.max(edades)}')
print(f'Desviación estándar: {np.std(edades)}')

# Clasificar por edades
df["grupo_edad"]=np.where(df["edad"]<30,"joven",
                          np.where(df["edad"]<50,"adulto","adulto mayor"))
print(df)

mayores_promedio = df[df["edad"] >promedio]
print(mayores_promedio.head(6))

promedio_por_pais = df.groupby("pais")["edad"].mean()
print(promedio_por_pais)

conteo_genero_1=df["genero"].value_counts()
print(conteo_genero_1)

df.to_csv("personas_analizadas.csv", index=False)