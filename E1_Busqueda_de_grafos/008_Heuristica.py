import heapq  # Cola de prioridad para seleccionar el mejor nodo

class Grafo:
    def __init__(self):
        self.nodos = {}
    
    def agregar_nodo(self, nombre, vecinos):
        """
        Agrega un nodo al grafo.
        :param nombre: Nombre del nodo (clave del diccionario).
        :param vecinos: Diccionario con nodos vecinos y sus costos.
        """
        self.nodos[nombre] = vecinos
    
    def a_estrella(self, inicio, objetivo, heuristica):
        """
        Implementación del algoritmo A*.
        :param inicio: Nodo de inicio.
        :param objetivo: Nodo objetivo.
        :param heuristica: Diccionario con valores heurísticos de cada nodo.
        """
        # Cola de prioridad con formato (costo_total, nodo_actual, camino_recorrido)
        frontera = [(0 + heuristica[inicio], 0, inicio, [inicio])]
        visitados = set()
        
        while frontera:
            _, costo_actual, nodo_actual, camino = heapq.heappop(frontera)  # Extraer el nodo con menor costo estimado
            
            if nodo_actual in visitados:
                continue
            
            visitados.add(nodo_actual)
            
            if nodo_actual == objetivo:
                return camino, costo_actual  # Se encontró el camino óptimo
            
            for vecino, costo in self.nodos[nodo_actual].items():
                if vecino not in visitados:
                    nuevo_costo = costo_actual + costo
                    heapq.heappush(frontera, (nuevo_costo + heuristica[vecino], nuevo_costo, vecino, camino + [vecino]))
        
        return None  # Si no hay camino

# Definir un grafo de ejemplo
grafo = Grafo()
grafo.agregar_nodo("A", {"B": 1, "C": 4})
grafo.agregar_nodo("B", {"A": 1, "D": 2, "E": 5})
grafo.agregar_nodo("C", {"A": 4, "F": 3})
grafo.agregar_nodo("D", {"B": 2, "E": 1})
grafo.agregar_nodo("E", {"B": 5, "D": 1, "F": 2})
grafo.agregar_nodo("F", {"C": 3, "E": 2})

# Definir heurística (valores estimados de cada nodo al objetivo "F")
heuristica = {"A": 7, "B": 6, "C": 2, "D": 3, "E": 1, "F": 0}

# Ejecutar A*
camino, costo = grafo.a_estrella("A", "F", heuristica)
print("Camino óptimo:", camino, "\nCosto total:", costo)
