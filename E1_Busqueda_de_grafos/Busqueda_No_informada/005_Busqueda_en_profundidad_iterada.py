def iddfs(grafo, inicio, objetivo):
    """
    Implementación de Iterative Deepening Depth-First Search (IDDFS)
    
    Args:
        grafo (dict): Diccionario de listas de adyacencia
        inicio (str): Nodo inicial de búsqueda
        objetivo (str): Nodo objetivo a encontrar
    
    Returns:
        list: Camino desde inicio hasta objetivo
        str: Mensaje si no se encuentra
    """
    # Función auxiliar para DLS (Depth-Limited Search)
    def dls(nodo, objetivo, limite):
        pila = [(nodo, [nodo], 0)]
        visitados = set()
        
        while pila:
            nodo_actual, camino, profundidad = pila.pop()
            
            if nodo_actual == objetivo:
                return camino
                
            if profundidad < limite:
                if nodo_actual not in visitados:
                    visitados.add(nodo_actual)
                    for vecino in reversed(grafo.get(nodo_actual, [])):
                        if vecino not in visitados:
                            pila.append((vecino, camino + [vecino], profundidad + 1))
        return None

    # Iteración con profundidad incremental
    profundidad = 0
    while True:
        resultado = dls(inicio, objetivo, profundidad)
        if resultado is not None:
            return resultado
        profundidad += 1
        # Opcional: establecer un límite máximo para evitar bucles infinitos
        if profundidad > 100:  # Límite de seguridad
            return f"No se encontró {objetivo} en profundidad máxima {profundidad}"

# Ejemplo de grafo
grafo_ejemplo = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': ['H'],
    'F': [],
    'G': ['I'],
    'H': [],
    'I': []
}

# Ejecución
resultado = iddfs(grafo_ejemplo, 'A', 'I')
print("Camino encontrado:", resultado)