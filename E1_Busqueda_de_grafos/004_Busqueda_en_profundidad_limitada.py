def dls(grafo, inicio, objetivo, limite_profundidad):
    """
    Implementación iterativa de Depth-Limited Search (DLS)
    
    Args:
        grafo (dict): Diccionario de listas de adyacencia
        inicio (str): Nodo inicial de búsqueda
        objetivo (str): Nodo objetivo a encontrar
        limite_profundidad (int): Máxima profundidad permitida
    
    Returns:
        list: Camino desde inicio hasta objetivo si se encuentra
        str: Mensaje de error si no se encuentra
    """
    # Pila almacena tuplas de (nodo, camino, profundidad)
    pila = [(inicio, [inicio], 0)]
    visitados = set()

    while pila:
        # Extraer el último nodo añadido (LIFO)
        nodo_actual, camino, profundidad = pila.pop()

        # Comprobar si encontramos el objetivo
        if nodo_actual == objetivo:
            return camino

        # Solo expandir si no superamos el límite
        if profundidad < limite_profundidad:
            if nodo_actual not in visitados:
                visitados.add(nodo_actual)

                # Explorar vecinos en orden inverso para mantener orden natural
                for vecino in reversed(grafo.get(nodo_actual, [])):
                    if vecino not in visitados:
                        pila.append((vecino, camino + [vecino], profundidad + 1))

    return f"No se encontró {objetivo} dentro de profundidad {limite_profundidad}"

# Ejemplo de grafo
grafo_ejemplo = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': ['H'],
    'F': [],
    'G': [],
    'H': []
}

# Ejecución con límite de profundidad 2
resultado = dls(grafo_ejemplo, 'A', 'H', 3)
print(resultado)  # No encontrará H porque está a profundidad 3