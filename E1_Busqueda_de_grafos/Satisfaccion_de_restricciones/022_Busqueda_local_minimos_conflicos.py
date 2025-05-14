# Luciano Alejandro Gómez Muñoz 22310214

# Este código implementa una solución al problema de las N-Reinas utilizando el algoritmo de Mínimos-Conflictos.
# El problema de las N-Reinas consiste en colocar N reinas en un tablero de ajedrez de N x N de tal manera que ninguna reina se ataque entre sí.
# La solución utiliza el algoritmo de Mínimos-Conflictos para explorar las posibles asignaciones de reinas y minimizar los conflictos.

# Importamos la librería random para generar números aleatorios
import random

# Función para contar conflictos en una posición de reina
def contar_conflictos(tablero, fila, columna):
    n = len(tablero)
    conflictos = 0
    for i in range(n):
        if i != columna:
            # Verificar si hay una reina en la misma fila o en diagonales
            if tablero[i] == fila or abs(tablero[i] - fila) == abs(i - columna):
                conflictos += 1
    return conflictos

# Algoritmo de Mínimos-Conflictos para N-Reinas
def minimos_conflictos_n_reinas(n, max_iteraciones=1000):
    # Asignación inicial aleatoria (una reina en cada columna en cualquier fila)
    tablero = [random.randint(0, n-1) for _ in range(n)]

    for _ in range(max_iteraciones):
        # Verificar si la solución es válida (sin conflictos)
        conflictos = [contar_conflictos(tablero, tablero[col], col) for col in range(n)]
        if sum(conflictos) == 0:
            return tablero  # Solución encontrada

        # Elegir una columna conflictiva aleatoriamente
        columnas_conflictivas = [i for i in range(n) if conflictos[i] > 0]
        columna = random.choice(columnas_conflictivas)

        # Elegir la fila con menos conflictos para esa columna
        mejor_fila = min(range(n), key=lambda fila: contar_conflictos(tablero, fila, columna))

        # Mover la reina a la fila con menos conflictos
        tablero[columna] = mejor_fila

    return None  # No se encontró solución en el límite de iteraciones

# Definir tamaño del tablero
N = 8  # Puedes cambiar este valor para probar con diferentes tamaños

# Ejecutar el algoritmo
solucion = minimos_conflictos_n_reinas(N)

if solucion:
    print(f"🔹 Solución para {N}-Reinas encontrada:")
    for fila in range(N):
        linea = ""
        for columna in range(N):
            if solucion[columna] == fila:
                linea += "♛ "  # Representa la reina
            else:
                linea += ". "
        print(linea)
else:
    print("No se encontró una solución.")
