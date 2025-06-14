
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Cargar el archivo CSV
df = pd.read_csv("ejercicio_2.csv", sep=',')

# Defino x e y
x = df['X']
y = df[' Y']

# a)
# Armo una funcion para graficar cada punto

for i in range(len(df)):
    plt.scatter(x[i], y[i], color='black')


# Calcurar Promedios y coeficientes de la recta
promedio_x = np.mean(x)
promedio_y = np.mean(y)

b1 = np.sum((x - promedio_x) * (y - promedio_y)) / np.sum((x - promedio_x)**2)
b0 = promedio_y - b1 * promedio_x

# Calculo la recta que mejor se aproxima a los puntos
plt.plot(x, b0 + b1 * x, color='red')
plt.title("Ejercicio 2.a")
plt.scatter(x, y, color='black')
plt.show()

# b)
# La aproximacion es buena, pero tenemos un problema con los datos. Tenemos datos negativos y ni el viento ni el tiempo pueden tomar valores negativos.
# Por lo tanto, la aproximacion no es buena.

