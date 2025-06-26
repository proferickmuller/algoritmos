import random
import timeit

DESCONTOS = {"0": 0, "10": 0.05, "20": 0.10, "50": 0.15}
DESCONTOS_KEYS = tuple(reversed(sorted(DESCONTOS.keys())))

precos = [random.randint(10, 100) for _ in range(200_000)]
quantidades = [x for x in range(1, 61)]


def calcular_desconto(quantidade):
    for limite in reversed(DESCONTOS_KEYS):
        if quantidade >= int(limite):
            return DESCONTOS[limite]


t1 = timeit.default_timer()
for i in range(len(precos)):
    q = random.choice(quantidades)
    [precos[i], q, calcular_desconto(q)]
t2 = timeit.default_timer()
print(t2 - t1)

# -----------

print("-" * 80)


CACHE_DESCONTOS = {}


def calcular_desconto_cache(quantidade):
    if CACHE_DESCONTOS and quantidade in CACHE_DESCONTOS:
        return CACHE_DESCONTOS[quantidade]
    else:
        for limite in reversed(DESCONTOS_KEYS):
            if quantidade >= int(limite):
                CACHE_DESCONTOS[quantidade] = DESCONTOS[limite]
                return DESCONTOS[limite]


t1 = timeit.default_timer()
for i in range(len(precos)):
    q = random.choice(quantidades)
    (precos[i], q, calcular_desconto_cache(q))
t2 = timeit.default_timer()
print(t2 - t1)

print("-" * 80)


# @functools.lru_cache(200)
# def calcular_desconto_mru(quantidade):
#     for limite in reversed(DESCONTOS_KEYS):
#         if quantidade >= int(limite):
#             return DESCONTOS[limite]


# t1 = timeit.default_timer()
# for i in range(len(precos)):
#     q = random.choice(quantidades)
#     [precos[i], q, calcular_desconto_mru(q)]
# t2 = timeit.default_timer()
# print(t2 - t1)
