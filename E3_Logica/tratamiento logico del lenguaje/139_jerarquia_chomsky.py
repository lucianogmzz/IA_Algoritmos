# Luciano Alejandro Gómez Muñoz 22310214

# Ejemplo de gramática regular (Tipo 3) utilizando expresiones regulares

import re

# Definimos una expresión regular que representa la gramática:
# L = { a^n b^n | n ≥ 1 } no es regular, pero para el ejemplo usaremos una expresión regular simple
# L = { a^n b^m | n ≥ 1, m ≥ 1 }

# Patrón: una o más 'a' seguidas de una o más 'b'
pattern = re.compile(r'^a+b+$')

# Lista de cadenas para probar
cadenas = ['ab', 'aabbb', 'aaab', 'bba', 'aabbc']

# Verificamos cuáles cadenas pertenecen al lenguaje definido por la gramática
for cadena in cadenas:
    if pattern.fullmatch(cadena):
        print(f"'{cadena}' pertenece al lenguaje.")
    else:
        print(f"'{cadena}' NO pertenece al lenguaje.")
