import timeit


# pre-computacao
def fibonacci_sem_cache(n):
    if n <= 1:
        return n
    else:
        return fibonacci_sem_cache(n - 1) + fibonacci_sem_cache(n - 2)


t = timeit.default_timer()
# Teste (lento para n > 35)
print(fibonacci_sem_cache(45))  # Demora vários segundos
print("tempo sem cache: {}".format(timeit.default_timer() - t))

# ---

cache = {}


def fibonacci_memo(n):
    if n in cache:
        return cache[n]  # Retorna o valor pré-computado
    if n <= 1:
        result = n
    else:
        result = fibonacci_memo(n - 1) + fibonacci_memo(n - 2)
    cache[n] = result  # Armazena no cache antes de retornar
    return result


t = timeit.default_timer()
print(fibonacci_memo(45))
print("tempo usando cache: {}".format(timeit.default_timer() - t))


"""
1134903170
tempo sem cache: 118.54423740701168
1134903170
tempo usando cache: 1.6225007129833102e-05
"""
