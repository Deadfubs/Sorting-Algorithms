"""
Algoritmo de ordenação Shell Sort
"""

import random
import time


# variável global para contar o número de comparações
comp = 0

# ----------------------------------------------------------------------------------------------------------------------
"""
O algoritmo passa várias vezes pelo vetor divindo-o em segmentos menores e aplicando o método de inserção em 
cada um deles
"""
def shellsort(v):
    global comp
    passo = len(v) // 2 #Distância da comparação
    while passo > 0:
        i = passo
        while i < len(v):
            aux = v[i]
            troca = False
            j = i - passo
            while j >= 0 and v[j] > aux:
                comp += 1
                v[j + passo] = v[j]
                troca = True
                j -= passo
            if troca:
                v[j + passo] = aux
            i += 1
        passo = passo // 2
# ----------------------------------------------------------------------------------------------------------------------

# main------------------------------------------------------------------------------------------------------------------
# Implementação da lista a ser utilizada para a ordenação
vetor = list(range(0, 10000))
random.shuffle(vetor)

print("O vetor inicial é:", end=" ")
print(vetor)

tI = time.time()
shellsort(vetor)
tF = time.time()

tempo = (tF-tI)*1000

print("O vetor ordenado é:", end=" ")
print(vetor)
print(f'O número de comparações é: {comp}')
print(f'O tempo total foi: {round(tempo, 2)} ms')
