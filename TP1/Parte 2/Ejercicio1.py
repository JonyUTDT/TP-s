
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Cargar el archivo CSV
df = pd.read_csv("ejercicio_1.csv", sep=',')

# Defino x e y
x = df['X']
y = df[' Y']

# a)
# Armo una funcion para graficar cada punto

for i in range(len(df)):
    plt.title("Ejercicio 1.a" )    
    plt.scatter(x[i], y[i], color='black')
plt.show()

# b)
# Calcurar Promedios y coeficientes de la recta
promedio_x = np.mean(x)
promedio_y = np.mean(y)

b1 = np.sum((x - promedio_x) * (y - promedio_y)) / np.sum((x - promedio_x)**2)
b0 = promedio_y - b1 * promedio_x

# Calculo la recta que mejor se aproxima a los puntos
plt.plot(x, b0 + b1 * x, color='red')
plt.title("Ejercicio 1.b")
plt.scatter(x, y, color='black')
plt.show()

# c)

# c. a)
# Armo una funcion para graficar cada punto

for i in range(len(df)):
    plt.title("Ejercicio 1.c.a" )    
    plt.scatter(x[i], (y[i] + 12), color='black')
plt.show()

# c. b)
# Calcurar Promedios y coeficientes de la recta
promedio_x = np.mean(x)
promedio_y = np.mean(y + 12)

b1 = np.sum((x - promedio_x) * ((y + 12)  - promedio_y)) / np.sum((x - promedio_x)**2)
b0 = promedio_y - b1 * promedio_x

# Calculo la recta que mejor se aproxima a los puntos
plt.plot(x, b0 + b1 * x, color='red')
plt.title("Ejercicio 1.c.b")
plt.scatter(x, (y + 12), color='black')
plt.show()

# Rsta
# No es una buena aproximacion, ya que los datos originales fueron alterados. Les sumamos 12 a todas las Y y las X las mantuvimos iguales.

# d)
# Calculando lo siguiente:
# b1 = np.sum((x - promedio_x) * (y - promedio_y)) / np.sum((x - promedio_x)**2)
# b0 = promedio_y - b1 * promedio_x
# Y haciendo la recta:
# m(x) = b0 + b1 * x