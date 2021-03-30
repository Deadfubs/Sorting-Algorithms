"""
Algoritmo de ordenação Bubble Sort
"""

import random
import time

# variável global para contar o número de comparações
comp = 0

# ----------------------------------------------------------------------------------------------------------------------
"""
Percorre diversas vezes o vetor fazendo flutuar para o topo o maior elemento da sequência. É um méotodo interessante
para vetores pequenos por não realizar trocas caso o vetor já esteja ordenado e também por ser um método estável.
"""
def bubblesort(vetor):
    global comp
    for i in range(len(vetor)):
        for j in range(len(vetor)-1):
            comp += 1
            if vetor[j] > vetor[j+1]:
                aux = vetor[j+1]
                vetor[j+1] = vetor[j]
                vetor[j] = aux
# ----------------------------------------------------------------------------------------------------------------------


# main------------------------------------------------------------------------------------------------------------------
# Implementação da lista a ser utilizada para a ordenação
vetor = list(range(0, 10))
random.shuffle(vetor)

print("O vetor inicial é:", end=" ")
print(vetor)

tI = time.time()
bubblesort(vetor)
tF = time.time()

tempo = (tF-tI)*1000

print("O vetor ordenado é:", end=" ")
print(vetor)
print(f'O número de comparações é: {comp}')
print(f'O tempo total foi: {round(tempo, 2)} ms')