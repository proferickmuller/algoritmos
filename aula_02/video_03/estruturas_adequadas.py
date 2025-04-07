import random
import timeit

# preciso armazenar os 100 primeiros numeros de uma lista de 500 que podem estar repetidos


def gera_lista_aleatoria_repetida(tamanho, limite):
    """Gera uma lista de tamanho com numeros entre 1 e limite,
    podendo haver repeticao de numeros na lista."""
    return [random.randint(1, limite) for _ in range(tamanho)]


lista_aleatoria = gera_lista_aleatoria_repetida(10000, 65)

# -------------------

t = timeit.default_timer()
lista_unicos = []
for num in lista_aleatoria:
    if num not in lista_unicos:
        lista_unicos.append(num)
print("tempo com lista: %.8f" % (timeit.default_timer() - t))

t = timeit.default_timer()
set_unicos = set(lista_aleatoria)
print("tempo com set: %.8f" % (timeit.default_timer() - t))
