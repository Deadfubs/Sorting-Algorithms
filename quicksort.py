"""
Quick Sort recursivo baseado na abordagem de Nico Lomuto (pivô inicializado pela esquerda do vetor)
"""
import random
import time
import sys
# sys.setrecursionlimit(100000000) # (NÃO USAR, PODE TRAVAR O COMPUTADOR - Quicksort tem um comportamento muito ruim
                                   # quando o vetor já está ordenado)

# variável global para contar o número de comparações
comp = 0

# ----------------------------------------------------------------------------------------------------------------------
# As entradas são o vetor a ser ordenado, a posição inicial e a posição final.
def quicksort(vetor, pI, pF):
    if pI < pF: # Condição de existência
        pF_pivo = particionar(vetor, pI, pF)
        quicksort(vetor, pI, pF_pivo-1) # Ordenar os elementos menores que o pivô
        quicksort(vetor, pF_pivo+1, pF) # Ordenar os elementos maiores que o pivô
# ----------------------------------------------------------------------------------------------------------------------


# ----------------------------------------------------------------------------------------------------------------------
def particionar(vetor, pI, pF):
    global comp
    pivo = vetor[pI] # O primeiro elemento do vetor
    destino = pI # Destino do pivô, inicializado no local onde o pivo está
    i = pI + 1 # Parâmetro para percorrer o restante do vetor
    while i <= pF:
        comp += 1
        if vetor[i] < pivo: # Verifica se o elemento iterado é menor do que o pivo
            destino += 1  # Incrementa a posição de destino
            trocar(vetor, destino, i)
        i += 1 # Passa próximo elemento

    trocar(vetor, pI, destino)

    return destino
# ----------------------------------------------------------------------------------------------------------------------


# ----------------------------------------------------------------------------------------------------------------------
# Troca os elementos do vetor
def trocar(vetor, e1, e2):
    aux = vetor[e1]
    vetor[e1] = vetor[e2]
    vetor[e2] = aux
# ----------------------------------------------------------------------------------------------------------------------


# main------------------------------------------------------------------------------------------------------------------
# Implementação da lista a ser utilizada para a ordenação
vetor = list(range(0, 1000))
random.shuffle(vetor)

print('O vetor inicial é: ', end='')
print(vetor)

tI = time.time()
quicksort(vetor, 0, len(vetor)-1)
tF = time.time()

tempo = (tF-tI)*1000


print(f'O vetor ordenado é: ', end='')
print(vetor)
print(f'O número de comparações é: {comp}')
print(f'O tempo total foi: {round(tempo, 2)} ms')