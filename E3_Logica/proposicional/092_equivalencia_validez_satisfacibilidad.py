# Luciano Alejandro Gómez Muñoz 22310214 6E2

# -----------------------------------------------------------------
# Evaluación de equivalencia, validez y satisfacibilidad de expresiones lógicas
# -----------------------------------------------------------------
# Este código permite evaluar tres propiedades lógicas fundamentales:
# 1. **Equivalencia**: Si dos expresiones lógicas tienen el mismo valor de verdad en todas las circunstancias.
# 2. **Validez**: Si una expresión lógica es verdadera en todos los posibles escenarios (es válida).
# 3. **Satisfacibilidad**: Si existe al menos un escenario en el que la expresión lógica sea verdadera.

# --------------------------------------------------------------
# Importación de bibliotecas necesarias
# --------------------------------------------------------------
from sympy import symbols, Equivalent, And, Or, Not       # Importa las funciones necesarias de sympy
from sympy.logic.inference import satisfiable            # Importa el método para verificar la satisfacibilidad

# --------------------------------------------------------------
# Definición de las proposiciones simbólicas
# --------------------------------------------------------------
P, Q, R = symbols('P Q R')  # Definimos tres proposiciones: P, Q y R

# --------------------------------------------------------------
# Definición de las expresiones lógicas
# --------------------------------------------------------------
expr1 = And(P, Q)  # La expresión lógica 'P ∧ Q' (P y Q)
expr2 = Or(P, Q)   # La expresión lógica 'P ∨ Q' (P o Q)
expr3 = Not(P)     # La expresión lógica '¬P' (negación de P)

# --------------------------------------------------------------
# Evaluar equivalencia entre dos expresiones
# --------------------------------------------------------------
# Usamos la función Equivalent para verificar si dos expresiones son lógicamente equivalentes.
equivalence = Equivalent(expr1, expr2)  # Verifica si 'expr1' es equivalente a 'expr2'
print(f"¿Son equivalentes '{expr1}' y '{expr2}'? {equivalence}")  # Imprime el resultado de la equivalencia

# --------------------------------------------------------------
# Evaluar validez de las expresiones
# --------------------------------------------------------------
# Evaluamos si una expresión es válida (es decir, si es verdadera en todos los casos posibles)
validity1 = satisfiable(expr1)  # Verifica si 'expr1' es válida
validity2 = satisfiable(expr2)  # Verifica si 'expr2' es válida
print(f"¿Es válida '{expr1}'? {validity1}")  # Imprime si 'expr1' es válida
print(f"¿Es válida '{expr2}'? {validity2}")  # Imprime si 'expr2' es válida

# --------------------------------------------------------------
# Evaluar satisfacibilidad de las expresiones
# --------------------------------------------------------------
# Evaluamos si las expresiones son satisfacibles, es decir, si existe al menos una asignación de valores de verdad
# que haga que la expresión sea verdadera.
satisfiability1 = satisfiable(expr1)  # Verifica si 'expr1' es satisfacible
satisfiability2 = satisfiable(expr2)  # Verifica si 'expr2' es satisfacible
satisfiability3 = satisfiable(expr3)  # Verifica si 'expr3' es satisfacible
print(f"¿Es satisfacible '{expr1}'? {satisfiability1}")  # Imprime si 'expr1' es satisfacible
print(f"¿Es satisfacible '{expr2}'? {satisfiability2}")  # Imprime si 'expr2' es satisfacible
print(f"¿Es satisfacible '{expr3}'? {satisfiability3}")  # Imprime si 'expr3' es satisfacible
