import ply.yacc as yacc

from lexer import tokens

# 2+3
# 67-(2+3*4)
# (9-2)*(13-4)
def p_expression_sum(p):
  "exp : exp PLUS fac"
  p[0] = p[1] + p[3]

def p_expression_minus(p):
  "exp : exp MINUS fac"
  p[0] = p[1] - p[3]

def p_expression(p):
  "exp : fac"
  p[0] = p[1]

def p_factor_mul(p):
  "fac : fac MUL term"
  p[0] = p[1] * p[3]

def p_factor_div(p):
  "fac : fac DIV term"
  p[0] = p[1] / p[3]

def p_factor(p):
  "fac : term"
  p[0] = p[1]

def p_term_paren(p):
  "term : LP exp RP"
  p[0] = p[2]

def p_term_num(p):
  "term : NUMBER"
  p[0] = p[1]

def p_error(p):
  print(f"Erro sintático no input {p}")

parser = yacc.yacc()

def main():
  # user_input = input(">> ")
  user_input = "((9+(3))-(2+2))*(13-4)"
  r = parser.parse(user_input)
  print(f"Resultado {r}")

if __name__ == "__main__":
  main()
