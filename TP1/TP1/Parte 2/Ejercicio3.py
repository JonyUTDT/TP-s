
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Cargar el archivo CSV
df = pd.read_csv("ejercicio_3.csv", sep=',')

# Defino x e y
X = df['x']
Y = df['y']

#Opcion 1: Sacando el b0
# a)
# Armo una funcion para graficar cada punto

for i in range(len(df)):
    plt.scatter(X[i], Y[i], color='black')

# Calcurar Promedios y coeficientes de la recta
promedio_x = np.mean(X)
promedio_y = np.mean(Y)

b1 = np.sum((X - promedio_x) * (Y - promedio_y)) / np.sum((X - promedio_x)**2)

# Calculo la recta que mejor se aproxima a los puntos
plt.plot(X, b1 * X, color='red')
plt.title("Ejercicio 3.a")
plt.scatter(X, Y, color='black')
plt.show()

#Opcion 2: Con el b0
# a)
# Armo una funcion para graficar cada punto

for i in range(len(df)):
    plt.scatter(X[i], Y[i], color='black')

# Calcurar Promedios y coeficientes de la recta
promedio_x = np.mean(X)
promedio_y = np.mean(Y)

b1 = np.sum((X - promedio_x) * (Y - promedio_y)) / np.sum((X - promedio_x)**2)
b0 = promedio_y - b1 * promedio_x

# Calculo la recta que mejor se aproxima a los puntos
plt.plot(X, b0 + b1 * X, color='red')
plt.title("Ejercicio 3.a1")
plt.scatter(X, Y, color='black')
plt.show()

# b)
# Lo que ocurre es que nos queda la recta ubicada en el x=3 aproximadamente. Sucede dado que todas las x son iguales.

# Calculo del det(X^t * X)
v = [X, Y]
v = np.array(v)
mult = np.dot(v, v.T)
det = np.linalg.det(mult)
print(det)

# c)
# La diferencia entre este grafico y los anteriores es que este es mas como una constante o linea vertical, a diferencia de los anteriores que son crecientes/decrecientes
# permitiendo una linea de tendencia o de regresion con mas sentido.

