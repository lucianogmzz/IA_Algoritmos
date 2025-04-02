import heapq  # Para manejar la cola de prioridad

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
    
    def a_estrella(self, inicio, objetivo, heuristica):
        """
        Implementación del algoritmo A*.
        :param inicio: Nodo de inicio.
        :param objetivo: Nodo objetivo.
        :param heuristica: Diccionario con valores heurísticos de cada nodo.
        """
        frontera = [(0 + heuristica[inicio], 0, inicio, [inicio])]  # (costo total estimado, costo real, nodo, camino recorrido)
        visitados = set()
        
        while frontera:
            _, costo_actual, nodo_actual, camino = heapq.heappop(frontera)  # Extrae el nodo con menor f(n)
            
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
    
    def ao_estrella(self, inicio, objetivo, heuristica):
        """
        Implementación del algoritmo AO* (And-Or Graph Search).
        :param inicio: Nodo de inicio.
        :param objetivo: Nodo objetivo.
        :param heuristica: Diccionario con valores heurísticos de cada nodo.
        """
        frontera = [(heuristica[inicio], inicio, [inicio])]  # (heurística, nodo actual, camino recorrido)
        solucion = {}  # Almacena las soluciones parciales
        
        while frontera:
            _, nodo_actual, camino = heapq.heappop(frontera)  # Extrae el nodo con menor heurística
            
            if nodo_actual == objetivo:
                solucion[nodo_actual] = camino  # Marca el nodo como resuelto
                return camino  # Se encontró una solución
            
            if nodo_actual in self.nodos:
                hijos = list(self.nodos[nodo_actual].keys())
                mejor_hijo = min(hijos, key=lambda h: heuristica[h])  # Selecciona el mejor hijo basado en la heurística
                
                if mejor_hijo not in solucion:
                    heapq.heappush(frontera, (heuristica[mejor_hijo], mejor_hijo, camino + [mejor_hijo]))
        
        return None  # Si no hay solución

# Definir el grafo
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
camino_a, costo_a = grafo.a_estrella("A", "F", heuristica)
print("Camino óptimo con A*:", camino_a, "\nCosto total:", costo_a)

# Ejecutar AO*
camino_ao = grafo.ao_estrella("A", "F", heuristica)
print("Camino encontrado con AO*:", camino_ao)
