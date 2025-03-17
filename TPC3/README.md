# Conversor de Markdown para HTML

## 2025-03-09

## Autor:

- A98352
- Enzo Gabriel Barros Vieira

## Enunciado

Neste trabalho, o objetivo é desenvolver um conversor de Markdown para HTML utilizando expressões regulares do Python. O programa deverá:

Processar o conteúdo identificando e convertendo os seguintes elementos:

- **Headers:** Linhas que começam com de 1 a 6 `#` devem ser convertidas para `<h1>` até `<h6>`;
- **Negrito:** Textos delimitados por `**` devem ser convertidos para `<b>...</b>`;
- **Itálico:** Textos delimitados por `*` devem ser convertidos para `<i>...</i>`;
- **Listas ordenadas:** Blocos de itens numerados (ex.: `1. Item`) devem ser transformados em listas HTML, utilizando `<ol>` e `<li>`;
- **Links:** Sintaxe `[texto](URL)` deve ser convertida para `<a href="URL">texto</a>`;
- **Imagens:** Sintaxe `![alt](URL)` deve ser convertida para `<img src="URL" alt="alt"/>`.

## Resumo

O conversor foi implementado no ficheiro `main.py` e realiza a transformação do Markdown para HTML através de sucessivas substituições utilizando expressões regulares. O programa primeiro lê o ficheiro completo para poder capturar elementos que se estendem por várias linhas (como listas ordenadas) e, em seguida, aplica transformações específicas para cada elemento do Markdown.

Entre as técnicas empregadas, destacam-se:

- Uso de **named groups** e funções lambda para extrair e manipular os elementos, por exemplo, determinando dinamicamente o nível do header com base no número de `#` encontrados;
- Agrupamento de linhas para identificar blocos consecutivos de itens de listas, permitindo a conversão para `<ol>` e `<li>`;
- Substituições cuidadosas que respeitam a ordem dos elementos, de modo a evitar que uma transformação interfira na interpretação de outra.

## Exemplo de Execução

### Entrada

O ficheiro `example.txt` contém o seguinte Markdown:

```markdown
# Exemplo

## Outro Exemplo

### Exemplo ainda menor

Este é um **exemplo**

Este é um _exemplo_

1. Primeiro Item
2. Segundo Item
3. Terceiro Item

# Outra lista

1. Outro Primeiro Item
2. Outro Segundo Item
3. Outro Terceiro Item

Como pode ser consultado em [página da UC](http://www.uc.pt)

Como se vê na imagem seguinte: ![imagem dum coelho](http://www.coelho.com)
```

### Execução

```bash
python3 main.py > result.html
```

### Saída

O ficheiro `result.html` gerado contém a conversão completa:

```html
<h1>Exemplo</h1>

<h2>Outro Exemplo</h2>

<h3>Exemplo ainda menor</h3>

<p>Este é um <b>exemplo</b></p>

<p>Este é um <i>exemplo</i></p>

<ol>
  <li>Primeiro Item</li>
  <li>Segundo Item</li>
  <li>Terceiro Item</li>
</ol>
<h1>Outra lista</h1>
<ol>
  <li>Outro Primeiro Item</li>
  <li>Outro Segundo Item</li>
  <li>Outro Terceiro Item</li>
</ol>

<p>Como pode ser consultado em <a href="http://www.uc.pt">página da UC</a></p>

<p>
  Como se vê na imagem seguinte:
  <img src="http://www.coelho.com" alt="imagem dum coelho" />
</p>
```

## Conclusão

Este trabalho demonstra a aplicação de expressões regulares para converter Markdown em HTML, evidenciando a capacidade dessa abordagem para processar textos com estruturas pré-definidas. Embora o uso exclusivo de regex possa apresentar desafios para casos mais complexos do Markdown, o conversor desenvolvido cumpre os requisitos propostos, processando headers, ênfases, listas, links e imagens.
