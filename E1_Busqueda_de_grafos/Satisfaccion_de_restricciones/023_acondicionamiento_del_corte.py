import itertools

grafo = {
    'Matemáticas': ['Física', 'Química'],
    'Física': ['Matemáticas', 'Biología'],
    'Química': ['Matemáticas', 'Biología'],
    'Biología': ['Física', 'Química']
}

horarios = ['8AM', '10AM', '12PM']

def es_valido(asignacion, clase, horario):
    for conflicto in grafo[clase]:
        if conflicto in asignacion and asignacion[conflicto] == horario:
            return False
    return True

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

def asignar_horarios_cutset(grafo, horarios):
    cutset = {'Matemáticas'}  # Cortamos esta clase para resolver primero
    asignaciones_cutset = list(itertools.product(horarios, repeat=len(cutset)))
    
    for asignacion in asignaciones_cutset:
        asignacion_actual = dict(zip(cutset, asignacion))
        if all(es_valido(asignacion_actual, clase, asignacion_actual[clase]) for clase in cutset):
            if resolver_subgrafo(grafo, horarios, asignacion_actual, set(grafo.keys()) - cutset):
                return asignacion_actual
    
    return None

solucion = asignar_horarios_cutset(grafo, horarios)

if solucion:
    print("\n✅ Horarios asignados:")
    for clase in sorted(solucion.keys()):
        print(f"Clase {clase} → {solucion[clase]}")
else:
    print("\n❌ No se encontró una solución válida.")
