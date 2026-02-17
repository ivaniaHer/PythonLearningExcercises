from statistics import LinearRegression

import numpy as np
from sklearn.linear_model import LogisticRegression

horas = np.array([[1],[2],[3],[4],[5]])
aprueba = np.array([0,0,0,1,1])

modelo = LogisticRegression()
modelo.fit(horas,aprueba)

probabilidad=modelo.predict_proba([[7]])
prediccion=modelo.predict([[7]])
print(f'Probabilidad es: {probabilidad}\nPredicción es: {prediccion}')
