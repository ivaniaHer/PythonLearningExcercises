import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Personas por pais
#Usa Numpy para generar: 100 edades aleatorias
edades = np.random.randint(1,100, size=100)
#usa una lista fija de paises
lista_paises = ['Mexico', 'Argentina', 'Colombia','Canada','USA','Guatemala','Honduras','Chile','Peru','Paraguay']
paises_rep = np.tile(lista_paises, 10)
#crea un dataframe con id/pais/edad
df = pd.DataFrame({
    'id': range(1,101),
    'pais':paises_rep,
    'edad':edades
})
#Calcula el promedio de edad por pais
promedio_por_pais = (
    df.groupby('pais', as_index=False)['edad']
      .mean()
      .rename(columns={'edad': 'promedio_edad'})
)
#Grafica el promedio por pais con un gráfico de barras
print(promedio_por_pais)
plt.bar(promedio_por_pais['pais'],promedio_por_pais['promedio_edad'], color = 'pink', edgecolor = 'black')
for i, valor in enumerate(promedio_por_pais['promedio_edad']):
    plt.text(i, valor, f'{valor:.1f}', ha='center', va='bottom')
#Enumerate obtiene la posicion de cada barra, plt.text escribe el valor
plt.xlabel('Países')
plt.ylabel('Promedio de edad')
plt.title('Promedio de edad por países')
plt.xticks(rotation = 30)
plt.show()