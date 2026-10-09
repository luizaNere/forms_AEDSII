'''
Escreva uma função recursiva para calcular a função de Ackermann 
A (m, n), sendo m e n valores inteiros não negativos, dada por:

n + 1                          se m = 0
A(m, n)  =  A(m-1,1)           se m > 0 e n = 0
A(m-1, A(m, n-1))              se m > 0 e n > 0

(obs: Como gera chamadas recursivas profundas, a função de Ackermann 
é usada para testar limites de pilha em compiladores, linguagens de 
programação e ambientes de execução. 

Teste 1: A(0, 5)
Saída: 6

Teste 2: A(1, 5)
Saída: 7

Teste 3: A(2, 5)
Saída: 13
'''

def ackermann(m, n):
    if m == 0:
        return n + 1
    elif n == 0:
        return ackermann(m - 1, 1)
    else:
        return ackermann(m - 1, ackermann(m, n - 1))