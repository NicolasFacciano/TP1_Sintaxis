# AFD para identificadores (ID)
def afd_id(cadena):
    if not cadena:
        return False
    if not cadena[0].isalpha():
        return False
    for c in cadena[1:]:
        if not (c.isalnum()):
            return False
    return True

# AFD para números (NUM)
def afd_num(cadena):
    return cadena.isdigit()

# Palabras clave individuales (según AFDs del TP)

def afd_program(cadena): return cadena == "program"
def afd_var(cadena): return cadena == "var"
def afd_int(cadena): return cadena == "int"
def afd_bool(cadena): return cadena == "bool"
def afd_true(cadena): return cadena == "true"
def afd_false(cadena): return cadena == "false"
def afd_begin(cadena): return cadena == "begin"
def afd_end(cadena): return cadena == "end"
def afd_if(cadena): return cadena == "if"
def afd_else(cadena): return cadena == "else"
def afd_goto(cadena): return cadena == "goto"
def afd_let(cadena): return cadena == "let"
def afd_not(cadena): return cadena == "not"
def afd_and(cadena): return cadena == "and"
def afd_or(cadena): return cadena == "or"

# Operadores compuestos
def afd_assign(cadena): return cadena == ":="
def afd_eq(cadena): return cadena == "=="
def afd_neq(cadena): return cadena == "<>"
def afd_le(cadena): return cadena == "<="
def afd_ge(cadena): return cadena == ">="

# Operadores simples y signos
def afd_plus(c): return c == "+"
def afd_minus(c): return c == "-"
def afd_mult(c): return c == "*"
def afd_colon(c): return c == ":"
def afd_semicolon(c): return c == ";"
def afd_dot(c): return c == "."
def afd_equal(c): return c == "="
def afd_lt(c): return c == "<"
def afd_gt(c): return c == ">"
def afd_lparen(c): return c == "("
def afd_rparen(c): return c == ")"

