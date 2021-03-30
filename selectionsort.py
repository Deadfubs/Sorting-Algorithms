"""
Algoritmo de ordenação Selection Sort
"""

import random
import time

# variável global para contar o número de comparações
comp = 0

# ----------------------------------------------------------------------------------------------------------------------
"""
Ordena selecionando os menores elementos da lista e colocando no início do vetor
"""
def selectionsort(vetor):
    global comp
    i = 0
    while i < len(vetor) - 1:
        menor = i
        j = i + 1
    # Confirma qual é o menor elemento
        while j < len(vetor):
            comp += 1
            if vetor[j] < vetor[menor]:
            menor = j
        j += 1
    comp += 1
    if menor != i:
    aux = vetor[i]
    vetor[i] = vetor[menor]
    vetor[menor] = aux
    i += 1
# ----------------------------------------------------------------------------------------------------------------------


# main------------------------------------------------------------------------------------------------------------------
# Implementação da lista a ser utilizada para a ordenação
vetor = list(range(0, 10000))
random.shuffle(vetor)

print("O vetor inicial é:", end=" ")
print(vetor)

tI = time.time()
selectionsort(vetor)
tF = time.time()

tempo = (tF-tI)*1000

print("O vetor ordenado é:", end=" ")
print(vetor)
print(f'O número de comparações é: {comp}')
print(f'O tempo total foi: {round(tempo, 2)} ms')