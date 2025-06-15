ESTADO_FINAL = "ESTADO FINAL"
ESTADO_NO_FINAL = "NO ACEPTADO"
ESTADO_TRAMPA = "EN ESTADO TRAMPA"

# Automata para "program"
def automata_program(lexema):
    estado = 0
    estados_finales = [7]
    for caracter in lexema:
        if estado == 0 and caracter == 'p':
            estado = 1
        elif estado == 1 and caracter == 'r':
            estado = 2
        elif estado == 2 and caracter == 'o':
            estado = 3
        elif estado == 3 and caracter == 'g':
            estado = 4
        elif estado == 4 and caracter == 'r':
            estado = 5
        elif estado == 5 and caracter == 'a':
            estado = 6
        elif estado == 6 and caracter == 'm':
            estado = 7
        else:
            estado = -1
            break
    if estado == -1:
        return ESTADO_TRAMPA
    if estado in estados_finales:
        return ESTADO_FINAL
    return ESTADO_NO_FINAL

# Automata para "var"
def automata_var(lexema):
    estado = 0
    estados_finales = [3]
    for caracter in lexema:
        if estado == 0 and caracter == 'v':
            estado = 1
        elif estado == 1 and caracter == 'a':
            estado = 2
        elif estado == 2 and caracter == 'r':
            estado = 3
        else:
            estado = -1
            break
    if estado == -1:
        return ESTADO_TRAMPA
    if estado in estados_finales:
        return ESTADO_FINAL
    return ESTADO_NO_FINAL

# Automata para "int"
def automata_int(lexema):
    estado = 0
    estados_finales = [3]
    for caracter in lexema:
        if estado == 0 and caracter == 'i':
            estado = 1
        elif estado == 1 and caracter == 'n':
            estado = 2
        elif estado == 2 and caracter == 't':
            estado = 3
        else:
            estado = -1
            break
    if estado == -1:
        return ESTADO_TRAMPA
    if estado in estados_finales:
        return ESTADO_FINAL
    return ESTADO_NO_FINAL

# Automata para "bool"
def automata_bool(lexema):
    estado = 0
    estados_finales = [4]
    for caracter in lexema:
        if estado == 0 and caracter == 'b':
            estado = 1
        elif estado == 1 and caracter == 'o':
            estado = 2
        elif estado == 2 and caracter == 'o':
            estado = 3
        elif estado == 3 and caracter == 'l':
            estado = 4
        else:
            estado = -1
            break
    if estado == -1:
        return ESTADO_TRAMPA
    if estado in estados_finales:
        return ESTADO_FINAL
    return ESTADO_NO_FINAL

# Automata para "true"
def automata_true(lexema):
    estado = 0
    estados_finales = [4]
    for caracter in lexema:
        if estado == 0 and caracter == 't':
            estado = 1
        elif estado == 1 and caracter == 'r':
            estado = 2
        elif estado == 2 and caracter == 'u':
            estado = 3
        elif estado == 3 and caracter == 'e':
            estado = 4
        else:
            estado = -1
            break
    if estado == -1:
        return ESTADO_TRAMPA
    if estado in estados_finales:
        return ESTADO_FINAL
    return ESTADO_NO_FINAL

# Automata para "false"
def automata_false(lexema):
    estado = 0
    estados_finales = [5]
    for caracter in lexema:
        if estado == 0 and caracter == 'f':
            estado = 1
        elif estado == 1 and caracter == 'a':
            estado = 2
        elif estado == 2 and caracter == 'l':
            estado = 3
        elif estado == 3 and caracter == 's':
            estado = 4
        elif estado == 4 and caracter == 'e':
            estado = 5
        else:
            estado = -1
            break
    if estado == -1:
        return ESTADO_TRAMPA
    if estado in estados_finales:
        return ESTADO_FINAL
    return ESTADO_NO_FINAL

# Automata para "begin"
def automata_begin(lexema):
    estado = 0
    estados_finales = [5]
    for caracter in lexema:
        if estado == 0 and caracter == 'b':
            estado = 1
        elif estado == 1 and caracter == 'e':
            estado = 2
        elif estado == 2 and caracter == 'g':
            estado = 3
        elif estado == 3 and caracter == 'i':
            estado = 4
        elif estado == 4 and caracter == 'n':
            estado = 5
        else:
            estado = -1
            break
    if estado == -1:
        return ESTADO_TRAMPA
    if estado in estados_finales:
        return ESTADO_FINAL
    return ESTADO_NO_FINAL

# Automata para "end"
def automata_end(lexema):
    estado = 0
    estados_finales = [3]
    for caracter in lexema:
        if estado == 0 and caracter == 'e':
            estado = 1
        elif estado == 1 and caracter == 'n':
            estado = 2
        elif estado == 2 and caracter == 'd':
            estado = 3
        else:
            estado = -1
            break
    if estado == -1:
        return ESTADO_TRAMPA
    if estado in estados_finales:
        return ESTADO_FINAL
    return ESTADO_NO_FINAL

# Automata para "if"
def automata_if(lexema):
    estado = 0
    estados_finales = [2]
    for caracter in lexema:
        if estado == 0 and caracter == 'i':
            estado = 1
        elif estado == 1 and caracter == 'f':
            estado = 2
        else:
            estado = -1
            break
    if estado == -1:
        return ESTADO_TRAMPA
    if estado in estados_finales:
        return ESTADO_FINAL
    return ESTADO_NO_FINAL

# Automata para "else"
def automata_else(lexema):
    estado = 0
    estados_finales = [4]
    for caracter in lexema:
        if estado == 0 and caracter == 'e':
            estado = 1
        elif estado == 1 and caracter == 'l':
            estado = 2
        elif estado == 2 and caracter == 's':
            estado = 3
        elif estado == 3 and caracter == 'e':
            estado = 4
        else:
            estado = -1
            break
    if estado == -1:
        return ESTADO_TRAMPA
    if estado in estados_finales:
        return ESTADO_FINAL
    return ESTADO_NO_FINAL

# Automata para "not"
def automata_not(lexema):
    estado = 0
    estados_finales = [3]
    for caracter in lexema:
        if estado == 0 and caracter == 'n':
            estado = 1
        elif estado == 1 and caracter == 'o':
            estado = 2
        elif estado == 2 and caracter == 't':
            estado = 3
        else:
            estado = -1
            break
    if estado == -1:
        return ESTADO_TRAMPA
    if estado in estados_finales:
        return ESTADO_FINAL
    return ESTADO_NO_FINAL

# Automata para "goto"
def automata_goto(lexema):
    estado = 0
    estados_finales = [4]
    for caracter in lexema:
        if estado == 0 and caracter == 'g':
            estado = 1
        elif estado == 1 and caracter == 'o':
            estado = 2
        elif estado == 2 and caracter == 't':
            estado = 3
        elif estado == 3 and caracter == 'o':
            estado = 4
        else:
            estado = -1
            break
    if estado == -1:
        return ESTADO_TRAMPA
    if estado in estados_finales:
        return ESTADO_FINAL
    return ESTADO_NO_FINAL

# Automata para "let"
def automata_let(lexema):
    estado = 0
    estados_finales = [3]
    for caracter in lexema:
        if estado == 0 and caracter == 'l':
            estado = 1
        elif estado == 1 and caracter == 'e':
            estado = 2
        elif estado == 2 and caracter == 't':
            estado = 3
        else:
            estado = -1
            break
    if estado == -1:
        return ESTADO_TRAMPA
    if estado in estados_finales:
        return ESTADO_FINAL
    return ESTADO_NO_FINAL


# Automata para <num> (solo dígitos)
def automata_num(lexema):
    estado = 0
    estados_finales = [1]
    for caracter in lexema:
        if estado == 0 and '0' <= caracter <= '9':
            estado = 1
        elif estado == 1 and '0' <= caracter <= '9':
            estado = 1
        else:
            estado = -1
            break
    if estado == -1:
        return ESTADO_TRAMPA
    if estado in estados_finales:
        return ESTADO_FINAL
    return ESTADO_NO_FINAL

# Automata para <id> (letra seguida de letras o números)
def es_letra(c):
    return ('a' <= c <= 'z') or ('A' <= c <= 'Z')

def es_digito(c):
    return '0' <= c <= '9'

def automata_id(lexema):
    estado = 0
    estados_finales = [1]
    for caracter in lexema:
        if estado == 0 and es_letra(caracter):
            estado = 1
        elif estado == 1 and (es_letra(caracter) or es_digito(caracter)):
            estado = 1
        else:
            estado = -1
            break
    if estado == -1:
        return ESTADO_TRAMPA
    if estado in estados_finales:
        return ESTADO_FINAL
    return ESTADO_NO_FINAL


# Automata para espacios, tab y salto de línea (para ignorar)
def automata_espacio(lexema):
    estados_finales = [1]
    estado = 0
    for c in lexema:
        if estado == 0 and c in [' ', '\t', '\n']:
            estado = 1
        elif estado == 1 and c in [' ', '\t', '\n']:
            estado = 1
        else:
            estado = -1
            break
    if estado == -1:
        return ESTADO_TRAMPA
    if estado in estados_finales:
        return ESTADO_FINAL
    return ESTADO_NO_FINAL


TOKENS_POSIBLES = [
    ("ESPACIO", automata_espacio),
    ("program", automata_program),
    ("var", automata_var),
    ("int", automata_int),
    ("bool", automata_bool),
    ("true", automata_true),
    ("false", automata_false),
    ("begin", automata_begin),
    ("end", automata_end),
    ("if", automata_if),
    ("else", automata_else),
    ("not", automata_not),
    ("goto", automata_goto),
    ("let", automata_let),
    ("num", automata_num),
    ("id", automata_id),
]

def lexer(codigo_fuente):
    tokens = []
    posicion_actual = 0
    while posicion_actual < len(codigo_fuente):
        comienzo_lexema = posicion_actual
        posibles_tokens = []
        posibles_tokens_con_un_caracter_mas = []
        lexema = ""
        var_aux_todos_en_estado_trampa = False

        while not var_aux_todos_en_estado_trampa and posicion_actual < len(codigo_fuente):
            var_aux_todos_en_estado_trampa = True
            lexema = codigo_fuente[comienzo_lexema:posicion_actual + 1]
            posibles_tokens = posibles_tokens_con_un_caracter_mas
            posibles_tokens_con_un_caracter_mas = []

            for (un_tipo_de_token, afd) in TOKENS_POSIBLES:
                simulacion_afd = afd(lexema)
                if simulacion_afd == ESTADO_FINAL:
                    posibles_tokens_con_un_caracter_mas.append(un_tipo_de_token)
                    var_aux_todos_en_estado_trampa = False
                elif simulacion_afd == ESTADO_NO_FINAL:
                    var_aux_todos_en_estado_trampa = False

            if not var_aux_todos_en_estado_trampa:
                posicion_actual += 1

        if len(posibles_tokens) == 0:
            raise Exception("ERROR:TOKEN DESCONOCIDO '" + lexema + "'")

        un_tipo_de_token = posibles_tokens[0]

        if un_tipo_de_token != "ESPACIO":
            tokens.append((un_tipo_de_token, lexema))

    return tokens


# Prueba:
codigo_prueba = "program var x1 123 if else true false begin end not goto let int bool"
print(lexer(codigo_prueba))
