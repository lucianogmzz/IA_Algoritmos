# Luciano Alejandro Gómez Muñoz 22310214 6E2
# Algoritmo: Monte Carlo para Cadenas de Markov (MCMC) - Método de Metropolis-Hastings
# Descripción breve:
# Este código implementa un algoritmo de Monte Carlo para Cadenas de Markov utilizando
# el método de Metropolis-Hastings para realizar muestreo de una distribución.

import numpy as np
import matplotlib.pyplot as plt

# Definimos la distribución objetivo de probabilidad (por ejemplo, una distribución normal)
def target_distribution(x):
    # Esto representa una distribución normal estándar N(0, 1)
    return np.exp(-x**2 / 2) / np.sqrt(2 * np.pi)

# Función de propuesta: generamos un nuevo estado cercano al actual (distribución normal)
def proposal_distribution(x):
    # Propuesta normal centrada en el estado actual
    return np.random.normal(x, 0.5)

# Algoritmo de Metropolis-Hastings
def metropolis_hastings(num_samples, initial_state):
    # Inicializamos la cadena con el estado inicial
    x = initial_state
    samples = []
    
    for _ in range(num_samples):
        # Proponer un nuevo estado
        x_new = proposal_distribution(x)
        
        # Calcular las probabilidades de aceptación
        acceptance_ratio = min(1, target_distribution(x_new) / target_distribution(x))
        
        # Aceptar o rechazar el nuevo estado
        if np.random.rand() < acceptance_ratio:
            x = x_new  # Aceptamos el nuevo estado
        
        # Almacenamos el estado actual en la cadena
        samples.append(x)
    
    return np.array(samples)

# Parámetros
num_samples = 10000  # Número de muestras a generar
initial_state = 0    # Estado inicial de la cadena

# Generamos muestras usando MCMC (Método de Metropolis-Hastings)
samples = metropolis_hastings(num_samples, initial_state)

# Graficamos las muestras generadas
plt.hist(samples, bins=50, density=True, alpha=0.6, color='g')
# Graficamos la distribución objetivo
x_vals = np.linspace(-5, 5, 1000)
plt.plot(x_vals, target_distribution(x_vals), 'r', label='Distribución objetivo')
plt.title("Muestreo por Metropolis-Hastings")
plt.xlabel("Valor")
plt.ylabel("Densidad de probabilidad")
plt.legend()
plt.show()

