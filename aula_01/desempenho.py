import os
import timeit


def buscar_por_primeira_letra(nomes, letra):
    resultado = []
    letra_ord = ord(letra)
    for iterations, nome in enumerate(nomes):
        if len(nome) > 0 and ord(nome[0]) == letra_ord:
            resultado.append(nome)
    return resultado, iterations + 1


# Exemplo de uso:
# nomes = ["Ana", "Bruno", "Alice", "Carlos"]
# print(buscar_por_primeira_letra(nomes, 'A'))  # Saída: ['Ana', 'Alice']


def buscar_por_primeira_letra_ordenada(nomes, letra):
    resultado = []
    letra_ord = ord(letra)
    for iterations, nome in enumerate(nomes):
        if len(nome) == 0:
            continue
        if ord(nome[0]) == letra_ord:
            resultado.append(nome)
        elif ord(nome[0]) > letra_ord:
            break
    return resultado, iterations + 1


# Exemplo de uso:
# nomes = ["Ana", "Alice", "Bruno", "Carlos"]
# print(buscar_por_primeira_letra_ordenada(nomes, 'A'))  # Saída: ['Ana', 'Alice']


with open(
    os.path.join(os.path.dirname(os.path.abspath(__file__)), "nomes.txt"), "r"
) as f_nomes:
    nomes = f_nomes.readlines()

nomes = [n.strip() for n in nomes]

t1 = timeit.default_timer()
print("total de iteracoes: {}".format(
    buscar_por_primeira_letra(nomes, "G")[1]))
t2 = timeit.default_timer()
print("tempo de execucao: {}".format(t2 - t1))


nomes_ordenada = sorted(nomes)
t1 = timeit.default_timer()
print(
    "total de iteracoes (ordenada): {}".format(
        buscar_por_primeira_letra_ordenada(nomes_ordenada, "G")[1]
    )
)
t2 = timeit.default_timer()
print("tempo de execucao (ordenada): {}".format(t2 - t1))

t1 = timeit.default_timer()
print("total de iteracoes: {}".format(
    buscar_por_primeira_letra(nomes, "G")[1]))
t2 = timeit.default_timer()
print("tempo de execucao: {}".format(t2 - t1))


print('-' * 80)
nro_execucoes = 100_000


print(f"em {nro_execucoes} execucoes...")
t1 = timeit.default_timer()
for _ in range(nro_execucoes):
    buscar_por_primeira_letra(nomes, "G")
t2 = timeit.default_timer()
total_sem_ordenacao = t2 - t1
print("tempo de execucao: {}".format(total_sem_ordenacao))

t1 = timeit.default_timer()
for _ in range(nro_execucoes):
    buscar_por_primeira_letra_ordenada(nomes, "G")
t2 = timeit.default_timer()

total_com_ordenacao = t2 - t1
print("tempo de execucao (ordenada): {}".format(total_com_ordenacao))

print("o desordenado roda {:.4f} vezes mais lento".format(
    total_sem_ordenacao / total_com_ordenacao))
