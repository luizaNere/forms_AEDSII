# Recursividade

## Questão 1 — Conversão de decimal para binário

### Enunciado

Escreva uma função recursiva que converta um número inteiro positivo da base decimal para a base binária.

A função deve receber um número inteiro e retornar uma string representando o número em binário. Utilize o método das divisões sucessivas por 2: a cada chamada recursiva, o resto da divisão por 2 corresponde a um dígito binário.

O programa principal deve ler um valor decimal da entrada e exibir o binário correspondente.

**Exemplo:** entrada `3`; saída `11`.

### Solução

```python
def decimal_para_binario(n):
    if n == 0:
        return ""
    elif n == 1:
        return "1"
    else:
        return decimal_para_binario(n // 2) + str(n % 2)
```

## Questão 2 — Raiz quadrada por aproximações

### Enunciado

Implemente uma função recursiva `raiz(N, A, E)` que calcula a raiz quadrada de `N`, onde:

- `N` é o número cuja raiz quadrada se deseja calcular;
- `A` é uma aproximação inicial para a raiz;
- `E` é o erro máximo admissível.

Se `|A² − N| < E`, a função retorna `A`. Caso contrário, chama-se recursivamente com a nova aproximação `(A² + N) / (2 * A)`. Exiba cada aproximação com seis casas decimais antes da próxima chamada.

**Exemplo:** `raiz(9, 4, 0.01)`.

### Solução

```python
def raiz(N, A, E):
    print(f"Aproximação {A:.6f}")

    if abs(A ** 2 - N) < E:
        print(f"Resultado final: {A:.6f}")
        return A
    else:
        return raiz(N, (A ** 2 + N) / (2 * A), E)
```

## Questão 3 — Máximo divisor comum

### Enunciado

Construa uma função recursiva `MDC` que determine o máximo divisor comum de dois inteiros `M` e `N` por meio do Algoritmo de Euclides:

- `MDC(N, M)`, se `N > M`;
- `M`, se `N = 0`;
- `MDC(N, M mod N)`, se `N > 0` e `N ≤ M`.

### Solução

```python
def mdc(m, n):
    if n == 0:
        return m
    elif n > m:
        return mdc(n, m)
    else:
        return mdc(n, m % n)
```

## Questão 4 — Função de Ackermann

### Enunciado

Escreva uma função recursiva para calcular a função de Ackermann `A(m, n)`, em que `m` e `n` são inteiros não negativos:

```text
A(m, n) = n + 1                    se m = 0
          A(m - 1, 1)              se m > 0 e n = 0
          A(m - 1, A(m, n - 1))    se m > 0 e n > 0
```

Testes:

- `A(0, 5)` deve retornar `6`;
- `A(1, 5)` deve retornar `7`;
- `A(2, 5)` deve retornar `13`.

### Solução

```python
def ackermann(m, n):
    if m == 0:
        return n + 1
    elif n == 0:
        return ackermann(m - 1, 1)
    else:
        return ackermann(m - 1, ackermann(m, n - 1))
```

## Questão 5 — Somatório dos elementos de um vetor

### Enunciado

O somatório dos elementos de um vetor pode ser calculado recursivamente. Faça um programa que:

a) leia um vetor de 10 elementos reais;
b) imprima o conteúdo desse vetor;
c) imprima o somatório dos elementos, calculado pela função recursiva.

Considere `L` como o índice do primeiro item do vetor `X` e `M` como o índice do último item.

Exemplo: `X = [2, 4, 6, 8]`, `L = 0`, `M = 3`.

### Solução

```python
def somatorio_recursivo(vetor, L, M):
    if L == M:
        return vetor[L]
    else:
        meio = (L + M) // 2
        return somatorio_recursivo(vetor, L, meio) + somatorio_recursivo(vetor, meio + 1, M)


vetor = []
for i in range(10):
    valor = float(input(f"Digite o {i+1}º elemento do vetor: "))
    vetor.append(valor)

print("Conteúdo do vetor:", vetor)

L = 0
M = len(vetor) - 1
resultado = somatorio_recursivo(vetor, L, M)
print("Resultado do somatório: ", resultado)
```

## Questão 6 — Potência

### Enunciado

Escreva uma função recursiva para calcular o valor de `xⁿ`, usando multiplicações. Não use o operador `**`, `pow()`, `math.pow()` ou outra função matemática.

### Solução

```python
def potencia_recursiva(x, n):
    if n == 0:
        return 1
    else:
        return x * potencia_recursiva(x, n - 1)
```

## Questão 7 — Soma de uma série

### Enunciado

Considere a seguinte soma:

```text
S = 1/2 + 2/3 + 3/5 + 4/7 + ... + 20/39
```

Escreva uma função recursiva para calcular a soma. O resultado é o valor do primeiro termo somado à chamada recursiva para calcular a soma a partir do segundo termo.

### Solução

```python
def soma_recursiva(n):
    if n == 1:
        return 1 / 2
    else:
        return n / (2 * n - 1) + soma_recursiva(n - 1)
```

Para somar os 20 termos da série, chame `soma_recursiva(20)`.

## Questão 8 — Soma de série com limite para o último termo

### Enunciado

Elabore uma função recursiva que calcule o valor da série:

```text
S = 70/7 + 69/14 + 68/21 + 67/28 + ...
```

Utilize tantos termos quantos forem necessários até que o último termo seja menor que `0,01`. Indique a quantidade mínima de termos necessária e o valor da soma.

### Solução

```python
def serie(k=1):
    termo = (71 - k) / (7 * k)

    if termo < 0.01:
        return termo, 1

    soma_resto, qtd_resto = serie(k + 1)
    return termo + soma_resto, qtd_resto + 1


soma, qtd = serie()
print(f"Quantidade de termos: {qtd}")
print(f"Soma: {soma:.4f}")
```

## Questão 9 — Produto dos elementos de um vetor

### Enunciado

Escreva uma função recursiva para calcular o produto dos elementos de um vetor. Use apenas multiplicação; não use funções matemáticas.

### Solução

```python
def produto_recursivo(vetor, indice=0):
    if indice == len(vetor):
        return 1
    else:
        return vetor[indice] * produto_recursivo(vetor, indice + 1)
```

## Questão 10 — Inversão de string

### Enunciado

Desenvolva uma função recursiva para inverter uma string recebida como parâmetro.

**Exemplo:** entrada `python`; saída `nohtyp`.

### Solução

```python
def inverter_string(s, indice=0):
    if indice >= len(s):
        return ""

    return inverter_string(s, indice + 1) + s[indice]
```
