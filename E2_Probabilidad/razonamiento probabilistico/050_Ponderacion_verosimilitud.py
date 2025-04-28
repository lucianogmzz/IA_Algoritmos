# Luciano Alejandro Gómez Muñoz 22310214 6E2
# Algoritmo: Ponderación de Verosimilitud
# Descripción breve:
# Este código implementa la ponderación de verosimilitud para ajustar un modelo
# de regresión lineal mediante un enfoque probabilístico. Las observaciones
# son ponderadas según su verosimilitud bajo el modelo de regresión.

import numpy as np
import matplotlib.pyplot as plt

# Generar datos simulados
np.random.seed(0)
n = 100  # Número de muestras
x = np.linspace(0, 10, n)  # Características (por ejemplo, tiempo)
y_true = 2 * x + 1  # Modelo verdadero (pendiente = 2, intercepto = 1)
y = y_true + np.random.normal(0, 1, n)  # Datos con ruido

# Función de verosimilitud para un modelo lineal (asumiendo normalidad en los errores)
def likelihood(y, x, theta0, theta1):
    # La verosimilitud se calcula como la probabilidad de observar los datos bajo el modelo
    predictions = theta0 + theta1 * x  # Predicciones del modelo
    residuals = y - predictions  # Residuos
    # Se asume una distribución normal para los errores
    sigma = 1  # Desviación estándar de los errores
    return np.exp(-0.5 * (residuals**2 / sigma**2)) / (sigma * np.sqrt(2 * np.pi))

# Función de ponderación de verosimilitud
def weighted_regression(x, y):
    # Inicializamos los parámetros (intercepto y pendiente) del modelo
    theta0, theta1 = 0, 0
    # Número de muestras
    n = len(x)
    # Establecer las ponderaciones de las muestras basadas en su verosimilitud
    weights = likelihood(y, x, theta0, theta1)
    
    # Ajuste del modelo utilizando ponderación de verosimilitud
    # Usamos un enfoque simple de minimización de la suma ponderada de los residuos
    weighted_sum_x = np.sum(weights * x)
    weighted_sum_y = np.sum(weights * y)
    weighted_sum_xx = np.sum(weights * x * x)
    weighted_sum_xy = np.sum(weights * x * y)
    
    # Calcular los nuevos parámetros ponderados (intercepto y pendiente)
    theta1_new = (weighted_sum_xy - weighted_sum_x * weighted_sum_y / weighted_sum_xx) / (weighted_sum_xx - weighted_sum_x**2 / weighted_sum_xx)
    theta0_new = weighted_sum_y / weighted_sum_xx - theta1_new * weighted_sum_x / weighted_sum_xx
    
    return theta0_new, theta1_new

# Realizar la regresión ponderada por verosimilitud
theta0_est, theta1_est = weighted_regression(x, y)

# Mostrar los resultados
print(f"Estimación del intercepto: {theta0_est}")
print(f"Estimación de la pendiente: {theta1_est}")

# Graficar los datos y la línea de regresión ajustada
plt.scatter(x, y, label='Datos observados')
plt.plot(x, theta0_est + theta1_est * x, color='red', label='Modelo ajustado')
plt.title("Regresión ponderada por verosimilitud")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.show()
