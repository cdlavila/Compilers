import ply.lex as lex

# Tokens list
tokens = (
    # PHP main tag
    'OPENMAINTAG',
    'CLOSEMAINTAG'
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
    'DOLAR'
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
# For PHP main tag
t_OPENMAINTAG = r'<?php'
T_CLOSEMAINTAG = r'?>'

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
t_LEESEQUAL = r'<='
t_GREATER = r'>'
t_GREATEREQUAL = r'>='
t_DEQUAL = r'!='
t_DISTINT = r'!'
t_ISEQUAL = r'/=='

# For symbols
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
t_DOLAR = r'$'

# To ignore line breaks
t_ignore = ' \t'

# For reserved words
# (KAREN) Escribir aquí las expresiones regulares para las palabras reservadas que le tocan


# (JUAN CAMILO) Escribir aquí las expresiones regulares para las palabras reservadas que le tocan


# For others (ID and NUMBER)
# (JUAN CAMILO) Escribir aquí las expresiones regulares para ID y NUMBER


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
    print("This is the analyzed code\n")
    print(code)
    # Performs lexical analysis of the code
    lexer = lex.lex()
    lexer.input(code)
    analyze(code, lexer)
