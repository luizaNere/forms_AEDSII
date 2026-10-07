'''
Implemente uma função recursiva raiz(N, A, E) que calcula a raiz 
quadrada de N.

A função recebe:
- N – o número cuja raiz quadrada se deseja calcular (float ou int);
- A – uma aproximação inicial para a raiz;
- E – o erro máximo admissível (precisão).

A função deve seguir a seguinte lógica:
- Se |A² – N| < E, então a função retorna A como resultado final.
- Caso contrário, a função retorna o resultado da chamada recursiva: 
Raiz(N, (A² + N) / (2 * A), E).

A função deve exibir cada aproximação (A) com 6 casas decimais antes 
da próxima chamada recursiva.

Exemplo:
raiz(9, 4, 0.01)

Saída:
Aproximação 4.000000
Aproximação 3.125000
Aproximação 3.002500
Aproximação 3.000001
Resultado final: 3.000001
'''

def raiz(N, A, E):

    print(f"Aproximação {A:.6f}")

    if abs(A ** 2 - N) < E:
        print(f"Resultado final: {A:.6f}")
        return A
    
    else:
        return raiz(N, (A ** 2 + N) / (2 * A), E)