'''
Escreva uma função recursiva que converta um número inteiro positivo 
da base decimal para a base binária.

A função deve receber um número inteiro (ex.: 3) e retornar uma string
 representando o número em binário (ex.: "11").

Utilize o método das divisões sucessivas por 2: a cada chamada
recursiva, o resto da divisão por 2 corresponde a um dígito binário 
(do menos significativo para o mais significativo).

O programa principal deve ler um valor decimal da entrada e exibir o 
binário correspondente como saída.

Exemplo:
Entrada: 3
Saída: 11
'''

def decimal_para_binario(n):
    if n == 0:
        return ""
    elif n == 1:
        return "1"
    else:
        return decimal_para_binario(n // 2) + str(n % 2)