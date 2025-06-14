import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Cargar el archivo CSV
df = pd.read_csv("ejercicio_2.csv", sep=',')
matriz = df.to_numpy()

# a)
# Armo una funcion para graficar cada punto
plt.title("Ejercicio 2.a") 
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
# La aproximacion es buena, ya que es la recta más cercana a la mayoría de los puntos
# Pero tenemos un problema con los datos, ya que muchos son negativos, y ni el viento ni el tiempo pueden tomar valores negativos.


