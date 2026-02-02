import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#Generación básica de datos
#Usa Numpy para generar 100 edades aleatorias entre 18 y 65 edades
edades = np.random.randint(18,65,size=100)
#Guarda las edades en un DataFrame de pandas
df_edades = pd.DataFrame(edades, columns=['Edades'])
#Calcula: Promedio/edad mínima/edad máxima
edad_promedio = df_edades.mean()
edad_minima = df_edades.min()
edad_maxima = df_edades.max()
print(f'Edad promedio: {edad_promedio}\nEdad minima: {edad_minima}\nEdad máxima{edad_maxima}')
#Muestra un histograma de las edades usando matplotlib
plt.hist(edades,bins=30,color='pink')
plt.title('Histograma de edades')
plt.xlabel('Edad')
plt.ylabel('Frecuencia')
plt.show()