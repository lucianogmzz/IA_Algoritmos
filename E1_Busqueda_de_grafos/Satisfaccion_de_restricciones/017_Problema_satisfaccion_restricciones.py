# Luciano Alejandro Gómez Muñoz 22310214

# Este código implementa una solución al problema de las n-reinas utilizando el algoritmo de satisfacción de restricciones (CSP).
# El problema de las n-reinas consiste en colocar n reinas en un tablero de ajedrez de n x n de tal manera que ninguna reina se ataque entre sí.
# La solución utiliza permutaciones para generar todas las posibles configuraciones de reinas y verifica si cumplen con las restricciones.

# Importamos la librería de itertools para generar permutaciones
from itertools import permutations

# Función para verificar si la asignación de reinas es válida
def es_valida(tablero):
    """
    Verifica si la asignación de reinas es válida, es decir, que ninguna reina se ataque.
    """
    # Verificar filas y columnas
    for i in range(len(tablero)):
        for j in range(i + 1, len(tablero)):
            # Las reinas no deben estar en la misma fila ni en la misma columna
            if tablero[i] == tablero[j]:
                return False

            # Verificar las diagonales
            if abs(tablero[i] - tablero[j]) == abs(i - j):
                return False
    return True

# Generación de todas las posibles permutaciones de posiciones para las reinas
def resolver_csp(n):
    """
    Resuelve el problema de las n reinas utilizando el algoritmo de satisfacción de restricciones.
    Genera todas las permutaciones posibles y verifica si cumplen con las restricciones.
    """
    # Generamos todas las permutaciones posibles de columnas para las reinas
    permutaciones_posibles = permutations(range(n))

    for perm in permutaciones_posibles:
        if es_valida(perm):  # Si la permutación cumple las restricciones
            return perm  # Retorna la solución válida

    return None  # Si no hay solución, retorna None

# Ejemplo de uso con n=3 (tablero 3x3)
n = 3
solucion = resolver_csp(n)

if solucion:
    print(f"Una solución válida para el tablero {n}x{n} es:", solucion)
else:
    print(f"No se encontró solución para el tablero {n}x{n}.")
