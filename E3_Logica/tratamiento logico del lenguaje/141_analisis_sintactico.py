# Luciano Alejandro Gómez Muñoz 22310214

# Analizador sintáctico para expresiones aritméticas utilizando Lark

from lark import Lark

# Definimos la gramática
gramatica = """
    ?start: expr
    ?expr: expr "+" term   -> suma
         | expr "-" term   -> resta
         | term
    ?term: term "*" factor -> multiplicacion
         | term "/" factor -> division
         | factor
    ?factor: NUMBER        -> numero
           | "(" expr ")"
    %import common.NUMBER
    %import common.WS_INLINE
    %ignore WS_INLINE
"""

# Creamos el analizador
analizador = Lark(gramatica, parser='lalr')

# Analizamos una expresión
arbol = analizador.parse("3 + 4 * (2 - 1)")
print(arbol.pretty())
