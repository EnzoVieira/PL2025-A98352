# Máquina de Vending

## 2025-03-08

## Autor:

- A98352
- Enzo Gabriel Barros Vieira

## Enunciado

Desenvolver um programa que simule uma máquina de vending.
O sistema deve:

1. Carregar um estoque de produtos a partir de um ficheiro JSON ("stock.json"), onde cada produto é representado por um dicionário contendo:

   - **cod:** Código do produto (ex.: "A23")
   - **nome:** Nome do produto (ex.: "agua 0.5L")
   - **quant:** Quantidade em estoque
   - **preco:** Preço do produto (em euros; ex.: 0.7)

2. Aceitar comandos em lowercase do utilizador via terminal para:
   - **listar:** Exibir o estoque atual, formatado com colunas (código, nome, quantidade e preço).
   - **saldo:** Exibir o saldo disponível do utilizador.
   - **moeda:** Permitir ao utilizador depositar moedas, informando valores como "1e" para euros e "20c" para cêntimos. O saldo é atualizado e exibido (por exemplo, "Saldo = 1e30c").
   - **selecionar:** Efetuar a compra de um produto especificado por seu código. Se o saldo for suficiente ou tiver produtos em estoque, o produto é dispensado e o estoque atualizado; caso contrário, o sistema informa que o saldo é insuficiente ou que não há produtos em estoque.
   - **sair:** Encerrar a sessão, calculando e exibindo o troco (em moedas) a ser devolvido, e salvando o estoque atualizado no ficheiro JSON.

O programa deve contemplar cenários como produto inexistente, estoque insuficiente ou saldo insuficiente, e pode ser estendido para permitir a adição de novos produtos ao estoque.

## Resumo

O sistema foi implementado utilizando Python e o módulo PLY para a criação de um lexer que interpreta os comandos digitados pelo utilizador. Os principais pontos da implementação são:

- **Leitura e Persistência do Estoque:**  
  O estoque é carregado a partir de "stock.json" na inicialização e, ao término da execução, o estoque é gravado de volta no mesmo ficheiro, mantendo o estado entre as interações.

- **Analisador Léxico com PLY:**  
  Foram definidos tokens para identificar comandos (como LISTAR, MOEDA, SELECIONAR, SAIR, SALDO), moedas (EURO e CENTS), identificadores de produtos e outros símbolos (como o terminador de instrução "."). Essa abordagem garante a correta interpretação da entrada do usuário.

- **Gerenciamento do Saldo e Troco:**  
  O saldo do utilizador é armazenado como um float (representando o valor em euros). Ao encerrar a sessão, uma função calcula o troco a ser devolvido.

- **Processamento de Comandos:**  
  Dependendo do comando recebido:
  - **LISTAR:** Exibe o estoque..
  - **MOEDA:** Atualiza o saldo com os valores depositados.
  - **SELECIONAR:** Verifica se o produto existe, se há saldo suficiente e, em caso afirmativo, despacha o produto e atualiza o saldo.
  - **SAIR:** Calcula e exibe o troco a ser devolvido, encerrando a interação.

## Exemplo de Execução

```bash
maq: 2024-03-08, Stock carregado, Estado atualizado.
maq: Bom dia. Estou disponível para atender o seu pedido.
>> listar
maq:
cod | nome           | quantidade | preço
A23   água 0.5L        7            0.7
B2    Coca-Cola 0.2L   1            1.0
>> moeda 1e, 20c, 5c, 5c .
maq: Saldo = 1e30c
>> selecionar A23
maq: Pode retirar o produto dispensado "água 0.5L"
maq: Saldo = 60c
>> sair
maq: Pode retirar o troco: 1x 50c, 1x 10c.
maq: Até à próxima
```

## Conclusão

Este projeto demonstra a implementação de uma máquina de vending simulada, abordando a leitura e persistência de estoque via JSON, a interpretação de comandos do utilizador com um analisador léxico (PLY) e a manipulação de saldo com cálculo de troco.  
A solução contempla cenários diversos (produto inexistente, estoque insuficiente, saldo insuficiente) e pode ser expandida para incluir novas funcionalidades.
