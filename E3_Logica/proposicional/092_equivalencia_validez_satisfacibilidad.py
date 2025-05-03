# Luciano Alejandro Gómez Muñoz 22310214 6E2

# Este código evalúa la equivalencia, validez y satisfacibilidad de expresiones lógicas.

from sympy import symbols, Equivalent, And, Or, Not
from sympy.logic.inference import satisfiable

# Definir proposiciones simbólicas
P, Q, R = symbols('P Q R')

# Definir expresiones lógicas
expr1 = And(P, Q)
expr2 = Or(P, Q)
expr3 = Not(P)

# Evaluar equivalencia
equivalence = Equivalent(expr1, expr2)
print(f"¿Son equivalentes '{expr1}' y '{expr2}'? {equivalence}")

# Evaluar validez
validity1 = satisfiable(expr1)
validity2 = satisfiable(expr2)
print(f"¿Es válida '{expr1}'? {validity1}")
print(f"¿Es válida '{expr2}'? {validity2}")

# Evaluar satisfacibilidad
satisfiability1 = satisfiable(expr1)
satisfiability2 = satisfiable(expr2)
satisfiability3 = satisfiable(expr3)
print(f"¿Es satisfacible '{expr1}'? {satisfiability1}")
print(f"¿Es satisfacible '{expr2}'? {satisfiability2}")
print(f"¿Es satisfacible '{expr3}'? {satisfiability3}")
