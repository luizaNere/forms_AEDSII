# Algoritmos de Busca

## Questão 1 — Busca binária

### Enunciado

Implemente a função `busca_binaria(lista, chave)`, que realiza a busca de um elemento em uma lista Python previamente ordenada de forma crescente.

A função deve localizar a chave e retornar o seu índice. Caso a chave não esteja presente, o retorno deve ser `-1`.

**Restrição:** É proibido o uso de funções ou métodos prontos de busca ou posicionamento, como `lista.index()`, `lista.count()` ou o módulo nativo `bisect`. A lógica do algoritmo de divisão e conquista deve ser implementada manualmente.

### Resolução

```python
def busca_binaria(lista, chave):
    e = 0
    d = len(lista) - 1

    while e <= d:
        meio = (e + d) // 2

        if lista[meio] == chave:
            return meio
        elif lista[meio] > chave:
            d = meio - 1
        else:
            e = meio + 1

    return -1
```

## Questão 2 — Passo a passo da busca binária

### Enunciado

Considere a seguinte lista de inteiros ordenada em Python:

```python
lista = [1, 3, 5, 7, 9, 11, 13, 15]
```

Para cada caso abaixo, descreva o passo a passo da busca binária, indicando a sequência de índices acessados até que o algoritmo chegue ao resultado final.

**Regra de cálculo:** Para determinar o índice do meio, utilize a divisão inteira:

```python
meio = (inicio + fim) // 2
```

**a)** Busca pela chave `13`. Liste a sequência de índices testados até encontrar o valor.

**b)** Busca pela chave `6`. Liste a sequência de índices testados até que o algoritmo determine que o valor não está presente na lista (retorno `-1`).

### Resolução

#### a) Busca pela chave 13

```text
inicio = 0
fim = 7
meio = 3
lista[meio] = 7
7 < 13
inicio = meio + 1 = 4

inicio = 4, fim = 7
meio = 5
lista[meio] = 11
11 < 13
inicio = meio + 1 = 6

inicio = 6, fim = 7
meio = 6
lista[meio] = 13
13 = 13, encontrou
retorna 6
```

Sequência de índices testados: `3 → 5 → 6`.

A chave `13` foi encontrada no índice `6`.

#### b) Busca pela chave 6

```text
inicio = 0
fim = 7
meio = 3
lista[meio] = 7
7 > 6
fim = meio - 1 = 2

inicio = 0, fim = 2
meio = 1
lista[meio] = 3
3 < 6
inicio = meio + 1 = 2

inicio = 2, fim = 2
meio = 2
lista[meio] = 5
5 < 6
inicio = meio + 1 = 3

inicio = 3, fim = 2
3 > 2
retorna -1
```

Sequência de índices testados: `3 → 1 → 2`.

A chave `6` não foi encontrada na lista, portanto o algoritmo retorna `-1`.

## Questão 3 — Primeira ocorrência

### Enunciado

Adapte o algoritmo de busca binária para localizar a primeira ocorrência de uma chave em uma lista que permite elementos duplicados. Ao encontrar o valor alvo, o algoritmo não deve encerrar a execução imediatamente; em vez disso, deve continuar a busca no subintervalo à esquerda para garantir que o índice retornado seja o menor possível.

**Exemplo:** Em `lista = [2, 4, 4, 4, 5, 7]`, a busca pela chave `4` deve retornar o índice `1`.

### Resolução

```python
def busca_binaria(lista, chave):
    inicio = 0
    fim = len(lista) - 1
    resultado = -1

    while inicio <= fim:
        meio = (inicio + fim) // 2

        if lista[meio] == chave:
            resultado = meio
            fim = meio - 1
        elif lista[meio] > chave:
            fim = meio - 1
        else:
            inicio = meio + 1

    return resultado
```

## Questão 4 — Limite inferior (Lower Bound)

### Enunciado

Implemente uma função em Python para encontrar o limite inferior (*Lower Bound*) de uma chave em uma lista ordenada. A função deve retornar o índice do menor elemento que seja maior ou igual à chave.

**Entrada:** Uma lista de inteiros ordenada e um valor `chave`.

**Saída:** O índice do elemento que satisfaz a condição. Se todos os elementos da lista forem menores que a chave, a função deve retornar `-1`.

**Exemplo:** Para `lista = [10, 20, 30, 40, 50]` e `chave = 35`, o retorno deve ser `3` (índice do valor `40`).

### Resolução

```python
def lower_bound(lista, chave):
    inicio = 0
    fim = len(lista) - 1
    indice = -1

    while inicio <= fim:
        meio = (inicio + fim) // 2

        if lista[meio] >= chave:
            indice = meio
            fim = meio - 1
        else:
            inicio = meio + 1

    return indice
```

## Questão 5 — Busca de caractere

### Enunciado

Implemente uma função em Python que utilize busca binária para verificar a existência de um caractere em uma string ordenada alfabeticamente.

**Entrada:** Uma string `s` e um caractere `chave`.

**Retorno:** O índice da primeira ocorrência da chave ou `-1` caso não seja encontrada.

**Restrição:** Não utilize o operador `in` ou o método `find()`; a lógica de divisão e conquista deve ser implementada manualmente.

### Resolução

```python
def busca_caractere(s, chave):
    inicio = 0
    fim = len(s) - 1
    resultado = -1

    while inicio <= fim:
        meio = (inicio + fim) // 2

        if s[meio] == chave:
            resultado = meio
            fim = meio - 1
        elif s[meio] < chave:
            inicio = meio + 1
        else:
            fim = meio - 1

    return resultado
```

## Questão 6 — Primeiro horário disponível

### Enunciado

Em um sistema de agendamento médico, os horários disponíveis são armazenados em uma lista de strings ordenada:

```python
horarios = ['08:00', '09:30', '14:00', '15:30', '16:00']
```

Implemente uma função que utilize busca binária para localizar o primeiro horário disponível que seja maior ou igual ao horário solicitado pelo paciente (`chave`).

**Exemplo:** Se o paciente solicita `'15:00'`, a função deve retornar o índice `3` (correspondente a `'15:30'`).

**Caso de exceção:** Se o horário solicitado for posterior ao último horário disponível, a função deve retornar `-1`.

**Restrição:** Utilize a comparação direta de strings do Python e mantenha a eficiência `O(log n)`.

### Resolução

```python
def primeiro_horario_disponivel(horarios, chave):
    inicio = 0
    fim = len(horarios) - 1
    resultado = -1

    while inicio <= fim:
        meio = (inicio + fim) // 2

        if horarios[meio] >= chave:
            resultado = meio
            fim = meio - 1
        else:
            inicio = meio + 1

    return resultado
```

## Questão 7 — Localizar ou inserir ID

### Enunciado

Implemente a função `localizar_ou_inserir(lista_ids, novo_id)`, que utiliza busca binária para gerenciar o cadastro de alunos.

**Cenário A:** Se o `novo_id` já estiver presente na lista, a função deve retornar o seu índice atual.

**Cenário B:** Se o `novo_id` não for encontrado, a função deve retornar o índice da posição ideal de inserção, ou seja, o ponto onde o ID deve ser inserido para que a lista permaneça ordenada.

**Exemplo:** Em `[10, 20, 30]`, buscar por `20` retorna `1`. Buscar por `25` também retorna `2` (posição onde o `25` entraria).

### Resolução

```python
def localizar_ou_inserir(lista_ids, novo_id):
    inicio = 0
    fim = len(lista_ids) - 1

    while inicio <= fim:
        meio = (inicio + fim) // 2

        if lista_ids[meio] == novo_id:
            return meio
        elif lista_ids[meio] < novo_id:
            inicio = meio + 1
        else:
            fim = meio - 1

    return inicio
```

## Questão 8 — Adivinhação numérica

### Enunciado

Implemente um simulador do jogo “Adivinhação Numérica” usando busca binária. O computador deve possuir um número secreto (por exemplo, `750`) dentro de um intervalo de `1` a `1000`.

**Requisitos:**

- O algoritmo deve tentar adivinhar o número ajustando os limites `inicio` e `fim` a cada tentativa.
- A cada palpite (meio do intervalo), o programa deve informar se o número secreto é maior ou menor que o palpite atual.
- Ao encontrar o número, o programa deve exibir o valor descoberto e o total de tentativas realizadas.

**Desafio:** Garanta que o número máximo de tentativas nunca ultrapasse `log₂(1000)` (aproximadamente 10 tentativas).

### Resolução

```python
def adivinhar(secreto, minimo=1, maximo=1000):
    inicio = minimo
    fim = maximo
    tentativas = 0

    while inicio <= fim:
        meio = (inicio + fim) // 2
        tentativas += 1
        print(f"Tentativa {tentativas}: palpite = {meio}")

        if meio == secreto:
            print(f"Número descoberto: {meio}")
            print(f"Total de tentativas: {tentativas}")
            return meio, tentativas
        elif secreto > meio:
            print("  O número secreto é maior")
            inicio = meio + 1
        else:
            print("  O número secreto é menor")
            fim = meio - 1

    return None, tentativas


adivinhar(750)
```

## Questão 9 — Frequência de uma chave

### Enunciado

Implemente uma função em Python para calcular a frequência de uma chave em uma lista ordenada, utilizando exclusivamente busca binária.

**Requisitos:**

- Não utilize o método `lista.count()`.
- Realize duas buscas binárias distintas: uma para localizar o índice da primeira ocorrência e outra para o índice da última ocorrência da chave.
- Calcule o total de repetições através da fórmula: `total = índice_último - índice_primeiro + 1`.
- Se a chave não estiver presente em nenhuma das buscas, o retorno deve ser `0`.

### Resolução

```python
def primeira_ocorrencia(lista, chave):
    inicio = 0
    fim = len(lista) - 1
    resultado = -1

    while inicio <= fim:
        meio = (inicio + fim) // 2

        if lista[meio] == chave:
            resultado = meio
            fim = meio - 1
        elif lista[meio] < chave:
            inicio = meio + 1
        else:
            fim = meio - 1

    return resultado


def ultima_ocorrencia(lista, chave):
    inicio = 0
    fim = len(lista) - 1
    resultado = -1

    while inicio <= fim:
        meio = (inicio + fim) // 2

        if lista[meio] == chave:
            resultado = meio
            inicio = meio + 1
        elif lista[meio] < chave:
            inicio = meio + 1
        else:
            fim = meio - 1

    return resultado


def frequencia(lista, chave):
    primeiro = primeira_ocorrencia(lista, chave)

    if primeiro == -1:
        return 0

    ultimo = ultima_ocorrencia(lista, chave)
    return ultimo - primeiro + 1
```
