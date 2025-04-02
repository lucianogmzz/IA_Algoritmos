import random
import numpy as np
from deap import base, creator, tools, algorithms

# 1. Grafo de ejemplo (ciudades con coordenadas)
ciudades = {
    0: (2, 3),  # Ciudad A
    1: (5, 8),  # Ciudad B
    2: (6, 4),  # Ciudad C
    3: (8, 2),  # Ciudad D
    4: (4, 1)   # Ciudad E
}

# 2. Configuración del algoritmo genético
creator.create("FitnessMin", base.Fitness, weights=(-1.0,))  # Minimizar distancia
creator.create("Individual", list, fitness=creator.FitnessMin)

toolbox = base.Toolbox()

# 3. Generación de individuos
toolbox.register("indices", random.sample, range(len(ciudades)), len(ciudades))
toolbox.register("individual", tools.initIterate, creator.Individual, toolbox.indices)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)

# 4. Función de fitness (distancia total)
def calcular_distancia(ruta):
    distancia = 0
    for i in range(len(ruta)):
        ciudad_actual = ciudades[ruta[i]]
        ciudad_siguiente = ciudades[ruta[(i + 1) % len(ruta)]]
        distancia += np.sqrt((ciudad_actual[0] - ciudad_siguiente[0])**2 + 
                     (ciudad_actual[1] - ciudad_siguiente[1])**2)
    return (distancia,)

toolbox.register("evaluate", calcular_distancia)

# 5. Operadores genéticos
toolbox.register("mate", tools.cxOrdered)  # Cruce para permutaciones
toolbox.register("mutate", tools.mutShuffleIndexes, indpb=0.1)
toolbox.register("select", tools.selTournament, tournsize=3)

# 6. Algoritmo principal (sin visualización)
def main():
    pop = toolbox.population(n=50)
    hof = tools.HallOfFame(1)
    
    stats = tools.Statistics(lambda ind: ind.fitness.values)
    stats.register("avg", np.mean)
    stats.register("min", np.min)
    
    pop, log = algorithms.eaSimple(pop, toolbox, cxpb=0.8, mutpb=0.2, 
                                  ngen=50, stats=stats, halloffame=hof, 
                                  verbose=True)
    
    # Mostrar resultados en texto
    print("\n--- Mejor ruta encontrada ---")
    print(f"Ciudades en orden: {hof[0]}")
    print(f"Distancia total: {calcular_distancia(hof[0])[0]:.2f} unidades")
    
    return hof[0]

if __name__ == "__main__":
    mejor_ruta = main()