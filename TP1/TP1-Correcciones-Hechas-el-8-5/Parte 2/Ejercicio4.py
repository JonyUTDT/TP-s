import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Cargar el archivo CSV
df = pd.read_csv("ejercicio_4.csv", sep=',')
matriz = df.to_numpy()

# a)
# Armo una funcion para graficar cada punto
plt.title("Ejercicio 4.a") 
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
# Lo que ocurre es que la recta está alejada de casi todos los puntos, aún siendo beta*. Sucede dado que los puntos forman una parabola, por lo que no es posible que una recta cuya distancia de los puntos sea mínima
# Para que el método funcione, vamos a agregar una columna con los datos al cuadrado

# c)
# Creamos la matriz con las potencias hasta grado 10
X = np.column_stack((np.ones(len(x)), x, x**2))

# Calcular beta* usando la fórmula (X^T X)^(-1) X^T y
beta = np.linalg.inv(X.T @ X) @ X.T @ y

b0, b1, b2 = beta

# Mostrar la recta y los puntos
plt.scatter(x, y, label="Datos", color='black')
plt.plot(x, b0 + b1 * x + b2 * x**2, label=f"Recta: y = {b0:.2f} + {b1:.2f}x", color='red')
plt.xlabel("x")
plt.ylabel("y")
plt.show()

# d)
# Creamos la matriz con las potencias hasta grado 10
X = np.column_stack([x**i for i in range(11)])  # desde x^0 hasta x^10

# Calculamos los coeficientes beta*
beta = np.linalg.inv(X.T @ X) @ X.T @ y

# Evaluamos el polinomio ajustado
y_aprox = X @ beta

# Graficamos los puntos originales y la curva ajustada
plt.title("Ejercicio 4.d - Ajuste polinómico grado 10")
plt.scatter(x, y, label="Datos", color='black')
plt.plot(x, y_aprox, label="Ajuste grado 10", color='green')
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.show()

# Respuestas Teoricas
# Podemos decir que sí, se reduce el error. Esto se debe a que, al ser un polinomio de grado alto, puede ajustarse mejor a los puntos que uno de grado más bajo. 
# En este caso, el polinomio de grado alto es el de grado diez, y el de grado bajo es el de grado dos.
# Sin embargo, aunque parece ajustarse bien a los datos, el polinomio oscila demasiado entre los puntos. Esto se nota en la parábola, que no es una línea "recta", 
# sino que se va "desformando". Este comportamiento es conocido como el efecto Runge.