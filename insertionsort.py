"""
Algoritmo de ordenação Insertion Sort
"""

import random
import time

# variável global para contar o número de comparações
comp = 0


# ----------------------------------------------------------------------------------------------------------------------
"""
O algoritmo insere cada elemento na sua posição correspondente no vetor. O valor do elemento a ser inserido é a chave 
de comparação para saber onde deve ser inserido. O algoritmo é excelente quando você já possui um vetor ordenado ou
próximo disso e desja inserir um novo elemento de forma ordenada no vetor. É um método estável.
"""
def insertionsort(v):
    global comp
    i = 1
    while i < len(v):
        aux = v[i]
        troca = False
        j = i - 1
        while j >= 0 and v[j] > aux:
            v[j + 1] = v[j]
            troca = True
            j -= 1
            comp+=1
        if troca:
            v[j + 1] = aux
        i += 1
# ----------------------------------------------------------------------------------------------------------------------


# main------------------------------------------------------------------------------------------------------------------
# Implementação da lista a ser utilizada para a ordenação
vetor = list(range(0, 10000))
random.shuffle(vetor)

print("O vetor inicial é:", end=" ")
print(vetor)

tI = time.time()
insertionsort(vetor)
tF = time.time()

tempo = (tF-tI)*1000

print("O vetor ordenado é:", end=" ")
print(vetor)
print(f'O número de comparações é: {comp}')
print(f'O tempo total foi: {round(tempo, 2)} ms')