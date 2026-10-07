# Complexidade de Algoritmos

## Questão 1 — Conceito e importância

### Enunciado

Explique com suas palavras o que é complexidade de algoritmos e por que é importante.

### Resposta

A complexidade de algoritmos diz respeito ao custo (memória, tempo, capital etc.) necessário para executar ou implementar um algoritmo. É importante para definir qual é a maneira mais eficiente de solucionar um problema e quais soluções são viáveis dado o contexto e a quantidade de recursos disponíveis.

## Questão 2 — Critérios de eficiência

### Enunciado

Quais são os dois principais critérios de eficiência de um algoritmo?

### Resposta

Tempo de execução e uso de memória.

## Questão 3 — Complexidade assintótica

### Enunciado

O que é a complexidade assintótica e por que ela é usada?

### Resposta

A complexidade assintótica analisa o algoritmo quando o valor de `n` tende ao infinito, ignorando as constantes e os termos de menor ordem. Ela é utilizada para prever o desempenho e a complexidade de um algoritmo para entradas de diferentes tamanhos.

## Questão 4 — Termo dominante

### Enunciado

Por que, em uma função de complexidade $f(n) = n^2 + 100n + \log_{10}n + 1.000$, o termo dominante ($n^2$) se torna mais significativo para grandes valores de `n`?

### Resposta

Porque o termo de maior ordem domina o comportamento da função. Com o aumento de `n`, o termo cujo valor cresce mais rapidamente, nesse caso `n²`, passa a ter a maior influência no resultado.

## Questão 5 — Complexidade da busca binária

### Enunciado

Qual é a complexidade do algoritmo de busca binária?

### Resposta

- Melhor caso (chave exatamente no meio da lista): `O(1)`.
- Caso médio: `O(log n)`.
- Pior caso (chave não está na lista ou só é encontrada após sucessivas divisões): `O(log n)`.

## Questão 6 — Melhor, pior e caso médio

### Enunciado

Explique a diferença entre o melhor, o pior e o caso médio de um algoritmo. Qual é a principal complicação ao determinar o caso médio?

### Resposta

O melhor caso corresponde à menor quantidade de operações que o algoritmo realiza para uma entrada de determinado tamanho. O pior caso corresponde à maior quantidade de operações. O caso médio representa o custo esperado considerando as entradas possíveis e a probabilidade de cada uma delas.

A principal complicação é determinar uma distribuição de probabilidades que represente adequadamente as entradas reais; sem essa informação, a média pode não refletir o uso típico do algoritmo.

## Questão 7 — Notação Big-O

### Enunciado

Defina a notação Big-O (`O`) em suas próprias palavras. O que ela representa em termos de taxa de crescimento de funções?

### Resposta

A notação Big-O descreve como o tempo de execução ou o uso de memória cresce em relação ao tamanho da entrada (`n`). Para isso, considera-se o termo de maior ordem, que domina a função conforme `n` aumenta, ignorando constantes e termos de menor ordem.
