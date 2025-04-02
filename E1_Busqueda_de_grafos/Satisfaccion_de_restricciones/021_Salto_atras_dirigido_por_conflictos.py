import networkx as nx
import matplotlib.pyplot as plt

# Definir el grafo como un diccionario de adyacencias
grafo = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D'],
    'D': ['B', 'C']
}

# Colores posibles
colores = ['Rojo', 'Verde', 'Azul']

# Almacenar la solución
solucion = {}

# Función para verificar si la asignación es válida
def es_valida(nodo, color):
    for vecino in grafo[nodo]:  # Revisar vecinos del nodo
        if vecino in solucion and solucion[vecino] == color:
            return False  # Conflicto de color
    return True

# Implementación del Salto Atrás Dirigido por Conflictos (CDBJ)
def salto_atras_dirigido(nodo_actual, orden_nodos, conflictos):
    if nodo_actual == len(orden_nodos):  # Si todos los nodos están coloreados
        return True

    nodo = orden_nodos[nodo_actual]

    for color in colores:
        if es_valida(nodo, color):
            solucion[nodo] = color  # Asignar color al nodo

            if salto_atras_dirigido(nodo_actual + 1, orden_nodos, conflictos):  # Intentar siguiente nodo
                return True
            
            del solucion[nodo]  # Deshacer asignación si falla

    # Si no se encontró color válido, hacer salto atrás dirigido
    if nodo_actual > 0:
        nodo_conflictivo = conflictos[nodo] if nodo in conflictos else nodo_actual - 1
        return salto_atras_dirigido(nodo_conflictivo, orden_nodos, conflictos)
    
    return False  # No hay solución

# Aplicar el algoritmo
orden_nodos = list(grafo.keys())
conflictos = {}  # Diccionario para almacenar conflictos

if salto_atras_dirigido(0, orden_nodos, conflictos):
    print("🔹 Solución encontrada:")
    for nodo, color in solucion.items():
        print(f"  {nodo} → {color}")
else:
    print("No se encontró una solución.")

# Dibujar el grafo coloreado
G = nx.Graph()
G.add_edges_from([(nodo, vecino) for nodo in grafo for vecino in grafo[nodo]])

color_map = {nodo: solucion[nodo] for nodo in grafo}
colores_visual = {'Rojo': 'red', 'Verde': 'green', 'Azul': 'blue'}

plt.figure(figsize=(5, 5))
nx.draw(G, with_labels=True, node_color=[colores_visual[color_map[n]] for n in G.nodes], node_size=1000, font_weight='bold')
plt.show()
