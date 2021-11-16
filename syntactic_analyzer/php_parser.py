import ply.yacc as yacc
from lexical_analyzer import php_lexer
import sys

VERBOSE = 1


def p_program(p):
    """program : declaration_list"""
    pass


def p_declaration_list_1(p):
    """declaration_list : declaration_list  declaration"""
    pass


def p_declaration_list_2(p):
    """declaration_list : declaration"""
    pass


def p_declaration(p):
    """declaration : var_declaration | fun_declaration | header_declaration"""
    pass


def p_header_declaration_1(p):
    """header_declaration : INCLUDE ID DOT php"""
    pass


def p_var_declaration_1(p):
    """var_declaration : dolar var_declaration2 SEMICOLON"""
    pass


def p_var_declaration_2(p):
    """var_declaration2 : ID COMMA var_declaration2
    | dolar ID
    | dolar ID EQUAL NUMBER COMMA var_declaration2
    | dolar ID EQUAL NUMBER
    | TIMES dolar ID COMMA var_declaration2
    | TIMES dolar ID
    | dolar ID EQUAL dolar ID COMMA var_declaration2
    | dolar ID EQUAL dolar ID
    | COMMA
    | TIMES TIMES dolar ID
    | TIMES TIMES dolar ID COMMA var_declaration2
    """
    pass


def dolar(p):
    """dolar : $"""
    pass
