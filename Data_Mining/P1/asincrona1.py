import numpy as np
import statistics as st
from scipy import stats

datos = [5, 6, 3, 34, 5, 23, 6, 7, 8, 6, 56, 5]
# Calcular media aritmética
media = np.mean(datos)
print(f"Media Aritmética: {media}")

# Calcular mediana
mediana = st.median(datos)
print(f'Mediana: {mediana}')

# Calcular moda
moda = st.mode(datos)
print(f'Moda: {moda}')

# Multimodal
multimodal = st.multimode(datos)
print(f'Multimodal: {multimodal}')

# Desviación típica poblacional
desv_tipica_p = st.pstdev(datos)
print(f'Desviación típica poblacional: {desv_tipica_p}')

# Varianza muestral
varianza = st.variance(datos)
print(f'Varianza muestral: {varianza}')

# Correlación de Pearson
x = [1,2,3,4,5]
y= [1,2,3,3,5]
corr=np.corrcoef(x,y)[0,1]
print(f'Correlación de Pearson: {corr}')

# Covarianza
x=[1,2,3,4,5]
y=[5,4,3,2,1]
covarianza = np.cov(x,y)[0,1]
print(f'Covarianza: {covarianza}')

# Asimetría
asimetria = stats.skew(datos)
print(f"Asimetría: {asimetria}")

# Error estándar de la media
sem = stats.sem(datos)
print(f'Error estándar de la media: {sem}')

