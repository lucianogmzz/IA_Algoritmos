# Luciano Alejandro Gómez Muñoz 22310214

# Este código implementa una solución al problema de asignación de horarios utilizando el método de corte (cutset).
# El problema consiste en asignar horarios a clases de tal manera que no haya conflictos de horario entre clases que comparten estudiantes.
# La solución utiliza el método de corte para resolver primero un subgrafo y luego extender la solución al grafo completo.

# Importamos la librería itertools para generar combinaciones de horarios
import itertools

# Definir el grafo de conflictos entre clases
grafo = {
    'Matemáticas': ['Física', 'Química'],
    'Física': ['Matemáticas', 'Biología'],
    'Química': ['Matemáticas', 'Biología'],
    'Biología': ['Física', 'Química']
}

# Definir los horarios disponibles
horarios = ['8AM', '10AM', '12PM']

# Función para verificar si una asignación es válida
def es_valido(asignacion, clase, horario):
    for conflicto in grafo[clase]:
        if conflicto in asignacion and asignacion[conflicto] == horario:
            return False
    return True

# Función para resolver el subgrafo utilizando backtracking
def resolver_subgrafo(grafo, horarios, asignacion, clases_restantes):
    if not clases_restantes:
        return True

    clase = clases_restantes.pop()
    for horario in horarios:
        if es_valido(asignacion, clase, horario):
            asignacion[clase] = horario
            if resolver_subgrafo(grafo, horarios, asignacion, clases_restantes.copy()):
                return True
            del asignacion[clase]

    clases_restantes.add(clase)
    return False

# Función para asignar horarios utilizando el método de corte
def asignar_horarios_cutset(grafo, horarios):
    cutset = {'Matemáticas'}  # Cortamos esta clase para resolver primero
    asignaciones_cutset = list(itertools.product(horarios, repeat=len(cutset)))

    for asignacion in asignaciones_cutset:
        asignacion_actual = dict(zip(cutset, asignacion))
        if all(es_valido(asignacion_actual, clase, asignacion_actual[clase]) for clase in cutset):
            if resolver_subgrafo(grafo, horarios, asignacion_actual, set(grafo.keys()) - cutset):
                return asignacion_actual

    return None

# Ejecutar el algoritmo
solucion = asignar_horarios_cutset(grafo, horarios)

if solucion:
    print("\n✅ Horarios asignados:")
    for clase in sorted(solucion.keys()):
        print(f"Clase {clase} → {solucion[clase]}")
else:
    print("\n❌ No se encontró una solución válida.")
