import networkx as nx
import matplotlib.pyplot as plt

# Definir el grafo
grafo = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D'],
    'D': ['B', 'C']
}

# Definir los posibles colores
colores = ['Rojo', 'Verde', 'Azul']

# Inicializar dominios de cada nodo (cada nodo puede tener cualquier color inicialmente)
dominios = {nodo: colores[:] for nodo in grafo}

# Función para reducir dominios basado en restricciones (propagación de restricciones)
def propagar_restricciones():
    cambios = True
    while cambios:
        cambios = False
        for nodo, vecinos in grafo.items():
            if len(dominios[nodo]) == 1:  # Si el nodo ya tiene un color asignado
                color_fijo = dominios[nodo][0]
                for vecino in vecinos:
                    if color_fijo in dominios[vecino]:  # Eliminar el color del dominio del vecino
                        dominios[vecino].remove(color_fijo)
                        cambios = True  # Hubo un cambio, repetir la propagación

# Función para resolver el problema con propagación y backtracking
def resolver_coloreo(nodo_actual=0, nodos=list(grafo.keys())):
    if nodo_actual == len(nodos):  # Si todos los nodos están coloreados
        return True

    nodo = nodos[nodo_actual]
    if len(dominios[nodo]) == 1:  # Si el nodo ya tiene un color fijo
        return resolver_coloreo(nodo_actual + 1, nodos)

    for color in dominios[nodo]:  # Intentar cada color posible
        asignacion_valida = True
        for vecino in grafo[nodo]:  # Verificar si algún vecino tiene el mismo color
            if len(dominios[vecino]) == 1 and dominios[vecino][0] == color:
                asignacion_valida = False
                break

        if asignacion_valida:
            dominios_original = dominios.copy()  # Guardar estado
            dominios[nodo] = [color]  # Asignar color
            propagar_restricciones()  # Propagar restricciones

            if resolver_coloreo(nodo_actual + 1, nodos):  # Continuar con el siguiente nodo
                return True

            dominios.update(dominios_original)  # Revertir cambios si falló

    return False  # No hay solución

# Aplicar propagación inicial
propagar_restricciones()

# Resolver problema
if resolver_coloreo():
    print("🔹 Solución encontrada:")
    for nodo, color in dominios.items():
        print(f"  {nodo} → {color[0]}")
else:
    print("No se encontró una solución.")

# Dibujar el grafo coloreado
G = nx.Graph()
G.add_edges_from([(nodo, vecino) for nodo in grafo for vecino in grafo[nodo]])

color_map = {nodo: dominios[nodo][0] for nodo in grafo}
colores_visual = {'Rojo': 'red', 'Verde': 'green', 'Azul': 'blue'}

plt.figure(figsize=(5, 5))
nx.draw(G, with_labels=True, node_color=[colores_visual[color_map[n]] for n in G.nodes], node_size=1000, font_weight='bold')
plt.show()
