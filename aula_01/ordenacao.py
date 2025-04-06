import util

# visualizacao https://dsa-visualizer-arm.netlify.app/sorting

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


lista = util.gera_lista_aleatoria(300, 400)
# print("Lista desordenada:", lista)

lista_ordenada = bubble_sort(lista)
# print("Lista ordenada:", lista_ordenada)
