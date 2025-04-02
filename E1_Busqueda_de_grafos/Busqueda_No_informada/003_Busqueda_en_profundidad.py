def dfs(grafo, inicio, objetivo):
    
    # Implementación iterativa de Depth-First Search (DFS) usando una pila.
    
    # Parámetros:
    #     grafo (dict): Diccionario que representa el grafo como lista de adyacencia.
    #                  Formato: {'nodo': ['vecino1', 'vecino2', ...]}
    #     inicio (str): Nodo inicial desde donde comienza la búsqueda.
    #     objetivo (str): Nodo que queremos encontrar.
    
    # Retorna:
    #     list: Camino desde el nodo inicial hasta el objetivo, si existe.
    #     str: Mensaje de error si no se encuentra el objetivo.
   
    
    # Inicializamos la pila con una tupla que contiene:
    # - El nodo actual (inicio)
    # - El camino recorrido hasta ahora (que inicialmente solo contiene el nodo inicio)
    pila = [(inicio, [inicio])]
    
    # Conjunto para llevar registro de los nodos ya visitados y evitar ciclos
    visitados = set()

    # Mientras haya nodos por explorar en la pila
    while pila:
        # Extraemos el último nodo añadido (comportamiento LIFO)
        nodo_actual, camino = pila.pop()
        
        # Si encontramos el nodo objetivo, retornamos el camino
        if nodo_actual == objetivo:
            return camino
        
        # Solo procesamos el nodo si no ha sido visitado antes
        if nodo_actual not in visitados:
            # Marcamos el nodo como visitado
            visitados.add(nodo_actual)
            
            # Exploramos los vecinos del nodo actual
            # Usamos reversed() para procesar los vecinos en orden (opcional)
            for vecino in reversed(grafo.get(nodo_actual, [])):
                # Si el vecino no ha sido visitado, lo añadimos a la pila
                if vecino not in visitados:
                    # Añadimos a la pila:
                    # - El vecino como nuevo nodo actual
                    # - El camino actual más este nuevo vecino
                    pila.append((vecino, camino + [vecino]))
    
    # Si la pila se vacía sin encontrar el objetivo
    return "No se encontró un camino al objetivo"

# Ejemplo de grafo no dirigido representado como lista de adyacencia
grafo_ejemplo = {
    'A': ['B', 'C'],    # A está conectado con B y C
    'B': ['A', 'D', 'E'],  # B está conectado con A, D y E
    'C': ['A', 'F'],     # C está conectado con A y F
    'D': ['B'],          # D está conectado solo con B
    'E': ['B', 'F'],     # E está conectado con B y F
    'F': ['C', 'E']      # F está conectado con C y E
}

# Ejecutamos DFS desde 'A' hasta 'F'
inicio = 'A'
objetivo = 'F'
resultado = dfs(grafo_ejemplo, inicio, objetivo)

# Mostramos resultados
print(f"Camino encontrado de {inicio} a {objetivo}: {resultado}")
