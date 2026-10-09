'''
Considere a seguinte soma:

S = 1/2 + 2/3 + 3/5 + 4/7 + ... + 20/39

Para achar a solução dessa série escreva:
a) uma função recursiva (o resultado da soma é o valor do primeiro termo 
somado à chamada recursiva para calcular a soma a partir do segundo termo).
'''

def soma_recursiva(n):
    if n == 1:
        return 1/2
    else:
        return n/(2 * n - 1) + soma_recursiva(n - 1)