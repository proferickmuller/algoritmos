import timeit

VALIDO = True
SKIP_FACTOR = 13

t = timeit.default_timer()
numero_maximo = 100_000
numero_atual = 1
lista_numeros = []
while VALIDO:
    if numero_atual < numero_maximo and numero_atual % SKIP_FACTOR != 0:
        lista_numeros.append(numero_atual)
        numero_atual += 1
    else:
        VALIDO = False

print("tempo com while e flag: %.8f" % (timeit.default_timer() - t))

# -------------------

t = timeit.default_timer()
numero_maximo = 100_000
numero_atual = 1
lista_numeros = []
while True:
    if numero_atual < numero_maximo and numero_atual % SKIP_FACTOR != 0:
        break

    lista_numeros.append(numero_atual)
    numero_atual += 1
print("tempo com while e break: %.8f" % (timeit.default_timer() - t))
