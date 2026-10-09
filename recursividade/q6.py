'''
Escreva uma função recursiva para calcular o valor de x^n (x elevado a n), 
usando multiplicações. Não usar: o operador * *, pow(), math.pow() ou 
outra função matemática.
'''

def potencia_recursiva(x, n):
    if n == 0:
        return 1
    else:
        return x * potencia_recursiva(x, n - 1)