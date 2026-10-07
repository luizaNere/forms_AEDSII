'''
Adapte o algoritmo de busca binária para localizar a primeira 
ocorrência de uma chave em uma lista que permite elementos 
duplicados. Ao encontrar o valor alvo, o algoritmo não deve 
encerrar a execução imediatamente; em vez disso, deve continuar 
a busca no subintervalo à esquerda para garantir que o índice 
retornado seja o menor possível.

Exemplo: Em lista = [2, 4, 4, 4, 5, 7], a busca pela chave 4 deve retornar o índice 1.
'''

def busca_binaria(lista, chave):
     inicio = 0
     fim = len(lista) - 1
     resultado = -1

     while inicio <= fim:
          meio = (inicio + fim) // 2

          if lista[meio] == chave:
               resultado = meio
               fim = meio - 1
          elif  lista[meio] > chave:
               fim = meio - 1
          else:
               inicio = meio + 1
               
     return resultado