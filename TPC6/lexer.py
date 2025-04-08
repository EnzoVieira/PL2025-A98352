import ply.lex as lex

tokens = [
  'NUMBER',
  'PLUS',
  'MINUS',
  'MUL',
  'DIV',
  'LP',
  'RP'
]

def t_NUMBER(t):
  r'\d+'
  t.value = int(t.value)
  return t

t_PLUS = r'\+'
t_MINUS = r'-'
t_MUL = r'\*'
t_DIV = r'/'
t_LP = r'\('
t_RP = r'\)'

t_ignore = ' \t\n'

def t_error(t):
  print(f"Carácter ilegal {t.value[0]}")
  t.lexer.skip(1)

lexer = lex.lex()

# def main():
#   lexer.input("2  + 3")

#   while tok := lexer.token():
#     print(tok)

# if __name__ == "__main__":
#   main()
