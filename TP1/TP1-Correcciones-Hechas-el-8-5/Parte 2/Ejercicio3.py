import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Cargar el archivo CSV
df = pd.read_csv("ejercicio_3.csv", sep=',')
matriz = df.to_numpy()

# a)
# Armo una funcion para graficar cada punto
plt.title("Ejercicio 3.a") 
for i in range(len(matriz)):
    plt.scatter(matriz[i][0], matriz[i][1], color='black')

x = matriz[:, 0]
y = matriz[:, 1]

X = np.column_stack((np.ones(len(x)), x))

# Calcular beta* usando la fórmula (X^T X)^(-1) X^T y
beta = np.linalg.inv(X.T @ X) @ X.T @ y

b0, b1 = beta

# Mostrar la recta y los puntos
plt.scatter(x, y, label="Datos", color='black')
plt.plot(x, b0 + b1 * x, label=f"Recta: y = {b0:.2f} + {b1:.2f}x", color='red')
plt.xlabel("x")
plt.ylabel("y")
plt.show()


# b)
# Lo que ocurre es que la recta está alejada de casi todos los puntos, aún siendo beta*. Sucede dado que todas las x son prácticamente iguales.

# Calculo del det(X^t * X)
det = np.linalg.det(X.T @ X)
print(det)
# El determinante es 0, lo que significa que la matriz X no es invertible, por lo que no se puede despejar beta*.

# c)
# La diferencia entre este grafico y los anteriores es que en éste, la recta es casi vertical, y está alejada de muchos de los puntos;
# mientras que en los anteriores, las rectas son crecientes/decrecientes y están muy cerca de la mayoría de los puntos




