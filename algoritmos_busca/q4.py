'''
Implemente uma função em Python para encontrar o Limite Inferior 
(Lower Bound) de uma chave em uma lista ordenada. A função deve 
retornar o índice do menor elemento que seja maior ou igual à chave.

Entrada: Uma lista de inteiros ordenada e um valor chave.

Saída: O índice do elemento que satisfaz a condição. 
Se todos os elementos da lista forem menores que a chave, 
a função deve retornar -1.

Exemplo: Para lista = [10, 20, 30, 40, 50] e chave = 35, o retorno deve ser 3 (índice do valor 40).
'''

def lower_bound (lista, chave):
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