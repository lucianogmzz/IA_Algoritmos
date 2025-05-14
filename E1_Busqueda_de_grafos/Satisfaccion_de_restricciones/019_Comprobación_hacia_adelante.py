# Luciano Alejandro Gómez Muñoz 22310214

# Este código implementa una solución al problema de Sudoku utilizando el algoritmo de backtracking con forward checking.
# El problema de Sudoku consiste en llenar un tablero 9x9 con números del 1 al 9, de tal manera que cada fila, columna y bloque 3x3 contenga todos los números sin repetición.
# La solución utiliza backtracking para explorar todas las posibles asignaciones de números y forward checking para reducir el dominio de valores posibles.

import numpy as np

# Función para encontrar la siguiente celda vacía en el Sudoku
def encontrar_celda_vacia(tablero):
    for fila in range(9):
        for columna in range(9):
            if tablero[fila][columna] == 0:  # Celda vacía
                return fila, columna
    return None  # No hay más celdas vacías (Sudoku resuelto)

# Función para verificar si un número puede colocarse en una celda
def es_valido(tablero, fila, columna, num):
    # Verificar si el número ya está en la fila
    if num in tablero[fila]:
        return False
    # Verificar si el número ya está en la columna
    if num in tablero[:, columna]:
        return False
    # Verificar si el número ya está en el bloque 3x3
    bloque_fila = (fila // 3) * 3
    bloque_columna = (columna // 3) * 3
    if num in tablero[bloque_fila:bloque_fila+3, bloque_columna:bloque_columna+3]:
        return False
    return True

# Función que implementa Backtracking con Forward Checking
def forward_checking(tablero):
    # Encontrar la siguiente celda vacía
    celda = encontrar_celda_vacia(tablero)
    if not celda:  # Si no hay más celdas vacías, el Sudoku está resuelto
        return True

    fila, columna = celda

    # Dominio: valores posibles en la celda
    posibles_valores = [num for num in range(1, 10) if es_valido(tablero, fila, columna, num)]

    # Aplicamos forward checking: Intentamos solo valores válidos
    for num in posibles_valores:
        tablero[fila][columna] = num  # Asignamos un número

        if forward_checking(tablero):  # Llamada recursiva para resolver el resto
            return True

        tablero[fila][columna] = 0  # Si no funciona, revertimos el cambio (Backtracking)

    return False  # Si ningún número funciona, retrocedemos

# Sudoku inicial con algunas celdas vacías (0 representa vacío)
sudoku = np.array([
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
])

# Resolver el Sudoku con Forward Checking
if forward_checking(sudoku):
    print("🔹 Sudoku Resuelto:")
    print(sudoku)
else:
    print("No se encontró solución.")

