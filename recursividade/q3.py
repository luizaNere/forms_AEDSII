'''
Construa uma função recursiva MDC que determina o maior divisor comum 
de dois inteiros M e N por meio do Algoritmo de Euclides, como segue:

MDC(N, M)                 se N > M
MDC(M, N) = M         se N = 0
MDC(N, M mod N)    se N > 0 e N <= M
'''

def mdc(m, n):
    if n == 0:
        return m
    elif n > m:
        return mdc(n, m)
    else:
        return mdc(n, m % n)