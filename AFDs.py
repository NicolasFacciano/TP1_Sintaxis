KEYWORDS = {
    "program": "PROGRAM",
    "var": "VAR",
    "int": "INT",
    "bool": "BOOL",
    "true": "TRUE",
    "false": "FALSE",
    "begin": "BEGIN",
    "end": "END",
    "if": "IF",
    "else": "ELSE",
    "goto": "GOTO",
    "let": "LET",
    "not": "NOT",
    "and": "AND",
    "or": "OR"
}
def is_id(cadena):
    if not cadena:
        return False
    if not (cadena[0].isalpha() or cadena[0] == "_"):
        return False
    for c in cadena[1:]:
        if not (c.isalnum() or c == "_"):
            return False
    return True

token_type = KEYWORDS.get(cadena, "ID")

def is_num(cadena):
    return cadena.isdigit()

def is_assign(cadena):
    return cadena == ":="

def is_eq(cadena):
    return cadena == "=="

def is_neq(cadena):
    return cadena == "<>"

def is_le(cadena):
    return cadena == "<="

def is_ge(cadena):
    return cadena == ">="


def is_lt(c): return c == "<"
def is_gt(c): return c == ">"
def is_plus(c): return c == "+"
def is_minus(c): return c == "-"
def is_mult(c): return c == "*"
def is_equal(c): return c == "="
def is_colon(c): return c == ":"
def is_semicolon(c): return c == ";"
def is_dot(c): return c == "."
def is_lparen(c): return c == "("
def is_rparen(c): return c == ")"

