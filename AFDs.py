ESTADO_FINAL = "ESTADO FINAL"
ESTADO_NO_FINAL = "NO ACEPTADO"
ESTADO_TRAMPA = "EN ESTADO TRAMPA"

# SUG: Considerar filtrar o ignorar tokens WHITESPACE si no son necesarios para simplificar flujo.
# SUG: Cachear len(codigo_fuente) y evitar recalcular en cada iteración del lexer.
# SUG: Podríamos usar un trie o expresiones regulares precompiladas para optimizar la búsqueda de tokens.
# SUG: Renombrar variables (start, end) para mejorar claridad del control de posición.
# SUG: Romper la construcción de resultados al primer ESTADO_TRAMPA completo para ahorrar ciclos.

# Definiciones de autómatas para cada token
# Autómata para espacios en blanco (incluye espacios, tabulaciones y saltos de línea)
def automata_whitespace(lexema):
    estado = 0
    for c in lexema:
        if estado == 0 and c in (' ', '\n', '\t'):
            estado = 1
        elif estado == 1 and c in (' ', '\n', '\t'):
            estado = 1
        else:
            return ESTADO_TRAMPA
    return ESTADO_FINAL

# Autómata para identificadores (ID) con soporte de guión bajo
def automata_id(lexema):
    estado = 0
    for c in lexema:
        if estado == 0 and (c.isalpha() or c == '_'):
            estado = 1
        elif estado == 1 and (c.isalnum() or c == '_'):
            estado = 1
        else:
            return ESTADO_TRAMPA
    return ESTADO_FINAL if estado == 1 else ESTADO_NO_FINAL

# Autómata para números (NUM)
def automata_num(lexema):
    estado = 0
    for c in lexema:
        if estado == 0 and c.isdigit():
            estado = 1
        elif estado == 1 and c.isdigit():
            estado = 1
        else:
            return ESTADO_TRAMPA
    return ESTADO_FINAL if estado == 1 else ESTADO_NO_FINAL

# Autómatas para operadores compuestos
def automata_assign(lexema): return ESTADO_FINAL if lexema == ":=" else ESTADO_TRAMPA
def automata_eq(lexema):     return ESTADO_FINAL if lexema == "==" else ESTADO_TRAMPA
def automata_neq(lexema):    return ESTADO_FINAL if lexema == "<>" else ESTADO_TRAMPA
def automata_le(lexema):     return ESTADO_FINAL if lexema == "<=" else ESTADO_TRAMPA
def automata_ge(lexema):     return ESTADO_FINAL if lexema == ">=" else ESTADO_TRAMPA

# Autómatas para operadores simples y símbolos
def automata_plus(lexema):     return ESTADO_FINAL if lexema == "+" else ESTADO_TRAMPA
def automata_minus(lexema):    return ESTADO_FINAL if lexema == "-" else ESTADO_TRAMPA
def automata_mult(lexema):     return ESTADO_FINAL if lexema == "*" else ESTADO_TRAMPA
def automata_colon(lexema):    return ESTADO_FINAL if lexema == ":" else ESTADO_TRAMPA
def automata_semicolon(lexema):return ESTADO_FINAL if lexema == ";" else ESTADO_TRAMPA
def automata_dot(lexema):      return ESTADO_FINAL if lexema == "." else ESTADO_TRAMPA
def automata_equal(lexema):    return ESTADO_FINAL if lexema == "=" else ESTADO_TRAMPA
def automata_lt(lexema):       return ESTADO_FINAL if lexema == "<" else ESTADO_TRAMPA
def automata_gt(lexema):       return ESTADO_FINAL if lexema == ">" else ESTADO_TRAMPA
def automata_lparen(lexema):   return ESTADO_FINAL if lexema == "(" else ESTADO_TRAMPA
def automata_rparen(lexema):   return ESTADO_FINAL if lexema == ")" else ESTADO_TRAMPA

# Mapeo de palabras clave para reclasificar IDs
KEYWORDS = {
    "program": "PROGRAM", "var": "VAR",   "int": "INT",
    "bool": "BOOL",     "true": "TRUE", "false": "FALSE",
    "begin": "BEGIN",   "end": "END",   "if": "IF",
    "else": "ELSE",     "goto": "GOTO", "let": "LET",
    "not": "NOT",       "and": "AND",   "or": "OR"
}

# Lista de tokens con sus autómatas (ordenados por precedencia)
TOKENS_POSIBLES = [
    ("WHITESPACE", automata_whitespace),
    ("ASSIGN",     automata_assign),
    ("EQ",         automata_eq),
    ("NEQ",        automata_neq),
    ("LE",         automata_le),
    ("GE",         automata_ge),
    ("PLUS",       automata_plus),
    ("MINUS",      automata_minus),
    ("MULT",       automata_mult),
    ("COLON",      automata_colon),
    ("SEMICOLON",  automata_semicolon),
    ("DOT",        automata_dot),
    ("EQUAL",      automata_equal),
    ("LT",         automata_lt),
    ("GT",         automata_gt),
    ("LPAREN",     automata_lparen),
    ("RPAREN",     automata_rparen),
    ("NUM",        automata_num),
    ("ID",         automata_id),
]

# Lexer principal con corrección de gestión de posibles tokens
def lexer(codigo_fuente):
    tokens = []
    posicion = 0
    total_len = len(codigo_fuente)

    while posicion < total_len:
        start = posicion
        best_lexema = ''
        best_tokens = []
        end = start

        # Consumir la longitud máxima posible
        while end < total_len:
            lexema = codigo_fuente[start:end+1]
            # SUG: Romper al primer estado trampa completo en vez de recolectar todos
            results = [(name, afd(lexema)) for name, afd in TOKENS_POSIBLES]
            if any(res != ESTADO_TRAMPA for _, res in results):
                finals = [name for name, res in results if res == ESTADO_FINAL]
                if finals:
                    best_tokens = finals
                    best_lexema = lexema
                end += 1
            else:
                break

        if not best_tokens:
            bad = codigo_fuente[start:end]
            raise Exception(f"ERROR LÉXICO: '{bad}' no reconocido")

        token_type = best_tokens[0]
        if token_type == "ID":
            token_type = KEYWORDS.get(best_lexema, "ID")

        tokens.append((token_type, best_lexema))
        posicion = start + len(best_lexema)

    return tokens

# Ejemplos de pruebas adicionales def run_tests():

def run_tests():
    ejemplos = [
        "   \t\n",               # whitespace puro
        "123 456",                # números
        "foo bar1 _baz qux_123",  # identificadores con underscore
        ":= == <> <= >= + - * /", # el '/' debe fallar
        "program x := 42 ; if x == 42 goto L1 ; end"
    ]
    for codigo in ejemplos:
        print(f"\nEntrada: {repr(codigo)}")
        try:
            for tk in lexer(codigo):
                print("  ", tk)
        except Exception as e:
            print("  ", e)

if __name__ == "__main__":
    run_tests()
