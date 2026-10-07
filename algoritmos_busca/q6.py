'''
Em um sistema de agendamento médico, os horários disponíveis são 
armazenados em uma lista de strings ordenada: 
horarios = ['08:00', '09:30', '14:00', '15:30', '16:00'].

Implemente uma função que utilize busca binária para localizar o 
primeiro horário disponível que seja maior ou igual ao horário 
solicitado pelo paciente (chave).

Exemplo: Se o paciente solicita '15:00', a função deve retornar o 
índice 3 (correspondente a '15:30').

Caso de exceção: Se o horário solicitado for posterior ao último 
horário disponível, a função deve retornar -1.

Restrição: Utilize a comparação direta de strings do Python e 
mantenha a eficiência O(log n).
'''

def primeiro_horario_disponivel(horarios, chave):
    inicio = 0
    fim = len(horarios) - 1
    resultado = -1

    while inicio <= fim:
        meio = (inicio + fim) // 2

        if horarios[meio] >= chave:
            resultado = meio 
            fim = meio - 1
        else:
            inicio = meio + 1

    return resultado