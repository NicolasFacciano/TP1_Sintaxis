# Código completo con tests y ejemplo de ejecución

ESTADO_FINAL = "ESTADO_FINAL"
ESTADO_TRAMPA = "ESTADO_TRAMPA"

def automata_id(lexema):
    estado = 0
    for c in lexema:
        if estado == 0 and (c.isalpha() or c == "_"):
            estado = 1
        elif estado == 1 and (c.isalnum() or c == "_"):
            estado = 1
        else:
            return ESTADO_TRAMPA
    return ESTADO_FINAL if estado == 1 else ESTADO_TRAMPA

def automata_num(lexema):
    estado = 0
    for c in lexema:
        if estado == 0 and c.isdigit():
            estado = 1
        elif estado == 1 and c.isdigit():
            estado = 1
        else:
            return ESTADO_TRAMPA
    return ESTADO_FINAL if estado == 1 else ESTADO_TRAMPA

def automata_program(lexema): return ESTADO_FINAL if lexema == "program" else ESTADO_TRAMPA
def automata_var(lexema):     return ESTADO_FINAL if lexema == "var"     else ESTADO_TRAMPA
def automata_int(lexema):     return ESTADO_FINAL if lexema == "int"     else ESTADO_TRAMPA
def automata_bool(lexema):    return ESTADO_FINAL if lexema == "bool"    else ESTADO_TRAMPA
def automata_true(lexema):    return ESTADO_FINAL if lexema == "true"    else ESTADO_TRAMPA
def automata_false(lexema):   return ESTADO_FINAL if lexema == "false"   else ESTADO_TRAMPA
def automata_begin(lexema):   return ESTADO_FINAL if lexema == "begin"   else ESTADO_TRAMPA
def automata_end(lexema):     return ESTADO_FINAL if lexema == "end"     else ESTADO_TRAMPA
def automata_if(lexema):      return ESTADO_FINAL if lexema == "if"      else ESTADO_TRAMPA
def automata_else(lexema):    return ESTADO_FINAL if lexema == "else"    else ESTADO_TRAMPA
def automata_goto(lexema):    return ESTADO_FINAL if lexema == "goto"    else ESTADO_TRAMPA
def automata_let(lexema):     return ESTADO_FINAL if lexema == "let"     else ESTADO_TRAMPA
def automata_not(lexema):     return ESTADO_FINAL if lexema == "not"     else ESTADO_TRAMPA
def automata_and(lexema):     return ESTADO_FINAL if lexema == "and"     else ESTADO_TRAMPA
def automata_or(lexema):      return ESTADO_FINAL if lexema == "or"      else ESTADO_TRAMPA

def automata_assign(lexema):  return ESTADO_FINAL if lexema == ":=" else ESTADO_TRAMPA
def automata_eq(lexema):      return ESTADO_FINAL if lexema == "==" else ESTADO_TRAMPA
def automata_neq(lexema):     return ESTADO_FINAL if lexema == "<>" else ESTADO_TRAMPA
def automata_le(lexema):      return ESTADO_FINAL if lexema == "<=" else ESTADO_TRAMPA
def automata_ge(lexema):      return ESTADO_FINAL if lexema == ">=" else ESTADO_TRAMPA

def automata_plus(lexema):    return ESTADO_FINAL if lexema == "+"   else ESTADO_TRAMPA
def automata_minus(lexema):   return ESTADO_FINAL if lexema == "-"   else ESTADO_TRAMPA
def automata_mult(lexema):    return ESTADO_FINAL if lexema == "*"   else ESTADO_TRAMPA
def automata_colon(lexema):   return ESTADO_FINAL if lexema == ":"   else ESTADO_TRAMPA
def automata_semicolon(lexema):return ESTADO_FINAL if lexema == ";"   else ESTADO_TRAMPA
def automata_dot(lexema):     return ESTADO_FINAL if lexema == "."   else ESTADO_TRAMPA
def automata_equal(lexema):   return ESTADO_FINAL if lexema == "="   else ESTADO_TRAMPA
def automata_lt(lexema):      return ESTADO_FINAL if lexema == "<"   else ESTADO_TRAMPA
def automata_gt(lexema):      return ESTADO_FINAL if lexema == ">"   else ESTADO_TRAMPA
def automata_lparen(lexema):  return ESTADO_FINAL if lexema == "("   else ESTADO_TRAMPA
def automata_rparen(lexema):  return ESTADO_FINAL if lexema == ")"   else ESTADO_TRAMPA

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

def lexer(codigo_fuente):
    tokens = []
    i, n = 0, len(codigo_fuente)
    while i < n:
        if codigo_fuente[i].isspace():
            i += 1; continue
        start, last = i, None
        j = i
        while j < n:
            lexema = codigo_fuente[start:j+1]
            any_non_trap = False; matches = []
            for idx, (tok, afd) in enumerate(TOKENS_POSIBLES):
                res = afd(lexema)
                if res != ESTADO_TRAMPA:
                    any_non_trap = True
                    if res == ESTADO_FINAL:
                        matches.append((idx, tok))
            if not any_non_trap: break
            if matches:
                idx_min, tok_sel = min(matches, key=lambda x: x[0])
                last = (tok_sel, lexema, j+1-start)
            j += 1
        if last is None:
            raise Exception(f"ERROR LÉXICO: '{codigo_fuente[start]}' no reconocido")
        token, lexeme, length = last
        tokens.append((token, lexeme))
        i += length
    return tokens

# ==== Función de tests ====
def run_tests():
    casos = [
        ("program p1 .",                  [("PROGRAM","program"),("ID","p1"),("DOT",".")]),
        ("program myProg . begin end",    [("PROGRAM","program"),("ID","myProg"),
                                          ("DOT","."),("BEGIN","begin"),("END","end")]),
        ("var _x1 ;",                     [("VAR","var"),("ID","_x1"),("SEMICOLON",";")]),
        ("let x := 100 + 20 ;",          [("LET","let"),("ID","x"),("ASSIGN",":="),
                                          ("NUM","100"),("PLUS","+"),("NUM","20"),
                                          ("SEMICOLON",";")]),
        ("let flag = true and false ;",  [("LET","let"),("ID","flag"),("EQUAL","="),
                                          ("TRUE","true"),("AND","and"),("FALSE","false"),
                                          ("SEMICOLON",";")]),
        ("if x>=10 goto L1 ;",           [("IF","if"),("ID","x"),("GE",">="),
                                          ("NUM","10"),("GOTO","goto"),("ID","L1"),
                                          ("SEMICOLON",";")]),
        ("x<>y",                          [("ID","x"),("NEQ","<>"),("ID","y")]),
        ("x<=y",                          [("ID","x"),("LE","<="),("ID","y")]),
        ("(a)",                           [("LPAREN","("),("ID","a"),("RPAREN",")")]),
        ("1a",                            [("NUM","1"),("ID","a")]),
        ("123",                           [("NUM","123")]),
        ("12a",                           [("NUM","12"),("ID","a")]),
        ("$",                             Exception),
        ("#",                             Exception),
    ]
    for codigo, esperado in casos:
        try:
            salida = lexer(codigo)
            assert salida == esperado, f"FALLÓ: {codigo} -> {salida}, esperado {esperado}"
        except Exception as e:
            assert esperado is Exception, f"FALLÓ EXCEPCIÓN: {codigo} -> {e}"
    print("Todas las pruebas pasaron.")

# ==== Ejecutar tests y ejemplo ====
if __name__ == "__main__":
    run_tests()
    print("Ejemplo:", lexer("bool flag = true ;"))
