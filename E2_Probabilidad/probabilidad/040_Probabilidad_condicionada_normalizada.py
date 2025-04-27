# Luciano Alejandro Gómez Muñoz 22310214 6E2.

# Breve explicación:
# Este programa calcula la probabilidad condicionada de que llueva (A) dado que está nublado (B).
# Utiliza la fórmula de probabilidad condicionada: P(A|B) = P(A ∩ B) / P(B)
# Luego, normaliza el resultado para asegurarse de que la probabilidad sea válida.

# Probabilidades dadas
P_A = 0.3  # Probabilidad de que llueva (evento A)
P_B = 0.5  # Probabilidad de que esté nublado (evento B)
P_A_intersection_B = 0.2  # Probabilidad de que ambos ocurran (llueva y esté nublado)

# Función para calcular la probabilidad condicionada
def probabilidad_condicionada(P_A_intersection_B, P_B):
    return P_A_intersection_B / P_B

# Calcular la probabilidad condicionada
P_A_dado_B = probabilidad_condicionada(P_A_intersection_B, P_B)
print(f"Probabilidad de que llueva dado que está nublado: {P_A_dado_B:.2f}")

# Normalización (si la probabilidad no suma 1, ajustamos los valores)
# En este caso, vamos a simular que tenemos un conjunto de probabilidades de eventos
eventos = [P_A, P_B, P_A_intersection_B]
suma_probabilidades = sum(eventos)

# Normalización de las probabilidades
normalizadas = [evento / suma_probabilidades for evento in eventos]
print("\nProbabilidades normalizadas:")
print(f"P(A) normalizada: {normalizadas[0]:.2f}")
print(f"P(B) normalizada: {normalizadas[1]:.2f}")
print(f"P(A ∩ B) normalizada: {normalizadas[2]:.2f}")
