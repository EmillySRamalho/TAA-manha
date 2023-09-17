def mergesort(lista, inicio, fim):
    if inicio < fim:
        meio = (inicio + fim) // 2 
        mergesort(lista, inicio, meio)
        mergesort(lista, meio + 1, fim)
        merge(lista, inicio, meio, fim)

def merge(lista, inicio, meio, fim):
    tamanhoEsq = meio - inicio + 1
    tamanhoDir = fim - meio
    vetoresquerdo = [0] * tamanhoEsq
    vetordireito = [0] * tamanhoDir

    for i in range(tamanhoEsq):
        vetoresquerdo[i] = lista[inicio + i]

    for j in range(tamanhoDir):
        vetordireito[j] = lista[meio + 1 + j]

    idxEsq = 0
    idxDir = 0
    k = inicio

    while idxEsq < tamanhoEsq and idxDir < tamanhoDir:
        if vetoresquerdo[idxEsq] <= vetordireito[idxDir]:
            lista[k] = vetoresquerdo[idxEsq]
            idxEsq += 1
        else:
            lista[k] = vetordireito[idxDir]
            idxDir += 1
        k += 1

    while idxEsq < tamanhoEsq:
        lista[k] = vetoresquerdo[idxEsq]
        idxEsq += 1
        k += 1

    while idxDir < tamanhoDir:
        lista[k] = vetordireito[idxDir]
        idxDir += 1
        k += 1

vetor = [0, 1, 8, 5, 10]
mergesort(vetor, 0, len(vetor) - 1)
print(vetor)
