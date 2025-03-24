import json
from datetime import date

class Stock:
  def __init__(self):
    self.balance = 0

    try:
      with open("stock.json") as stock_json:
        self.stock = json.load(stock_json)

        today = date.today().isoformat()
        self.log(f"{today}, Stock carregado, Estado atualizado.")
        self.log("Bom dia. Estou disponível para atender o seu pedido")
    except FileNotFoundError:
      print("Ficheiro não encontrado.")
  
  def save_stock(self):
    try:
      with open("stock.json", "w") as stock_json:
        json.dump(self.stock, stock_json, indent=2)
    except FileNotFoundError:
      print("Ficheiro não encontrado.")

  def log(self, m):
    print("maq:", m)

  def show_stock(self):
    print("maq:")
    print(f"{'cod':<5} | {'nome':<15} | {'quantidade':<12} | {'preço':<7}")

    for item in self.stock:
      print(f"{item['cod']:<5}   {item['nome']:<15}   {item['quant']:<12}   {item['preco']:<7}")
  
  def show_balance(self):
    self.log(f"Saldo = {self.balance}")

  def remove_item(self, item, quant=1):
    if item['quant'] >= quant:
      item['quant'] -= quant

  def add_balance(self, value):
    self.balance += value
    self.log(f"Saldo: {self.balance}")
  
  def buy_item(self, cod):
    item_found = self.get_item(cod)

    if item_found is None:
      self.log(f"Item não encontrado: {cod}")
      return

    if item_found['quant'] <= 0:
      self.log(f"Item não tem quantidade suficiente; {item_found['nome']} em estoque = {item_found['quant']}")
      return

    has_balance = item_found['preco'] <= self.balance

    if not has_balance:
      self.log("Saldo insuficiente para satisfazer o seu pedido")
      self.log(f"Saldo = {self.balance}; Pedido = {item_found['preco']}")
      return
    
    self.log(f"Pode retirar o produto dispensado '{item_found['nome']}'")

    self.balance -= item_found['preco']
    self.remove_item(item_found)
  
  def get_item(self, cod):
    for item in self.stock:
      if item['cod'] == cod:
        return item

    return None

  def calc_change(self):
    balance_in_cents = round(self.balance * 100)

    coins = [200, 100, 50, 20, 10, 5, 2, 1]
    change = {}
    
    for coin in coins:
      if balance_in_cents >= coin:
        quant = balance_in_cents // coin
        change[coin] = quant
        balance_in_cents %= coin

    change_str = []
    for coin in sorted(change, reverse=True):
      coin_str = f"{round(coin/100)}e" if coin >= 100 else f"{coin}c"
      change_str.append(f"{change[coin]} x {coin_str}")

    self.log(f"Pode retirar o troco: {', '.join(change_str)}")
