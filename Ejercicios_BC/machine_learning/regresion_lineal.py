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


x = np.array([
    [100,3],
    [80,2],
    [120,4],
    [90,2],
    [150,2]
])

precios = np.array([
    60000,
    35000,
    80000,
    40000,
    70000
])

model=LinearRegression()
model.fit(x,precios)
print(f'Interceptor: {model.intercept_}\nPendiente: {model.coef_}')
nueva_casa=np.array([[130,4]])
prediccion = model.predict(nueva_casa)
print(f'Predicción de precio: {prediccion}')
