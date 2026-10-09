'''
Escreva uma função recursiva para calcular o produto dos elementos de um 
vetor. Use apenas multiplicação. Não use funções matemáticas.
'''

def produto_recursivo(vetor, indice = 0):
    if indice == len(vetor):
        return 1
    else:
        return vetor[indice] * produto_recursivo(vetor, indice + 1)
