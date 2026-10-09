'''
O somatório dos elementos de um vetor pode ser calculado recursivamente 
utilizando a seguinte formula abaixo.

Faça um programa que:
a) preencha por leitura (do teclado) um vetor de 10 elementos reais;
b) imprima o conteúdo desse vetor;
c) imprima o resultado do somatório dos elementos desse vetor, 
calculado por essa função recursiva.

Considere L como o índice do primeiro item do vetor (X) e M o índice do
último item do vetor (X).

X=[2,4,6,8]
L=0
M=3
'''

def somatorio_recursivo(vetor, L, M):
    if L == M:
        return vetor[L]
    else:
        meio = (L + M) // 2
        return somatorio_recursivo(vetor, L, meio) + somatorio_recursivo(vetor, meio + 1, M)


vetor = []
for i in range(10):
    valor = float(input(f"Digite o {i+1}º elemento do vetor: "))
    vetor.append(valor)

print("Conteúdo do vetor:", vetor)

L = 0
M = len(vetor) - 1
resultado = somatorio_recursivo(vetor, L, M)
print("Resultado do somatório: ", resultado)