'''
Implemente a função busca_binaria(lista, chave), que realiza a busca
de um elemento em uma lista Python previamente ordenada de forma 
crescente.

A função deve localizar a chave e retornar o seu índice.

Caso a chave não esteja presente, o retorno deve ser -1.

Restrição: É proibido o uso de funções ou métodos prontos 
de busca ou posicionamento, como lista.index(), lista.count() 
ou o módulo nativo bisect. A lógica do algoritmo de divisão 
e conquista deve ser implementada manualmente.
'''

def busca_binaria(lista, chave):
    e = 0
    d = len(lista) - 1

    while e <= d:
        meio = (e+d)//2

        if lista[meio] == chave:
            return meio
        elif  lista[meio] > chave:
            d = meio - 1
        else:
            e = meio + 1

    return -1