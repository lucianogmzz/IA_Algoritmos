import random  # Para selección aleatoria de estados

# Definimos el grafo como un diccionario donde las claves son los nodos
# y los valores son listas de tuplas (vecino, costo)
grafo = {
    'A': [('B', 4), ('C', 2)],
    'B': [('A', 4), ('D', 3), ('E', 2)],
    'C': [('A', 2), ('F', 5)],
    'D': [('B', 3)],
    'E': [('B', 2), ('F', 1)],
    'F': [('C', 5), ('E', 1)]
}

def beam_search(grafo, inicio, objetivo, k):
    """
    Implementa la búsqueda de haz local en un grafo.
    """
    # Inicializamos con k caminos que solo contienen el nodo inicial
    caminos = [[inicio]]

    while caminos:
        nuevos_caminos = []

        for camino in caminos:
            nodo_actual = camino[-1]  # Último nodo en el camino actual

            if nodo_actual == objetivo:
                return camino  # Si llegamos al objetivo, devolvemos el camino encontrado

            # Generamos caminos vecinos extendiendo el actual con cada vecino
            for vecino, costo in grafo.get(nodo_actual, []):
                if vecino not in camino:  # Evitar ciclos
                    nuevos_caminos.append(camino + [vecino])

        # Seleccionamos los k mejores caminos basados en su costo total
        nuevos_caminos_con_costos = []

        for camino in nuevos_caminos:
            costo_total = 0
            for i in range(len(camino) - 1):
                for vecino, costo in grafo[camino[i]]:
                    if vecino == camino[i + 1]:
                        costo_total += costo
            nuevos_caminos_con_costos.append((camino, costo_total))

        # Ordenamos los caminos por costo total y mantenemos los k mejores
        caminos = [camino for camino, costo in sorted(nuevos_caminos_con_costos, key=lambda x: x[1])][:k]

    return None  # Si no encontramos un camino, devolvemos None

# Parámetros
inicio = 'A'
objetivo = 'F'
k = 2  # Número de caminos a mantener

# Ejecutar el algoritmo
mejor_camino = beam_search(grafo, inicio, objetivo, k)
print(f"Mejor camino encontrado: {mejor_camino}")
