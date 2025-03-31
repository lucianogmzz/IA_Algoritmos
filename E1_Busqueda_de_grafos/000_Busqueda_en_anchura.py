from collections import deque    #double-ended-queue, colas eficioentes

def bfs(grafo, inicio, objetivo):
    
    # Implementación de Búsqueda en Anchura (BFS).
    
    # Parámetros:
    #     grafo (dict): Diccionario que representa el grafo (lista de adyacencia).
    #     inicio (str): Nodo inicial de la búsqueda.
    #     objetivo (str): Nodo objetivo a encontrar.
    
    # Retorna:
    #     list: Camino desde 'inicio' hasta 'objetivo', o mensaje de no encontrado.
   
    # Usamos una cola para gestionar los nodos a explorar (FIFO)
    cola = deque([[inicio]])  # La cola almacena caminos, no solo nodos
    visitados = set()  # Conjunto para nodos ya visitados (evita ciclos)

    while cola:
        camino = cola.popleft()  # Extrae el primer camino de la cola
        nodo_actual = camino[-1]  # El último nodo del camino es el actual

        # Si encontramos el objetivo, retornamos el camino
        if nodo_actual == objetivo:
            return camino

        # Si el nodo no ha sido visitado, lo procesamos
        if nodo_actual not in visitados:
            visitados.add(nodo_actual)  # Marcamos como visitado

            # Exploramos todos los vecinos del nodo actual
            for vecino in grafo.get(nodo_actual, []):
                nuevo_camino = list(camino)  # Copiamos el camino actual
                nuevo_camino.append(vecino)  # Añadimos el vecino
                cola.append(nuevo_camino)  # Agregamos el nuevo camino a la cola

    return "No se encontró un camino"

# Ejemplo de grafo no dirigido (lista de adyacencia)
grafo = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# Ejecutamos BFS desde 'A' hasta 'F'
print(bfs(grafo, 'A', 'F'))  # Salida: ['A', 'C', 'F']