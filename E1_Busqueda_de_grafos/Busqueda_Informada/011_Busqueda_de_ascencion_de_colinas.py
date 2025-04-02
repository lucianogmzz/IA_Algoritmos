import heapq  # Para manejar la cola de prioridad
import random  # Para generar valores aleatorios en caso de estancamiento

class Grafo:
    def __init__(self):
        self.nodos = {}
    
    def agregar_nodo(self, nombre, vecinos):
        """
        Agrega un nodo al grafo.
        :param nombre: Nombre del nodo.
        :param vecinos: Diccionario con nodos vecinos y costos.
        """
        self.nodos[nombre] = vecinos
    
    def ascension_colinas(self, inicio, objetivo, heuristica):
        """
        Implementación del algoritmo de Ascensión de Colinas.
        :param inicio: Nodo de inicio.
        :param objetivo: Nodo objetivo.
        :param heuristica: Diccionario con valores heurísticos de cada nodo.
        """
        nodo_actual = inicio
        camino = [nodo_actual]
        
        while nodo_actual != objetivo:
            vecinos = self.nodos[nodo_actual]
            
            if not vecinos:
                return None  # No hay más opciones, se llegó a un óptimo local
            
            # Seleccionar el mejor vecino basado en la heurística
            mejor_vecino = max(vecinos, key=lambda n: heuristica[n])
            
            # Si el mejor vecino no es mejor que el nodo actual, se detiene
            if heuristica[mejor_vecino] <= heuristica[nodo_actual]:
                return camino  # Se alcanzó un óptimo local
            
            nodo_actual = mejor_vecino
            camino.append(nodo_actual)
        
        return camino  # Camino final hacia el objetivo

# Definir un nuevo grafo con distinto acomodo de nodos
grafo = Grafo()
grafo.agregar_nodo("X", {"Y": 3, "Z": 5})
grafo.agregar_nodo("Y", {"X": 3, "W": 2, "V": 4})
grafo.agregar_nodo("Z", {"X": 5, "U": 6})
grafo.agregar_nodo("W", {"Y": 2, "V": 3})
grafo.agregar_nodo("V", {"Y": 4, "W": 3, "U": 7})
grafo.agregar_nodo("U", {"Z": 6, "V": 7})

# Definir nueva heurística (A mayor valor, mejor opción)
heuristica = {"X": 3, "Y": 6, "Z": 5, "W": 4, "V": 7, "U": 9}

# Ejecutar Ascensión de Colinas
camino_hill_climbing = grafo.ascension_colinas("X", "U", heuristica)
print("Camino encontrado con Ascensión de Colinas:", camino_hill_climbing)
