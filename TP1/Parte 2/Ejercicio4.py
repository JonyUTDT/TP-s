
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Cargar el archivo CSV
df = pd.read_csv("ejercicio_4.csv", sep=',')

# Defino x e y
X = df['x_vector']
Y = df['y_error']

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
plt.title("Ejercicio 4.a")
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
plt.title("Ejercicio 4.a1")
plt.scatter(X, Y, color='black')
plt.show()

# b)
# No estima bien esto se debe a que tenemos una parabola, lo que hace que una recta no pueda aproximar bien los puntos. Modificariamos platneando 
# un modelo polinomial de grado 2. Ya que con eso obtendriamos una parabola que aproximara a los puntos.

# c)
#Opcion 1: Sacando el b0
# c)
# Armo una funcion para graficar cada punto

for i in range(len(df)):
    plt.scatter(X[i], Y[i], color='black')

# Calcurar Promedios y coeficientes de la recta
promedio_x = np.mean(X)
promedio_y = np.mean(Y)

b1 = np.sum((X - promedio_x) * (Y - promedio_y)) / np.sum((X - promedio_x)**2)

# Calculo la recta que mejor se aproxima a los puntos
plt.plot(X, b1 * (X**2), color='red')
plt.title("Ejercicio 4.a")
plt.scatter(X, Y, color='black')
plt.show()

#Opcion 2: Con el b0
# c)
# Armo una funcion para graficar cada punto

for i in range(len(df)):
    plt.scatter(X[i], Y[i], color='black')

# Calcurar Promedios y coeficientes de la recta
promedio_x = np.mean(X)
promedio_y = np.mean(Y)

b1 = np.sum((X**2 - promedio_x) * (Y - promedio_y)) / np.sum((X**2 - promedio_x)**2)
b0 = promedio_y - b1 * promedio_x

# Calculo la recta que mejor se aproxima a los puntos
plt.plot(X, b0 + b1 * X, color='red')
plt.title("Ejercicio 4.c1")
plt.scatter(X, Y, color='black')
plt.show()

# d)