import numpy as np  # Para operaciones matemáticas avanzadas
import random        # Para selección aleatoria de estados
import math          # Para funciones matemáticas como exp

def distancia_total(ruta, distancias):
    """
    Calcula la distancia total de una ruta dada la matriz de distancias.
    """
    return sum(distancias[ruta[i]][ruta[i+1]] for i in range(len(ruta)-1)) + distancias[ruta[-1]][ruta[0]]

def vecino(ruta):
    """
    Genera un vecino intercambiando dos ciudades aleatorias en la ruta.
    """
    nueva_ruta = ruta[:]
    i, j = random.sample(range(len(ruta)), 2)
    nueva_ruta[i], nueva_ruta[j] = nueva_ruta[j], nueva_ruta[i]
    return nueva_ruta

def simulated_annealing_tsp(temperatura_inicial, alpha, iteraciones, distancias):
    """
    Implementación del Temple Simulado para el Problema del Viajante (TSP).
    """
    # Inicialización
    T = temperatura_inicial
    num_ciudades = len(distancias)
    ruta_actual = list(range(num_ciudades))
    random.shuffle(ruta_actual)  # Ruta inicial aleatoria
    mejor_ruta = ruta_actual[:]
    mejor_distancia = distancia_total(ruta_actual, distancias)
    
    for _ in range(iteraciones):
        nueva_ruta = vecino(ruta_actual)
        delta_E = distancia_total(nueva_ruta, distancias) - distancia_total(ruta_actual, distancias)
        
        # Criterio de aceptación
        if delta_E < 0 or random.random() < math.exp(-delta_E / T):
            ruta_actual = nueva_ruta[:]
            
            if distancia_total(ruta_actual, distancias) < mejor_distancia:
                mejor_ruta = ruta_actual[:]
                mejor_distancia = distancia_total(ruta_actual, distancias)
        
        # Reducir la temperatura
        T *= alpha
        
        # Condición de paro
        if T < 1e-5:
            break
    
    return mejor_ruta, mejor_distancia

# Parámetros
T_inicial = 1000  # Temperatura inicial alta
alpha = 0.99  # Factor de enfriamiento
iteraciones = 10000  # Número máximo de iteraciones

# Matriz de distancias entre ciudades (simulada)
distancias = np.random.randint(10, 100, size=(5, 5))
np.fill_diagonal(distancias, 0)  # Distancia de una ciudad a sí misma es 0

# Ejecutar el algoritmo
mejor_ruta, mejor_distancia = simulated_annealing_tsp(T_inicial, alpha, iteraciones, distancias)
print(f"Mejor ruta encontrada: {mejor_ruta}, Distancia total: {mejor_distancia}")
