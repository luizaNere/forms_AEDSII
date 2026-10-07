'''
Implemente um simulador do jogo 'Adivinhação Numérica' usando busca 
binária. O computador deve possuir um número secreto (ex: 750) dentro 
de um intervalo de 1 a 1000.

Requisitos:

O algoritmo deve tentar adivinhar o número ajustando os limites inicio 
e fim a cada tentativa.

A cada palpite (meio do intervalo), o programa deve informar se o 
número secreto é maior ou menor que o palpite atual.

Saída: Ao encontrar o número, o programa deve exibir o valor 
descoberto e o total de tentativas realizadas.

Desafio: Garanta que o número máximo de tentativas nunca ultrapasse 
log_2(1000) ou seja (aproximadamente 10 tentativas).
'''

def adivinhar(secreto, minimo=1, maximo=1000):
    inicio = minimo
    fim = maximo
    tentativas = 0

    while inicio <= fim:
        meio = (inicio + fim) // 2
        tentativas += 1
        print(f"Tentativa {tentativas}: palpite = {meio}")

        if meio == secreto:
            print(f"Número descoberto: {meio}")
            print(f"Total de tentativas: {tentativas}")
            return meio, tentativas
        
        elif secreto > meio:
            print("  O número secreto é maior")
            inicio = meio + 1
            
        else:
            print("  O número secreto é menor")
            fim = meio - 1

    return None, tentativas


adivinhar(750)