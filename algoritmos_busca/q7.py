'''
Implemente a função localizar_ou_inserir(lista_ids, novo_id), que 
utiliza busca binária para gerenciar o cadastro de alunos.

Cenário A: Se o novo_id já estiver presente na lista, a função deve 
retornar o seu índice atual.

Cenário B: Se o novo_id não for encontrado, a função deve retornar 
o índice da posição ideal de inserção, ou seja, o ponto onde o ID 
deve ser inserido para que a lista permaneça ordenada.

Exemplo: Em [10, 20, 30], buscar por 20 retorna 1. Buscar por 25 
também retorna 2 (posição onde o 25 entraria).
'''

def localizar_ou_inserir(lista_ids, novo_id):
    inicio = 0
    fim = len(lista_ids) - 1

    while inicio <= fim:
        meio = (inicio + fim) // 2

        if lista_ids[meio] == novo_id:
            return meio         # Cenário A: já existe
        elif lista_ids[meio] < novo_id:
            inicio = meio + 1
        else:
            fim = meio - 1

    return inicio       # Cenário B: posição ideal de inserção