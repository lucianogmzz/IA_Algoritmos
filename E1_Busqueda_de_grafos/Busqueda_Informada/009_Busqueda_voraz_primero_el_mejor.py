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
    
    def busqueda_voraz(self, inicio, objetivo, heuristica):
        """
        Implementación de Búsqueda Voraz Primero el Mejor.
        :param inicio: Nodo de inicio.
        :param objetivo: Nodo objetivo.
        :param heuristica: Diccionario con valores heurísticos de cada nodo.
        """
        frontera = [(heuristica[inicio], inicio, [inicio])]  # (heurística, nodo actual, camino recorrido)
        visitados = set()
        
        while frontera:
            _, nodo_actual, camino = heapq.heappop(frontera)  # Extrae el nodo con menor heurística
            
            if nodo_actual in visitados:
                continue
            
            visitados.add(nodo_actual)
            
            if nodo_actual == objetivo:
                return camino  # Se encontró el camino al objetivo
            
            for vecino in self.nodos[nodo_actual].keys():
                if vecino not in visitados:
                    heapq.heappush(frontera, (heuristica[vecino], vecino, camino + [vecino]))
        
        return None  # Si no se encuentra camino

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

# Ejecutar búsqueda voraz
camino = grafo.busqueda_voraz("A", "F", heuristica)
print("Camino encontrado:", camino)
