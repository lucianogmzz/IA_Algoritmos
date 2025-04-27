# Luciano Alejandro Gómez Muñoz 22310214 6E2

# Breve explicación:
# En este ejemplo, implementamos una Red Bayesiana Dinámica simple que modela la evolución de un sistema con el paso del tiempo.
# Tenemos dos variables: 'Estado' que puede ser 'Activo' o 'Inactivo' y 'Fallos' que modela si el sistema ha fallado.
# Vamos a simular su comportamiento a lo largo de dos pasos de tiempo.

# Importamos las librerías necesarias
import numpy as np
import random

# Definimos las probabilidades de transición para las variables en cada paso de tiempo
# Estado en t+1 dado Estado en t (se usa como ejemplo simple de una probabilidad de transición)
P_estado = {
    "Activo": {"Activo": 0.9, "Inactivo": 0.1},  # 90% de probabilidad de mantenerse activo
    "Inactivo": {"Activo": 0.3, "Inactivo": 0.7}  # 30% de probabilidad de pasar de inactivo a activo
}

# Probabilidades de Fallos dado Estado
P_fallos = {
    "Activo": {"Fallos": 0.1, "No Fallos": 0.9},  # 10% de probabilidad de fallo si está activo
    "Inactivo": {"Fallos": 0.7, "No Fallos": 0.3}  # 70% de probabilidad de fallo si está inactivo
}

# Inicialización del sistema en el tiempo 0
estado_t = "Activo"  # Comenzamos con el sistema activo
fallos_t = "No Fallos"  # Inicialmente no hay fallos

# Función para simular un paso de tiempo
def evolucionar_estado(estado_actual):
    # Elegir el siguiente estado basándose en la probabilidad de transición
    proba = P_estado[estado_actual]
    siguiente_estado = random.choices(list(proba.keys()), weights=proba.values())[0]
    return siguiente_estado

def evolucionar_fallos(estado_actual):
    # Elegir si ocurre un fallo basado en el estado actual
    proba = P_fallos[estado_actual]
    fallo = random.choices(list(proba.keys()), weights=proba.values())[0]
    return fallo

# Simulación a lo largo de dos pasos de tiempo
def simular_red_bayesiana_dinamica():
    global estado_t, fallos_t

    print("Tiempo 0:")
    print(f"Estado: {estado_t}, Fallos: {fallos_t}")
    
    # Paso de tiempo 1
    estado_t = evolucionar_estado(estado_t)
    fallos_t = evolucionar_fallos(estado_t)
    print("\nTiempo 1:")
    print(f"Estado: {estado_t}, Fallos: {fallos_t}")
    
    # Paso de tiempo 2
    estado_t = evolucionar_estado(estado_t)
    fallos_t = evolucionar_fallos(estado_t)
    print("\nTiempo 2:")
    print(f"Estado: {estado_t}, Fallos: {fallos_t}")

# Ejecutamos la simulación
simular_red_bayesiana_dinamica()

