# Analisador Léxico para Linguagem de Consulta

## 2025-03-16

## Autor:

- A98352
- Enzo Gabriel Barros Vieira

## Enunciado

Neste trabalho, o objetivo é desenvolver um analisador léxico (lexer) para uma linguagem de consulta inspirada em SPARQL, utilizando o módulo PLY do Python. O lexer deve identificar e classificar os diferentes componentes de uma consulta, tais como:

- **Palavras Reservadas:**

  - `select`
  - `where`
  - `limit`

- **Tokens Gerais:**
  - **NUMBER:** Números inteiros (por exemplo, `1000`).
  - **ID:** Variáveis identificadas por `?` (por exemplo, `?nome`, `?desc`).
  - **LITERAL:** Literais não delimitados por aspas (por exemplo, a palavra `a` ou outras constantes simples).
  - **STRING:** para capturar literais entre aspas, como `"Chuck Berry"`.
  - **PREFIX:** Sequência representando o prefixo de um nome qualificado (por exemplo, `dbo:` ou `foaf:`).
  - **NAMESPACE:** O identificador local que segue um prefixo (por exemplo, `MusicalArtist` em `dbo:MusicalArtist`).
  - **TAG:** Tag de idioma para literais, como `@en`.
  - **TERMINATOR:** O ponto final (`.`) que termina uma instrução ou tripla.
  - **LBRACKET / RBRACKET:** Delimitadores de blocos, representados por `{` e `}`.

## Resumo

O analisador foi implementado utilizando o PLY, que permite definir regras de tokenização por meio de expressões regulares.  
Foram criadas funções para tokens específicos – especialmente para capturar os prefixos e os nomes qualificados – garantindo que:

- Palavras reservadas sejam mapeadas para seus respectivos tokens (por exemplo, `select` para `SELECT`).
- Prefixos como `dbo:` sejam identificados pelo token **PREFIX**, e o nome que os segue seja capturado como **NAMESPACE**.
- Variáveis, literais simples, números e demais símbolos (como `{`, `}`, e `.`) sejam corretamente reconhecidos e classificados.

A estratégia adotada inclui a definição de regras de token específicas (por meio de funções) para garantir a ordem de precedência correta, evitando que regras mais gerais (como a dos literais) sejam confundidas com partes que deveriam ser reconhecidas como tokens especiais.

## Exemplo de Execução

### Entrada

O ficheiro `example.txt` contém a seguinte consulta:

```sparql
# DBPedia: obras de Chuck Berry
select ?nome ?desc where {
    ?s a dbo:MusicalArtist.
    ?s foaf:name "Chuck Berry"@en .
    ?w dbo:artist ?s.
    ?w foaf:name ?nome.
    ?w dbo:abstract ?desc
} LIMIT 1000
```

### Execução

```bash
python3 main.py
```

### Saída

```
LexToken(SELECT,'select',1,32)
LexToken(ID,'?nome',1,39)
LexToken(ID,'?desc',1,45)
LexToken(WHERE,'where',1,51)
LexToken(LBRACKET,'{',1,57)
LexToken(ID,'?s',1,63)
LexToken(LITERAL,'a',1,66)
LexToken(PREFIX,'dbo:',1,68)
LexToken(NAMESPACE,'MusicalArtist',1,72)
LexToken(TERMINATOR,'.',1,85)
LexToken(ID,'?s',1,91)
LexToken(PREFIX,'foaf:',1,94)
LexToken(NAMESPACE,'name',1,99)
LexToken(STRING,'"Chuck Berry"',1,104)
LexToken(TAG,'@en',1,117)
LexToken(TERMINATOR,'.',1,121)
LexToken(ID,'?w',1,127)
LexToken(PREFIX,'dbo:',1,130)
LexToken(NAMESPACE,'artist',1,134)
LexToken(ID,'?s',1,141)
LexToken(TERMINATOR,'.',1,143)
LexToken(ID,'?w',1,149)
LexToken(PREFIX,'foaf:',1,152)
LexToken(NAMESPACE,'name',1,157)
LexToken(ID,'?nome',1,162)
LexToken(TERMINATOR,'.',1,167)
LexToken(ID,'?w',1,173)
LexToken(PREFIX,'dbo:',1,176)
LexToken(NAMESPACE,'abstract',1,180)
LexToken(ID,'?desc',1,189)
LexToken(RBRACKET,'}',1,195)
LexToken(LIMIT,'LIMIT',1,197)
LexToken(NUMBER,1000,1,203)
```

## Conclusão

Este projeto demonstra a implementação de um analisador léxico para uma linguagem de consulta, utilizando o módulo PLY do Python.
Através da definição cuidadosa de tokens e da ordenação das regras de tokenização, o lexer é capaz de identificar de forma precisa e robusta os diferentes componentes de uma consulta, como palavras reservadas, variáveis, literais, nomes qualificados e delimitadores.
