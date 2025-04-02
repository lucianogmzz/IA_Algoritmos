import heapq

def ucs(grafo, inicio, objetivo):

    # Implementación de Búsqueda de Costo Uniforme (UCS).
    
    # Parámetros:
    #     grafo (dict): Diccionario con nodos y aristas ponderadas (ej: {'A': [('B', 1), ('C', 3)]}).
    #     inicio (str): Nodo inicial.
    #     objetivo (str): Nodo objetivo.
    
    # Retorna:
    #     tuple: (costo_total, camino) o "No se encontró camino".
  
    cola_prioridad = []
    heapq.heappush(cola_prioridad, (0, [inicio]))  # (costo_acumulado, camino)
    visitados = set()

    while cola_prioridad:
        costo, camino = heapq.heappop(cola_prioridad)
        nodo_actual = camino[-1]

        if nodo_actual == objetivo:
            return (costo, camino)  # Solución encontrada

        if nodo_actual not in visitados:
            visitados.add(nodo_actual)  #marca como visitado para no reporcesar

            for vecino, costo_arista in grafo.get(nodo_actual, []):  #ITERA SOBRE EL NODO ACTUAL Y LOS ADYACENTES
                if vecino not in visitados:
                    nuevo_costo = costo + costo_arista  #calcula el nuevo costo
                    nuevo_camino = camino + [vecino]   #añade el nuevo vecino al camino
                    heapq.heappush(cola_prioridad, (nuevo_costo, nuevo_camino))  #INSERTA EL NUEVO CAMINO-COSTO AL HEAP

    return "No se encontró camino"

# Ejemplo de grafo ponderado
grafo = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('D', 3), ('E', 2)],
    'C': [('A', 4), ('F', 5)],
    'D': [('B', 3), ('F', 1)],
    'E': [('B', 2), ('F', 3)],
    'F': [('C', 5), ('D', 1), ('E', 3)]
}

# Ejecución desde 'A' hasta 'F'
resultado = ucs(grafo, 'A', 'F')
print(f"Costo: {resultado[0]}, Camino: {resultado[1]}")  # Salida: (5, ['A', 'B', 'D', 'F'])