from collections import deque

def bidirectional_search(grafo, inicio, objetivo):
    """
    Implementación de Búsqueda Bidireccional usando BFS en ambas direcciones
    
    Args:
        grafo (dict): Diccionario de listas de adyacencia
        inicio (str): Nodo inicial
        objetivo (str): Nodo objetivo
    
    Returns:
        list: Camino completo desde inicio hasta objetivo
        str: Mensaje si no se encuentra
    """
    # Verificación rápida de nodos existentes
    if inicio not in grafo or objetivo not in grafo:
        return "Nodo inicial o objetivo no existe en el grafo"
    
    # Estructuras para la búsqueda hacia adelante
    cola_adelante = deque()
    cola_adelante.append([inicio])
    visitados_adelante = {inicio: [inicio]}
    
    # Estructuras para la búsqueda hacia atrás
    cola_atras = deque()
    cola_atras.append([objetivo])
    visitados_atras = {objetivo: [objetivo]}
    
    # Búsqueda simultánea
    while cola_adelante and cola_atras:
        # Búsqueda desde el inicio
        camino_adelante = cola_adelante.popleft()
        nodo_actual_adelante = camino_adelante[-1]
        
        # Búsqueda desde el objetivo
        camino_atras = cola_atras.popleft()
        nodo_actual_atras = camino_atras[-1]
        
        # Verificar intersección
        if nodo_actual_adelante in visitados_atras:
            # Reconstruir camino completo
            camino_completo = camino_adelante[:-1] + visitados_atras[nodo_actual_adelante][::-1]
            return camino_completo
        
        if nodo_actual_atras in visitados_adelante:
            # Reconstruir camino completo
            camino_completo = visitados_adelante[nodo_actual_atras][:-1] + camino_atras[::-1]
            return camino_completo
        
        # Expandir búsqueda hacia adelante
        for vecino in grafo.get(nodo_actual_adelante, []):
            if vecino not in visitados_adelante:
                visitados_adelante[vecino] = camino_adelante + [vecino]
                cola_adelante.append(camino_adelante + [vecino])
        
        # Expandir búsqueda hacia atrás
        for vecino in grafo.get(nodo_actual_atras, []):
            if vecino not in visitados_atras:
                visitados_atras[vecino] = camino_atras + [vecino]
                cola_atras.append(camino_atras + [vecino])
    
    return "No se encontró un camino entre los nodos"

# Ejemplo de grafo no dirigido
grafo_ejemplo = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B', 'G'],
    'E': ['B', 'H'],
    'F': ['C', 'I'],
    'G': ['D'],
    'H': ['E', 'J'],
    'I': ['F'],
    'J': ['H']
}

# Ejecución
resultado = bidirectional_search(grafo_ejemplo, 'A', 'J')
print("Camino encontrado:", resultado)