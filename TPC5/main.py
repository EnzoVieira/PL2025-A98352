import ply.lex as lex

from stock import Stock

literals = [ ',', '.' ]

reserved = {
  'sair' : 'SAIR',
  'listar' : 'LISTAR',
  'moeda' : 'MOEDA',
  'selecionar' : 'SELECIONAR',
  'saldo': 'SALDO'
}

tokens = [
  'EURO',
  'CENTS',
  'ID',
  'PROD'
] + list(reserved.values())

def t_PROD(t):
  r'[A-Z]\d+'
  return t

def t_EURO(t):
  r'\d+(?=e)'
  t.value = int(t.value)
  t.lexer.skip(1)
  return t

def t_CENTS(t):
  r'\d+(?=c)'
  t.value = int(t.value)/100
  t.lexer.skip(1)
  return t

def t_ID(t):
  r"[a-z]+"
  t.type = reserved.get(t.value, "ID")
  return t

t_ignore = " \t\n"

def t_error(t):
  print(f"Token inválido {t.value}")
  t.lexer.skip(len(t.value))

lexer = lex.lex()


def main():
  stock = Stock()

  user_input = input(">> ")
  lexer.input(user_input)

  while (tok := lexer.token()).type != 'SAIR':
    match tok.type:
      case 'LISTAR':
        stock.show_stock()
      case 'SALDO':
        stock.show_balance()
      case 'MOEDA':
        add = 0
        while (tok := lexer.token()).type != '.':
            if tok.type == 'EURO' or tok.type == 'CENTS':
              add += tok.value 
        stock.add_balance(add)
      case 'SELECIONAR':
        tok = lexer.token() # item cod
        stock.buy_item(tok.value)
      
      case default:
        print(f"Ação não implementada: {tok.type}")

    user_input = input(">> ")
    lexer.input(user_input)
  
  stock.save_stock()
  stock.calc_change()
  stock.log("Até à próxima")

if __name__ == "__main__":
  main()
