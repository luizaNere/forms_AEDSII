'''
Implemente uma função em Python que utilize busca binária para 
verificar a existência de um caractere em uma string ordenada 
alfabeticamente.

Entrada: Uma string s e um caractere chave.

Retorno: O índice da primeira ocorrência da chave ou -1 caso 
não seja encontrada.

Restrição: Não utilize o operador in ou o método find(); a lógica 
de divisão e conquista deve ser implementada manualmente.
'''

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