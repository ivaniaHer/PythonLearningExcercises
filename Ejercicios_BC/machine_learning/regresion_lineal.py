import numpy as np
from sklearn.linear_model import LinearRegression

horas = np.array([[1],[2],[3],[4],[5]])
notas = np.array([[5],[6],[7],[8],[9]])

#modelo
modelo = LinearRegression()
modelo.fit(horas, notas)

nueva_prediccion = modelo.predict([[6]])
print(f'Interceptor: {modelo.intercept_}')
print(f'Pendiente: {modelo.coef_}')
print(f'Nota predicha para 6 horas: {nueva_prediccion}')