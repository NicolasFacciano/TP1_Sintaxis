# Lexer para TINY sin usar funciones auxiliares "is..."

ESTADO_FINAL = "ESTADO_FINAL"
ESTADO_TRAMPA = "ESTADO_TRAMPA"

def automata_id(lexema):
    estado = 0
    for c in lexema:
        # letra: 'a'..'z' o 'A'..'Z', o guión bajo
        if estado == 0 and (('a' <= c <= 'z') or ('A' <= c <= 'Z') or c == "_"):
            estado = 1
        # alfanumérico: letra, dígito '0'..'9', o '_'
        elif estado == 1 and (( 'a' <= c <= 'z') or ('A' <= c <= 'Z') or ('0' <= c <= '9') or c == "_"):
            estado = 1
        else:
            return ESTADO_TRAMPA
    return ESTADO_FINAL if estado == 1 else ESTADO_TRAMPA

def automata_num(lexema):
    estado = 0
    for c in lexema:
        # dígito '0'..'9'
        if estado == 0 and ('0' <= c <= '9'):
            estado = 1
        elif estado == 1 and ('0' <= c <= '9'):
            estado = 1
        else:
            return ESTADO_TRAMPA
    return ESTADO_FINAL if estado == 1 else ESTADO_TRAMPA

# Palabras clave
def automata_program(lex): return ESTADO_FINAL if lex == "program" else ESTADO_TRAMPA
def automata_var(lex):     return ESTADO_FINAL if lex == "var"     else ESTADO_TRAMPA
def automata_int(lex):     return ESTADO_FINAL if lex == "int"     else ESTADO_TRAMPA
def automata_bool(lex):    return ESTADO_FINAL if lex == "bool"    else ESTADO_TRAMPA
def automata_true(lex):    return ESTADO_FINAL if lex == "true"    else ESTADO_TRAMPA
def automata_false(lex):   return ESTADO_FINAL if lex == "false"   else ESTADO_TRAMPA
def automata_begin(lex):   return ESTADO_FINAL if lex == "begin"   else ESTADO_TRAMPA
def automata_end(lex):     return ESTADO_FINAL if lex == "end"     else ESTADO_TRAMPA
def automata_if(lex):      return ESTADO_FINAL if lex == "if"      else ESTADO_TRAMPA
def automata_else(lex):    return ESTADO_FINAL if lex == "else"    else ESTADO_TRAMPA
def automata_goto(lex):    return ESTADO_FINAL if lex == "goto"    else ESTADO_TRAMPA
def automata_let(lex):     return ESTADO_FINAL if lex == "let"     else ESTADO_TRAMPA
def automata_not(lex):     return ESTADO_FINAL if lex == "not"     else ESTADO_TRAMPA
def automata_and(lex):     return ESTADO_FINAL if lex == "and"     else ESTADO_TRAMPA
def automata_or(lex):      return ESTADO_FINAL if lex == "or"      else ESTADO_TRAMPA

# Operadores compuestos
def automata_assign(lex):  return ESTADO_FINAL if lex == ":=" else ESTADO_TRAMPA
def automata_eq(lex):      return ESTADO_FINAL if lex == "==" else ESTADO_TRAMPA
def automata_neq(lex):     return ESTADO_FINAL if lex == "<>" else ESTADO_TRAMPA
def automata_le(lex):      return ESTADO_FINAL if lex == "<=" else ESTADO_TRAMPA
def automata_ge(lex):      return ESTADO_FINAL if lex == ">=" else ESTADO_TRAMPA

# Operadores simples y puntuación
def automata_plus(lex):    return ESTADO_FINAL if lex == "+"   else ESTADO_TRAMPA
def automata_minus(lex):   return ESTADO_FINAL if lex == "-"   else ESTADO_TRAMPA
def automata_mult(lex):    return ESTADO_FINAL if lex == "*"   else ESTADO_TRAMPA
def automata_colon(lex):   return ESTADO_FINAL if lex == ":"   else ESTADO_TRAMPA
def automata_semicolon(lex):return ESTADO_FINAL if lex == ";"   else ESTADO_TRAMPA
def automata_dot(lex):     return ESTADO_FINAL if lex == "."   else ESTADO_TRAMPA
def automata_equal(lex):   return ESTADO_FINAL if lex == "="   else ESTADO_TRAMPA
def automata_lt(lex):      return ESTADO_FINAL if lex == "<"   else ESTADO_TRAMPA
def automata_gt(lex):      return ESTADO_FINAL if lex == ">"   else ESTADO_TRAMPA
def automata_lparen(lex):  return ESTADO_FINAL if lex == "("   else ESTADO_TRAMPA
def automata_rparen(lex):  return ESTADO_FINAL if lex == ")"   else ESTADO_TRAMPA

# Lista de tokens con precedencia
TOKENS_POSIBLES = [
    ("PROGRAM", automata_program),
    ("VAR",     automata_var),
    ("INT",     automata_int),
    ("BOOL",    automata_bool),
    ("TRUE",    automata_true),
    ("FALSE",   automata_false),
    ("BEGIN",   automata_begin),
    ("END",     automata_end),
    ("IF",      automata_if),
    ("ELSE",    automata_else),
    ("GOTO",    automata_goto),
    ("LET",     automata_let),
    ("NOT",     automata_not),
    ("AND",     automata_and),
    ("OR",      automata_or),
    ("ASSIGN",  automata_assign),
    ("EQ",      automata_eq),
    ("NEQ",     automata_neq),
    ("LE",      automata_le),
    ("GE",      automata_ge),
    ("PLUS",    automata_plus),
    ("MINUS",   automata_minus),
    ("MULT",    automata_mult),
    ("LPAREN",  automata_lparen),
    ("RPAREN",  automata_rparen),
    ("SEMICOLON",automata_semicolon),
    ("DOT",     automata_dot),
    ("COLON",   automata_colon),
    ("EQUAL",   automata_equal),
    ("LT",      automata_lt),
    ("GT",      automata_gt),
    ("ID",      automata_id),
    ("NUM",     automata_num),
]

def lexer(codigo):
    tokens = []
    i = 0
    n = len(codigo)
    while i < n:
        # Espacios: comparar directamente
        c = codigo[i]
        if c == ' ' or c == '\t' or c == '\n' or c == '\r':
            i += 1
            continue
        start = i
        last_match = None
        j = i
        while j < n:
            lexema = codigo[start:j+1]
            any_non_trap = False
            matches = []
            for idx, (tok, afd) in enumerate(TOKENS_POSIBLES):
                res = afd(lexema)
                if res != ESTADO_TRAMPA:
                    any_non_trap = True
                    if res == ESTADO_FINAL:
                        matches.append((idx, tok))
            if not any_non_trap:
                break
            if matches:
                idx_min, tok_sel = min(matches, key=lambda x: x[0])
                last_match = (tok_sel, lexema, j+1-start)
            j += 1
        if last_match is None:
            raise Exception(f"ERROR LÉXICO: '{codigo[start]}' no reconocido")
        tok, lexeme, length = last_match
        tokens.append((tok, lexeme))
        i += length
    return tokens

# ==== Tests ====

def run_tests():
    casos = [
        ("program p1 .",                  [("PROGRAM","program"),("ID","p1"),("DOT",".")]),
        ("var _x1 ;",                     [("VAR","var"),("ID","_x1"),("SEMICOLON",";")]),
        ("let x := 100 + 20 ;",          [("LET","let"),("ID","x"),("ASSIGN",":="),("NUM","100"),("PLUS","+"),("NUM","20"),("SEMICOLON",";")]),
        ("if x>=10 goto L1 ;",           [("IF","if"),("ID","x"),("GE",">="),("NUM","10"),("GOTO","goto"),("ID","L1"),("SEMICOLON",";")]),
        ("x<>y",                          [("ID","x"),("NEQ","<>"),("ID","y")]),
        ("123",                           [("NUM","123")]),
        ("1a",                            [("NUM","1"),("ID","a")]),
        ("$",                             Exception),
        ("#",                             Exception),
        ("(a)",                           [("LPAREN","("),("ID","a"),("RPAREN",")")]),
        ("and_or",                        [("ID","and_or")]),
    ]
    for codigo, esperado in casos:
        try:
            salida = lexer(codigo)
            assert salida == esperado, f"FALLÓ: {codigo} -> {salida}, esperado {esperado}"
        except Exception as e:
            assert esperado is Exception, f"FALLÓ EXCEPCIÓN: {codigo} -> {e}"
    print("Todas las pruebas pasaron.")

if __name__ == "__main__":
    run_tests()
    print("Ejemplo:", lexer("bool flag = true ;"))

