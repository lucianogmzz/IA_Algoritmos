# Definimos una función para verificar si un nodo puede ser coloreado con un color específico
def es_valido(nodo, color, colores, grafo):
    """
    Verifica si podemos asignar el color al nodo sin violar restricciones.
    """
    for vecino in grafo[nodo]:  # Revisamos los nodos adyacentes
        if colores[vecino] == color:  # Si algún vecino tiene el mismo color, no es válido
            return False
    return True  # Si no hay conflictos, la asignación es válida

# Algoritmo de backtracking para colorear el grafo
def colorear_grafo(nodo, grafo, colores, num_colores):
    """
    Intenta asignar colores a los nodos del grafo usando backtracking.
    """
    if nodo == len(grafo):  # Si todos los nodos han sido coloreados, hemos encontrado una solución
        return True

    for color in range(num_colores):  # Intentamos asignar cada color posible
        if es_valido(nodo, color, colores, grafo):  # Verificamos si el color es válido
            colores[nodo] = color  # Asignamos el color al nodo
            if colorear_grafo(nodo + 1, grafo, colores, num_colores):  # Llamada recursiva para el siguiente nodo
                return True  # Si se encuentra una solución, retornamos True
            colores[nodo] = -1  # Si no se encuentra solución, se retrocede (backtrack)

    return False  # Si no hay solución con los colores dados, retornamos False

# Definimos un grafo como una lista de listas (lista de adyacencia)
grafo = {
    0: [1, 2],   # Nodo 0 está conectado con 1 y 2
    1: [0, 2, 3], # Nodo 1 está conectado con 0, 2 y 3
    2: [0, 1, 3], # Nodo 2 está conectado con 0, 1 y 3
    3: [1, 2]    # Nodo 3 está conectado con 1 y 2
}

num_nodos = len(grafo)  # Número de nodos en el grafo
num_colores = 3  # Número máximo de colores permitidos
colores = [-1] * num_nodos  # Inicialmente, todos los nodos no tienen color (-1)

# Intentamos colorear el grafo
if colorear_grafo(0, grafo, colores, num_colores):
    print("Solución encontrada: ", colores)
else:
    print("No se encontró solución con", num_colores, "colores.")
