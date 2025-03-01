# Análise de um dataset de obras musicais

## 2025-02-14

## Autor:

- A98352
- Enzo Gabriel Barros Vieira

## Enunciado

Neste TPC é proibido utilizar o módulo CSV do Python. O programa deverá:

1. Ler um dataset de obras musicais;
2. Processar os dados e gerar os seguintes resultados:
   2.1. Lista ordenada alfabeticamente dos compositores musicais;

   2.2. Distribuição das obras por período (quantas obras há em cada período);

   2.3. Um dicionário em que cada período está associado a uma lista alfabética dos títulos das obras correspondentes.

## Resumo

O programa lê um ficheiro CSV (com campos separador por ponto e vírgula ";") que contém os seguinte campos para cada registro:

- Título da obra (grupo 1);
- Descrição (entre aspas ou não – grupo 2);
- Ano de criação (4 dígitos – grupo 3);
- Período (grupo 4);
- Compositor (grupo 5);
- Duração (no formato hh:mm:ss – grupo 6);
- Identificador (no formato “O” seguido de dígitos – grupo 7).

Como alguns campos (por exemplo, a descrição) podem conter quebras de linha, o programa acumula as linhas do arquivo até que um registro completo seja formado. A extração dos campos é feita utilizando expressões regulares (com a flag re.DOTALL para que o token “.” corresponda também com quebra de linhas "\n").

## Exemplo de Execução:

### Entrada via STDIN ou ficheiro:

Suponha que o dataset esteja no ficheiro `obras.csv`.

```sh
python3 main.py obras.csv
```

ou

```sh
python3 main.py obras.csv > result.txt
```
