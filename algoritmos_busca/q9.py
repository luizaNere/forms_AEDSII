'''
Implemente uma função em Python para calcular a frequência de uma 
chave em uma lista ordenada, utilizando exclusivamente busca binária.

Requisitos:

Não utilize o método lista.count().

Realize duas buscas binárias distintas: uma para localizar o índice 
da primeira ocorrência e outra para o índice da última ocorrência da 
chave.

Calcule o total de repetições através da fórmula: 
total = índice_último - índice_primeiro + 1.

Se a chave não estiver presente em nenhuma das buscas, o retorno deve 
ser 0.
'''

def primeira_ocorrencia(lista, chave):
    inicio = 0
    fim = len(lista) - 1
    resultado = -1

    while inicio <= fim:
        meio = (inicio + fim) // 2

        if lista[meio] == chave:
            resultado = meio
            fim = meio - 1            # continua à esquerda
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
            inicio = meio + 1         # continua à direita
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