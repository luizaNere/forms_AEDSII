'''
Elabore uma função recursiva que calcule o valor da série a seguir. 
Utilizar tantos termos quantos forem necessários para o valor do último 
termo seja menor que 0,01. Indique a quantidade mínima de termos 
necessário e o valor da soma.

S = 70/7 + 69/14 + 68/21 + 67/28 + ...
'''

def serie(k = 1):
    termo = (71 - k) / (7 * k)

    if termo < 0.01:
        return termo, 1

    soma_resto, qtd_resto = serie(k + 1)
    return termo + soma_resto, qtd_resto + 1


soma, qtd = serie()
print(f"Quantidade de termos: {qtd}")
print(f"Soma: {soma:.4f}")