'''
Desenvolva uma função recursiva para inverter uma string recebida 
como parâmetro.

Entrada: python
Saída: nohtyp
'''

def inverter_string(s, indice = 0):

    if indice >= len(s):
        return ""
    
    return inverter_string(s, indice + 1) + s[indice]