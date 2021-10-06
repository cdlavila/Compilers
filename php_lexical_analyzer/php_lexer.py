import ply.lex as lex

# Tokens list
tokens = (
    # Arithmetic operators
    'EQUAL',
    'PLUS',
    'PLUSPLUS',
    'PLUSEQUAL',
    'MINUS',
    'MINUSMINUS',
    'MINUSEQUAL',
    'TIMES',
    'DIVIDE',
    # Logical operators
    'OR',
    'AND',
    'XOR',
    # Relational operators
    'LESS',
    'LESSEQUAL',
    'GREATER',
    'GREATEREQUAL',
    'DEQUAL',
    'DISTINT',
    'ISEQUAL',
    # Symbols
    'QUESTION',
    'SEMICOLON',
    'COMMA',
    'LPAREN',
    'RPAREN',
    'LBRACKET',
    'RBRACKET',
    'LBLOCK',
    'RBLOCK',
    'COLON',
    'AMPERSANT',
    'QUOTES',
    'DOT',
    'DOLAR',
    # Reserverd words
    'BREAK',
    'ENDSWITCH',
    'FUNCTION',
    'INCLUDE',
    'REQUIRE',
    'VAR',
    'CONST',
    'DO',
    'ENDWHILE',
    'PRINT',
    'WHILE',
    'CASE',
    'ECHO',
    'ENDFOR',
    'RETURN',
    'ELSE',
    'ENDFOREACH',
    'FOR',
    'IF',
    'NAMESPACE',
    'AS',
    'DEFAULT',
    'ELSEIF',
    'ENDIF',
    'FOREACH',
    'SWITCH',
    # Others
    'ID',
    'NUMBER'
)

# REGULAR EXPRESSIONS RULES FOR SIMPLE TOKENS

# For arithmetic operators
t_EQUAL = r'='
t_PLUS = r'\+'
t_PLUSPLUS = r'\++'
t_PLUSEQUAL = r'\+='
t_MINUS = r'-'
t_MINUSMINUS = r'--'
t_MINUSEQUAL = r'-='
t_TIMES = r'\*'
t_DIVIDE = r'/'

# For logical operators
t_OR = r'or'
t_AND = r'and'
t_XOR = r'xor'

# For relational operators
t_LESS = r'<'
t_LESSEQUAL = r'<='
t_GREATER = r'>'
t_GREATEREQUAL = r'>='
t_DEQUAL = r'!='
t_DISTINT = r'!'
t_ISEQUAL = r'=='

# For symbols
t_QUESTION = r'\?'
t_SEMICOLON = ';'
t_COMMA = r','
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_LBLOCK = r'{'
t_RBLOCK = r'}'
t_COLON = r':'
t_AMPERSANT = r'\&'
t_QUOTES = r'"'
t_DOT = r'\.'
t_DOLAR = r'\$'


# To ignore line breaks
def t_newline(t):
    r"""\n+"""
    t.lexer.lineno += len(t.value)


# To ignore spaces
t_ignore = ' \t'


# For reserved words
# (KAREN) Escribir aquí las expresiones regulares para las palabras reservadas que le tocan
def t_BREAK(t):
    r"""break"""
    return t


def t_ENDSWITCH(t):
    r"""endswitch"""
    return t


def t_FUNCTION(t):
    r"""function"""
    return t


def t_INCLUDE(t):
    r"""include"""
    return t


def t_REQUIRE(t):
    r"""require"""
    return t


def t_VAR(t):
    r"""var"""
    return t


def t_CONST(t):
    r"""const"""
    return t


def t_DO(t):
    r"""do"""
    return t


def t_ENDWHILE(t):
    r"""endwhile"""
    return t


def t_PRINT(t):
    r"""print"""
    return t


def t_WHILE(t):
    r"""while"""
    return t


def t_CASE(t):
    r"""case"""
    return t


def t_ECHO(t):
    r"""echo"""
    return t


def t_ENDFOR(t):
    r"""endfor"""
    return t


def t_RETURN(t):
    r"""return"""
    return t


def t_ELSE(t):
    r"""else"""
    return t


def t_ENDFOREACH(t):
    r"""endforeach"""
    return t


def t_FOR(t):
    r"""for"""
    return t


def t_IF(t):
    r"""if"""
    return t


def t_NAMESPACE(t):
    r"""namespace"""
    return t


def t_AS(t):
    r"""as"""
    return t


def t_DEFAULT(t):
    r"""default"""
    return t


def t_ELSEIF(t):
    r"""elseif"""
    return t


def t_ENDIF(t):
     r"""endif"""
     return t


def t_FOREACH(t):
    r"""foreach"""
    return t


def t_SWITCH(t):
    r"""switch"""
    return t


# For others (ID and NUMBER)

def t_ID(t):
    r"""\w+(_\d\w)*"""
    return t


def t_NUMBER(t):
    r"""\$d(\.\d+)?"""
    t.value = float(t.value)
    return t


# For one line comment with #
def t_comments_oneline(t):
    r"""\#(.)*?\n"""
    t.lexer.lineno += 1


# For one line comment with //
def t_comments_oneline2(t):
    r"""//(.)*?\n"""
    t.lexer.lineno += 1


# For multi-line comment /*...*/
def t_comments_multiline(t):
    r"""/\*(.|\n)*?\*/"""
    t.lexer.lineno += t.value.count('\n')


# For lexical errors
def t_error(t):
    print("Lexical error: " + str(t.value[0]))
    t.lexer.skip(1)


def analyze(code, lexer):
    lexer.input(code)
    while True:
        token = lexer.token()
        if not token:
            break
        print(token)


if __name__ == '__main__':
    # Reads the file with code and print it
    file = 'code.php'
    f = open(file, 'r')
    code = f.read()
    print("\nThis is the analyzed code\n")
    print(code)
    # Performs lexical analysis of the code
    lexer = lex.lex()
    lexer.input(code)
    analyze(code, lexer)
