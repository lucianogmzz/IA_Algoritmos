# Luciano Alejandro Gómez Muñoz - 22310214
# Algoritmo Genético para resolver el Problema del Viajero (TSP)
# ---------------------------------------------------------------
# Este código encuentra una ruta de recorrido mínimo entre ciudades dadas en coordenadas 2D.
# Utiliza la biblioteca DEAP para definir individuos, operadores genéticos y evolución.

import random           # Librería estándar para operaciones aleatorias (cruces, mutaciones, etc.)
import numpy as np      # Librería para cálculos numéricos como raíz cuadrada y estadísticas
from deap import base, creator, tools, algorithms  # Módulos de DEAP para construir algoritmos

# ------------------------
# 1. Definición del grafo
# ------------------------

# Diccionario que representa las ciudades y sus coordenadas (x, y)
ciudades = {
    0: (2, 3),  # Ciudad A
    1: (5, 8),  # Ciudad B
    2: (6, 4),  # Ciudad C
    3: (8, 2),  # Ciudad D
    4: (4, 1)   # Ciudad E
}

# -----------------------------------------------
# 2. Configuración de la estructura evolutiva DEAP
# -----------------------------------------------

# Se define el tipo de fitness: queremos minimizar (por eso el peso es -1.0)
creator.create("FitnessMin", base.Fitness, weights=(-1.0,))

# Se define un individuo como una lista con este tipo de fitness
creator.create("Individual", list, fitness=creator.FitnessMin)

# Se crea una caja de herramientas para registrar funciones que usará el AG
toolbox = base.Toolbox()

# -------------------------------------
# 3. Registro de generación de individuos
# -------------------------------------

# Se registra una función para generar una permutación aleatoria de los índices de ciudades
toolbox.register("indices", random.sample, range(len(ciudades)), len(ciudades))

# Se define cómo construir un individuo: se usa la permutación como genoma
toolbox.register("individual", tools.initIterate, creator.Individual, toolbox.indices)

# Se define cómo construir una población: una lista de individuos
toolbox.register("population", tools.initRepeat, list, toolbox.individual)

# ---------------------------------------
# 4. Definición de la función de evaluación
# ---------------------------------------

def calcular_distancia(ruta):
    """
    Calcula la distancia total de una ruta (ciclo completo).
    La distancia entre ciudades es euclidiana.
    """
    distancia = 0  # Acumulador de distancia total
    for i in range(len(ruta)):
        ciudad_actual = ciudades[ruta[i]]  # Coordenadas de la ciudad actual
        ciudad_siguiente = ciudades[ruta[(i + 1) % len(ruta)]]  # La siguiente, con vuelta al inicio
        # Distancia euclidiana entre dos puntos
        distancia += np.sqrt((ciudad_actual[0] - ciudad_siguiente[0])**2 +
                             (ciudad_actual[1] - ciudad_siguiente[1])**2)
    return (distancia,)  # DEAP requiere que sea una tupla

# Registro de la función de evaluación en la toolbox
toolbox.register("evaluate", calcular_distancia)

# -------------------------
# 5. Operadores genéticos
# -------------------------

# Cruce ordenado: mantiene la validez de las permutaciones
toolbox.register("mate", tools.cxOrdered)

# Mutación por intercambio aleatorio de índices (permuta algunas posiciones)
toolbox.register("mutate", tools.mutShuffleIndexes, indpb=0.1)

# Selección por torneo: elige los mejores entre varios candidatos
toolbox.register("select", tools.selTournament, tournsize=3)

# ---------------------------
# 6. Ejecución del algoritmo
# ---------------------------

def main():
    # Se crea la población inicial de 50 individuos
    pop = toolbox.population(n=50)

    # Hall of Fame: almacena el mejor individuo de toda la evolución
    hof = tools.HallOfFame(1)

    # Estadísticas para monitorear evolución
    stats = tools.Statistics(lambda ind: ind.fitness.values)
    stats.register("avg", np.mean)  # Promedio de las distancias
    stats.register("min", np.min)   # Mejor distancia

    # Se ejecuta el algoritmo evolutivo (generaciones simples)
    pop, log = algorithms.eaSimple(
        pop,                # Población inicial
        toolbox,            # Caja de herramientas con operadores
        cxpb=0.8,           # Probabilidad de cruce
        mutpb=0.2,          # Probabilidad de mutación
        ngen=50,            # Número de generaciones
        stats=stats,        # Objeto de estadísticas
        halloffame=hof,     # Guarda el mejor individuo
        verbose=True        # Imprime información en consola
    )

    # Resultados
    print("\n--- Mejor ruta encontrada ---")
    print(f"Ciudades en orden: {hof[0]}")  # El orden óptimo hallado
    print(f"Distancia total: {calcular_distancia(hof[0])[0]:.2f} unidades")  # Distancia asociada

    return hof[0]  # Retorna la mejor ruta

# Punto de entrada del programa
if __name__ == "__main__":
    mejor_ruta = main()  # Ejecuta todo
