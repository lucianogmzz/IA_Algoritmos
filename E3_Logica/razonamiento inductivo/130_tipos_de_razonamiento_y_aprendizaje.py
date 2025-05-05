# Luciano Alejandro Gómez Muñoz 22310214
# Tipos de Razonamiento y Aprendizaje
# Este programa demuestra de manera simplificada los tres tipos de razonamiento
# lógico utilizados en IA: deductivo, inductivo y abductivo.

# Este código es educativo y funciona como una simulación lógica con condiciones y listas.

# ------------------ Razonamiento Deductivo ------------------

# Base de conocimiento
hechos_generales = {
    "todos_los_humanos_son_mortales": True,
    "socrates_es_humano": True
}

# Regla deductiva
if hechos_generales["todos_los_humanos_son_mortales"] and hechos_generales["socrates_es_humano"]:
    print("DEDUCTIVO: Sócrates es mortal.")

# ------------------ Razonamiento Inductivo ------------------

# Observaciones específicas (experiencias pasadas)
salidas_del_sol = ["lunes", "martes", "miércoles", "jueves", "viernes"]

# Regla general inducida
if len(salidas_del_sol) > 3:
    print("INDUCTIVO: El sol siempre sale (basado en observaciones pasadas).")

# ------------------ Razonamiento Abductivo ------------------

# Observación
suelo_mojado = True
regadera_abierta = False
llovio = True

# Abducción: inferir la causa más probable
if suelo_mojado:
    if llovio:
        causa = "Lluvia"
    elif regadera_abierta:
        causa = "Regadera"
    else:
        causa = "Desconocida"
    print(f"ABDUCTIVO: El suelo está mojado probablemente por: {causa}")
