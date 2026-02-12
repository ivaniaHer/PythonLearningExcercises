import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#Clasificacion por grupo de edad
#Genera 100 edades aleatorias usando numpy
edades = np.random.randint(1,100, size=100)
#Crea un DataFrame con pandas
df = pd.DataFrame({
    'edad' : edades
})
#Crea una columna grupo_edad con: joven (<30)/ Adulto (30-49)/ Adulto mayor (>50)
df['grupo_edad'] = np.where(
    df['edad'] < 30, 'Joven',
    np.where(df['edad'] < 50, 'Adulto', 'Adulto mayor')
)
#Cuenta cuantas personas hay en cada grupo
personas_por_grupo =  (
    df.groupby('grupo_edad', as_index=False)['edad']
        .count()
        .rename(columns={'edad':'cantidad'})
)
#Grafica el resultado con matplotlib
print(personas_por_grupo)
plt.bar(personas_por_grupo['grupo_edad'],personas_por_grupo['cantidad'], color = 'pink', edgecolor = 'black')
for x, valor in enumerate(personas_por_grupo['cantidad']):
    plt.text(x,valor, f'{valor}',ha='center', va='bottom')
plt.title('Cantidad de personas por grupo de edad')
plt.xlabel('Grupo de edad')
plt.ylabel('Cantidad')
plt.show()
