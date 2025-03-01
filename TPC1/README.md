# Somador on/off: criar programa em Python (sem usar expressões regulares)

## 2025-02-07

## Autor:

- A98352
- Enzo Gabriel Barros Vieira

## Enunciado:

1: Pretende-se um programa que some todas as sequências de dígitos que encontre num texto;

2: Sempre que encontrar a string "Off" em qualquer combinação de maiúsculas e minúsculas, esse comportamento é desligado;

3: Sempre que encontrar a string "On" em qualquer combinação de maiúsculas e minúsculas, esse comportamento é novamente ligado;

4: Sempre que encontrar o caráter "=", o resultado da soma é colocado na saída.

## Resumo:

O programa recebe uma linha do stdin na qual soma os números que encontra na linha, a soma é controlada por uma flag On e Off, e sempre que aparece um "=" o valor da soma atual é escrito no stdout.

## Exemplo:

exto de entrada a ser passado pelo stdin:

```sh
Hoje, 7 de Fevereiro de 2025, o professor de Processamento de Linguagens
deu-nos
este trabalho para fazer.=OfF
E deu-nos 7= dias para o fazer... ON
Cada trabalho destes vale 0.25 valores da nota final!
```

Texto enviado para stdout:

```sh
Hoje, 7 de Fevereiro de 2025, o professor de Processamento de Linguagens
deu-nos
este trabalho para fazer.=
>> 2032
OfF
E deu-nos 7=
>> 2032
 dias para o fazer... ON
Cada trabalho destes vale 0.25 valores da nota final!
>> 2057
```

## Testar

```sh
python3 main.py
```

ou usando o ficheiro de exemplo:

```sh
python3 main.py < example.txt
```
