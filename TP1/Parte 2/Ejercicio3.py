
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
    plt.title("Ejercicio 1.a" )    
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
    plt.title("Ejercicio 1.a" )    
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

# c)

v = [X, Y]
v = np.array(v)
v = v.T
v = v.reshape(2, 2)
v = np.linalg.inv(v)
v = np.dot(v, np.array([X, Y]))
v = v.T
np.t()
np.dot(X, Y) / np.dot(X, X)