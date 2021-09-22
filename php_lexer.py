import ply.lex as lex
import sys

# Tokens list
tokens = (
    # Reserverd words
    'BREAK',
    'ENDSWITCH',
    'FUNCTION',
    'INCLUDE',
    'OR',
    'REQUIRE',
    'THROW',
    'VAR',
    'CONST',
    'DO',
    'ENDWHILE',
    'FINALLY',
    'GLOBAL',
    'PRINT',
    'WHILE',
    'AND',
    'CASE',
    'CONTINUE',
    'ECHO',
    'ENDFOR',
    'RETURN',
    'TRY',
    'XOR',
    'CATCH',
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

    # Symbols
    'PLUS',
    'PLUSPLUS',
    # 'PLUSEQUAL',
    'MINUS',
    'MINUSMINUS',
    # 'MINUSEQUAL',
    'TIMES',
    'DIVIDE',
    'LESS',
    'LESSEQUAL',
    'GREATER',
    'GREATEREQUAL',
    'EQUAL',
    'DEQUAL',
    'DISTINT',
    'ISEQUAL',
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
    'HEADER'

    # Others
    'ID',
    'NUMBER'
)

# Regular expressions rules for a simple tokens
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_EQUAL = r'='
t_DISTINT = r'!'
t_LESS = r'<'
t_GREATER = r'>'
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
t_HEADER = r'<?php'
