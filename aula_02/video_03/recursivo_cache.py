import timeit

NUMERO_FATORES = 20


def fibonacci_recursivo_normal(numero_fatores):
    if numero_fatores <= 1:
        return numero_fatores
    else:
        return fibonacci_recursivo_normal(
            numero_fatores - 1
        ) + fibonacci_recursivo_normal(numero_fatores - 2)


def fibonacci_simples(numero_fatores):
    atual = 1
    soma = 0
    for i in range(numero_fatores):
        atual, soma = soma, atual + soma
    return soma


t = timeit.default_timer()
fibonacci_recursivo_normal(NUMERO_FATORES)
print("tempo recursivo normal: %.8f" % (timeit.default_timer() - t))

# -------------------

t = timeit.default_timer()
fibonacci_simples(NUMERO_FATORES)
print("tempo simples: %.8f" % (timeit.default_timer() - t))
