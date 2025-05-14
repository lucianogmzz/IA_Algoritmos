# Luciano Alejandro Gómez Muñoz 22310214

# Este código implementa un algoritmo de búsqueda en profundidad (DFS) para encontrar un nodo objetivo en un grafo.
# El grafo está representado como un diccionario de adyacencia, donde las claves son los nodos y los valores son listas de nodos adyacentes.
# La función de búsqueda online explora el grafo desde un nodo de inicio hasta encontrar el nodo objetivo.

# Grafo representado como un diccionario de adyacencia
grafo = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'E'],
    'D': ['B'],
    'E': ['B', 'C']
}

# Función de búsqueda online
def busqueda_online(grafo, inicio, objetivo):
    """ Implementa la búsqueda online de un nodo objetivo en un grafo. """

    # La lista de nodos visitados
    visitados = set()

    # La pila de nodos por explorar (implementación de DFS)
    frontera = [inicio]

    # Mientras haya nodos por explorar
    while frontera:
        # El agente elige un nodo de la frontera para explorar
        nodo_actual = frontera.pop(0)  # Extracción del primer nodo de la frontera

        # Si el nodo actual es el objetivo, hemos encontrado la solución
        if nodo_actual == objetivo:
            print(f"¡Objetivo '{objetivo}' encontrado desde '{inicio}'!")
            return True

        # Si el nodo no ha sido visitado, lo marcamos como visitado
        if nodo_actual not in visitados:
            visitados.add(nodo_actual)
            print(f"Explorando: {nodo_actual}")

            # Añadimos los nodos adyacentes no visitados a la frontera
            for vecino in grafo[nodo_actual]:
                if vecino not in visitados:
                    frontera.append(vecino)

    # Si no se encuentra el objetivo
    print(f"Objetivo '{objetivo}' no encontrado.")
    return False

# Ejecución de la búsqueda online
inicio = 'A'
objetivo = 'D'
busqueda_online(grafo, inicio, objetivo)
