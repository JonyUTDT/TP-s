import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Cargar el archivo CSV
df = pd.read_csv("ejercicio_1.csv", sep=',')
matriz = df.to_numpy()

# a)
# Armo una funcion para graficar cada punto
plt.title("Ejercicio 1.a" ) 
for i in range(len(matriz)):
    plt.scatter(matriz[i][0], matriz[i][1], color='black')
plt.show()

# b)
#β* = (X^T . X)^−1 . (X)^T . y

x = matriz[:, 0]
y = matriz[:, 1]

X = np.column_stack((np.ones(len(x)), x))

# Calcular beta* usando la fórmula (X^T X)^(-1) X^T y
beta = np.linalg.inv(X.T @ X) @ X.T @ y

b0, b1 = beta

# Mostrar la recta y los puntos
plt.scatter(x, y, label="Datos", color='black')
plt.plot(x, b0 + b1 * x, label=f"Recta: y = {b0:.2f} + {b1:.2f}x", color='red')
plt.title("Ejercicio 1.b")
plt.xlabel("x")
plt.ylabel("y")
plt.show()


# c)
df = pd.read_csv("ejercicio_1.csv", sep=',')
matriz = df.to_numpy()

# c.a)
# Armo una funcion para graficar cada punto
plt.title("Ejercicio 1.c.a" ) 
for i in range(len(matriz)):
    plt.scatter(matriz[i][0], matriz[i][1]+12, color='black')

# c.b)
x = matriz[:, 0]
y = matriz[:, 1]
for i in range(len(y)):
    y[i]+=12
X = np.column_stack((np.ones(len(x)), x))

# Calcular beta* usando la fórmula (X^T X)^(-1) X^T y
beta = np.linalg.inv(X.T @ X) @ X.T @ y

# Recta estimada: y = b0 + b1 * x
b0, b1 = beta

# Mostrar la recta y los puntos
plt.scatter(x, y, label="Datos", color='black')
plt.plot(x, b0 + b1 * x, label=f"Recta: y = {b0:.2f} + {b1:.2f}x", color='red')
plt.title("Ejercicio 1.c.b")
plt.xlabel("x")
plt.ylabel("y")
plt.show()

# La aproximación es buena, ya que la recta se ajusta a los puntos modificados y es la más cercana a la mayoría de los puntos.
# El problema es que cambió b0 y b1 no, lo que significa que b0 se ve afectado por el cambio en y, cuando no debería ser así ya que beta es fijo. 

# d)
# Calculando lo siguiente:
# Crear la matriz X con una columna de unos para b0 y una columna con los valores de x para b1
# Y calculando beta* = (X^T X)^(-1) X^T y

