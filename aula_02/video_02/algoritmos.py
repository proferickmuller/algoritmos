def bubble_sort(lista):
    """Ordena uma lista de numeros utilizando o algoritmo Bubble Sort"""
    trocou = True
    while trocou:
        trocou = False
        for i in range(len(lista)-1):
            if lista[i] > lista[i+1]:
                lista[i], lista[i+1] = lista[i+1], lista[i]
                trocou = True

    return lista

def insert_sort(lista):
    """
    Ordena uma lista de numeros utilizando o algoritmo Insert Sort
    Que cria uma nova lista ordenada a partir da existente
    """

    for i in range(1, len(lista)):
        chave = lista[i]
        j = i-1
        while j >= 0 and lista[j] > chave:
            lista[j+1] = lista[j]
            j -= 1
        lista[j+1] = chave
    return lista

def selection_sort(lista):
    """
    Ordena uma lista de numeros utilizando o algoritmo Selection Sort
    Que varre a lista ordenando os valores em pares.
    """
    for i in range(len(lista)):
        min_idx = i
        for j in range(i+1, len(lista)):
            if lista[min_idx] > lista[j]:
                min_idx = j
        lista[i], lista[min_idx] = lista[min_idx], lista[i]
    return lista

def quick_sort(lista):
    """
    Ordena uma lista de numeros utilizando o algoritmo Quick Sort
    Que elege um pivo e divide a lista em menores e maiores
    E recursivamente ordena as listas menores e maiores
    """
    if len(lista) <= 1:
        return lista
    else:
        pivot = lista[0]
        menores = [i for i in lista[1:] if i <= pivot]
        maiores = [i for i in lista[1:] if i > pivot]
        return quick_sort(menores) + [pivot] + quick_sort(maiores)


def heap_sort(lista):
    """
    Ordena uma lista de numeros utilizando o algoritmo Heap Sort
    Que cria um heap maximo (numa estrutura tree-like) e extrai os elementos um por um
    """
    def heapify(lista, n, i):
        maior = i
        esq = 2 * i + 1
        dir = 2 * i + 2

        if esq < n and lista[esq] > lista[maior]:
            maior = esq

        if dir < n and lista[dir] > lista[maior]:
            maior = dir

        if maior != i:
            lista[i], lista[maior] = lista[maior], lista[i]
            heapify(lista, n, maior)

    n = len(lista)

    # construir o heap maximo
    for i in range(n//2 - 1, -1, -1):
        heapify(lista, n, i)

    # extrair os elementos do heap um por um
    for i in range(n-1, 0, -1):
        lista[0], lista[i] = lista[i], lista[0]
        heapify(lista, i, 0)

    return lista

