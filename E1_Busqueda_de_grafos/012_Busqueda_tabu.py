import random  # Para la selección aleatoria de soluciones

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
    
    def busqueda_tabu(self, inicio, objetivo, heuristica, max_tabu=5, iteraciones=10):
        """
        Implementación de Búsqueda Tabú.
        :param inicio: Nodo de inicio.
        :param objetivo: Nodo objetivo.
        :param heuristica: Diccionario con valores heurísticos de cada nodo.
        :param max_tabu: Tamaño máximo de la lista tabú.
        :param iteraciones: Número máximo de iteraciones.
        """
        nodo_actual = inicio
        mejor_solucion = nodo_actual
        mejor_valor = heuristica[nodo_actual]
        
        tabu_list = []  # Lista tabú para evitar ciclos
        camino = [nodo_actual]
        
        for _ in range(iteraciones):
            vecinos = self.nodos[nodo_actual]
            
            if objetivo in vecinos:
                camino.append(objetivo)
                return camino  # Se encontró la solución óptima
            
            # Filtrar vecinos que no están en la lista tabú
            vecinos_validos = [n for n in vecinos if n not in tabu_list]
            
            if not vecinos_validos:
                return camino  # No hay más movimientos válidos
            
            # Elegir el mejor vecino basado en la heurística
            mejor_vecino = max(vecinos_validos, key=lambda n: heuristica[n])
            
            # Actualizar mejor solución encontrada
            if heuristica[mejor_vecino] > mejor_valor:
                mejor_solucion = mejor_vecino
                mejor_valor = heuristica[mejor_vecino]
            
            # Actualizar nodo actual y lista tabú
            nodo_actual = mejor_vecino
            camino.append(nodo_actual)
            tabu_list.append(nodo_actual)
            
            # Limitar tamaño de la lista tabú
            if len(tabu_list) > max_tabu:
                tabu_list.pop(0)
        
        return camino  # Devolver el mejor camino encontrado

# Definir el grafo
grafo = Grafo()
grafo.agregar_nodo("A", {"B": 2, "C": 3})
grafo.agregar_nodo("B", {"A": 2, "D": 4, "E": 1})
grafo.agregar_nodo("C", {"A": 3, "F": 5})
grafo.agregar_nodo("D", {"B": 4, "E": 2})
grafo.agregar_nodo("E", {"B": 1, "D": 2, "F": 3})
grafo.agregar_nodo("F", {"C": 5, "E": 3})

# Definir heurística (valores más altos son mejores)
heuristica = {"A": 3, "B": 6, "C": 4, "D": 5, "E": 8, "F": 10}

# Ejecutar Búsqueda Tabú
camino_tabu = grafo.busqueda_tabu("A", "F", heuristica)
print("Camino encontrado con Búsqueda Tabú:", camino_tabu)
