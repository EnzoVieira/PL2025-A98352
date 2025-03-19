import ply.lex as lex

reserved = {
  'select' : 'SELECT',
  'where' : "WHERE",
  'limit' : "LIMIT"
}

tokens = [
  'NUMBER',     # 1000
  'ID',         # Ex.: ?nome
  'STRING',     # "Chuck Berry"
  'LITERAL',    # 
  'PREFIX',     # foaf:
  'TAG',        # Ex.: @en
  'NAMESPACE',  # Ex.: (?<=:)MusicalArtist
  'TERMINATOR', # .
  'RBRACKET',   # }
  'LBRACKET'    # {
] + list(reserved.values())

def t_TERMINATOR(t):
  r'\.'
  return t

def t_PREFIX(t):
    r'[A-Za-z_][A-Za-z0-9_]*:'
    return t

def t_STRING(t):
  r'\".*\"'
  return t

def t_NAMESPACE(t):
  r'(?<=:)[a-zA-z]*'
  return t

def t_NUMBER(t):
  r'-?\d+'
  t.value = int(t.value)
  return t

def t_LITERAL(t):
  r'[a-zA-Z][a-zA-Z]*'
  t.type = reserved.get(t.value.lower(), 'LITERAL')
  return t

t_ID = r'\?[a-z]+'
t_TAG = r'\@[a-z]+'
t_RBRACKET = r'\}'
t_LBRACKET = r'\{'

t_ignore_COMMENT = r'\#.*'

t_ignore = ' \t\n'

def t_error(t):
  print(f"Carácter ilegal {t.value[0]}")
  t.lexer.skip(1)

lexer = lex.lex()

def main():
  with open("example.txt", "r") as query_file:
    query = query_file.read()

    lexer.input(query)
  
    while tok := lexer.token():
      print(tok)

if __name__ == "__main__":
  main()