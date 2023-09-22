def particao(A, esquerda, direita):
    pivo = A[esquerda]
    i = esquerda
    j = direita

    while i < j:
        while i < direita and A[i] <= pivo:
            i += 1
        while j > esquerda and A[j] > pivo:
            j -= 1
        if i < j:
            A[i], A[j] = A[j], A[i]

    A[esquerda], A[j] = A[j], A[esquerda]
    return j

def quicksort(A, esquerda, direita):
    if esquerda < direita:
        indice_pivo = particao(A, esquerda, direita)
        quicksort(A, esquerda, indice_pivo - 1)
        quicksort(A, indice_pivo + 1, direita)


A = [5,2,8,10,12,15,30,21,98,45,100,245,6,15,78,29,150]
quicksort(A, 0, len(A) - 1)
print(A)