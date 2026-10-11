# Listas em Python

## Questão 1 — Cópia invertida com fatiamento

### Enunciado

Como a sintaxe de fatiamento pode ser utilizada para criar uma cópia invertida de uma lista e qual é a natureza do objeto resultante em termos de alocação de memória?

### Resposta

```python
original = [2, 3, 5, 7]
invertida = original[::-1]  # cria uma cópia rasa da lista original
```

Cria uma nova lista em uma região de memória diferente da original. Assim, modificar a estrutura da cópia não altera a lista original. Entretanto, a cópia é rasa, ou seja, se a lista contiver objetos mutáveis, eles continuarão sendo compartilhados entre as duas listas.

## Questão 2 — Atribuição por índice e por fatia

### Enunciado

Diferencie o comportamento da atribuição por índice único (`L[i]=x`) do comportamento da atribuição por fatia vazia (`L[i:i]=[x]`) em termos de como a estrutura da lista é afetada.

### Resposta

A atribuição por índice único modifica o valor localizado na posição `i`, enquanto a atribuição por fatia vazia "cria um espaço" antes da posição `i` e insere o valor.

## Questão 3 — `append()` e `extend()`

### Enunciado

Se você possui uma lista `L1 = [10, 20]` e deseja adicionar os elementos da lista `L2 = [30, 40]` ao final de `L1`, explique a diferença estrutural no resultado final entre utilizar `L1.append(L2)` e `L1.extend(L2)`.

### Resposta

O resultado de `L1.append(L2)` é `L1 = [10, 20, [30, 40]]` e o resultado de `L1.extend(L2)` é `L1 = [10, 20, 30, 40]`.

## Questão 4 — Complexidade da inserção interna

### Enunciado

Por que a operação de inserção em uma posição interna (como o início ou meio) de uma lista grande possui uma complexidade de tempo de `O(n)`, enquanto a inserção no final é geralmente mais eficiente?

### Resposta

Porque é necessário deslocar todos os elementos à direita "para frente".

## Questão 5 — Desempenho de `extend()`

### Enunciado

Explique por que, em termos de desempenho, é preferível utilizar o método `extend()` em vez de realizar múltiplas chamadas consecutivas ao método `append()` para adicionar vários elementos ao final de uma lista.

### Resposta

O método `extend()` é preferível nesse caso porque permite inserir todos os elementos de um iterável em uma única chamada, reduzindo a sobrecarga de múltiplas chamadas do método `append()`.

## Questão 6 — `+=` e concatenação de listas

### Enunciado

Diferencie a operação de atribuição aumentada `L += [1, 2]` da atribuição simples `L = L + [1, 2]` no que diz respeito à identidade do objeto (`id`) e à alocação de memória para listas.

### Resposta

Em `L += [1, 2]`, o `id` é mantido, ou seja, é a mesma lista. Já em `L = L + [1, 2]`, uma nova lista, com um `id` diferente, é criada, ocupando outra posição de memória.

## Questão 7 — Remoção com `del`

### Enunciado

Explique como a instrução `del` atua ao remover um elemento de um índice específico em uma lista e descreva o impacto dessa operação na organização dos elementos subsequentes na memória.

### Resposta

A instrução `del` permite remover um elemento de uma lista por índice ou por fatia, utilizando a sintaxe `del lista[indice]`.

## Questão 8 — `del` e `pop()`

### Enunciado

Qual é a principal distinção funcional entre utilizar a instrução `del` e o método `pop(i)` para remover um item de uma lista em um índice específico?

### Resposta

A diferença mais importante entre os dois é que o método `pop(i)` retorna o elemento que foi removido da lista, enquanto a instrução `del` somente o remove da lista.

## Questão 9 — Complexidade da inserção e remoção

### Enunciado

Por que operações de inserção ou remoção no início de uma lista possuem complexidade temporal `O(n)`, enquanto no final da lista são geralmente `O(1)`?

### Resposta

Porque, quando o elemento está no início da lista, é necessário deslocar todos os elementos da lista para frente (inserção) ou para trás (remoção).

## Questão 10 — Método `clear()`

### Enunciado

Ao utilizar o método `clear()`, o que acontece com a identidade (representada pela função `id()`) do objeto lista e com a alocação de memória do interpretador?

### Resposta

A lista, mesmo que vazia, continua com o mesmo `id`, ou seja, na mesma posição de memória.

## Questão 11 — `sort()` e `sorted()`

### Enunciado

Explique a principal diferença funcional entre o método `L.sort()` e a função built-in `sorted(L)` em relação ao objeto original.

### Resposta

Enquanto o método `L.sort()` ordena a lista in-place, ou seja, não cria outro objeto, a função `sorted(L)` cria uma nova lista, com os mesmos elementos da anterior, e a ordena.

## Questão 12 — Parâmetros de `sort()`

### Enunciado

Quais parâmetros o método `sort()` pode receber e para que eles servem?

### Resposta

- `key`: determina o critério de ordenação dos elementos. Por exemplo, pode ordenar palavras pelo tamanho.
- `reverse`: define a direção da ordenação. Quando recebe `True`, ordena em ordem decrescente; quando recebe `False`, ordena em ordem crescente.

## Questão 13 — Operador `in` e método `index()`

### Enunciado

Explique a diferença fundamental entre o uso do operador `in` e o método `index()` ao procurar um elemento em uma lista Python.

### Resposta

Quando o elemento não está na lista, o operador `in` retorna `false` e o método `index()` retorna `ValueError`. Além disso, o operador `in` não retorna o índice do elemento.

## Questão 14 — Operadores `==` e `is`

### Enunciado

Explique a diferença fundamental entre os operadores `==` e `is` ao comparar duas listas em Python.

### Resposta

`==` compara os valores e a ordem dos elementos, enquanto `is` verifica a identidade, isto é, se as variáveis apontam para o mesmo `id`.

## Questão 15 — Requisitos da função `sum()`

### Enunciado

Se um programador tentar executar a função `sum(L)` em uma lista `L = [10, 20.5, "30"]`, o que acontecerá? Explique o requisito fundamental para o funcionamento dessa função.

### Resposta

O requisito fundamental para o funcionamento dessa função é que todos os elementos da lista sejam compatíveis com a operação de adição (como `int` e `float`). Logo, ao tentar somar uma string, a função retornará um `TypeError`.

## Questão 16 — Acesso a elementos de uma matriz

### Enunciado

Dada uma estrutura de dados bidimensional representada por uma lista de listas chamada `matriz`, descreva o processo lógico e a sintaxe necessária para acessar um elemento específico, explicando o que cada colchete representa na expressão `matriz[i][j]`.

### Resposta

O primeiro par de colchetes, que contém o índice `i`, se refere às linhas da matriz. Nesse caso, cada valor representa uma das sublistas contidas em `matriz`. O segundo par de colchetes, com o índice `j`, faz referência aos elementos dentro das sublistas (colunas da matriz).

## Questão 17 — Atribuição e referência ao mesmo objeto

### Enunciado

Explique por que a atribuição simples `L1=L` não é considerada uma operação de cópia independente e descreva o impacto de modificar um elemento através de `L1`.

### Resposta

A atribuição `L1 = L` não cria uma cópia independente da lista. Ela faz com que as variáveis `L1` e `L` apontem para o mesmo objeto na memória. Ao modificar um elemento por meio de `L1`, o valor também é alterado quando a lista é acessada por `L`, pois ambas as variáveis referenciam a mesma lista.

## Questão 18 — Cópias rasas de listas

### Enunciado

Compare os resultados de criar uma cópia de uma lista `L` usando `list(L)`, `L[:]` e `L.copy()`. Existe algum cenário onde um desses métodos produziria uma cópia mais profunda que os outros?

### Resposta

Os três métodos produzem cópias rasas da lista original, ou seja, criam uma nova lista, mas fazem referências aos mesmos objetos internos. Nenhum desses três métodos produz uma cópia mais profunda que os outros: todos realizam uma cópia superficial.
