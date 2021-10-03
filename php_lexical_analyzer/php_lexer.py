import ply.lex as lex
import sys

# Tokens list
tokens = (
    # PHP Header
    'HEADER',
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
    'DOT',
    'DOLAR'
    # Others
    'ID',
    'NUMBER'
)

# REGULAR EXPRESSIONS RULES FOR SIMPLE TOKENS
# For PHP Header
t_HEADER = r'<?php'

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
t_DOT = r'\.'
t_DOLAR = r'$'

# To ignore line breaks
t_ignore = ' \t'
