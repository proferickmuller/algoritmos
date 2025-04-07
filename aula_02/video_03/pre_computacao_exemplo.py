DESCONTOS = {"0": 0, "10": 0.05, "20": 0.10, "50": 0.15}


def calcular_desconto(quantidade):
    d = sorted(DESCONTOS.keys())
    for limite in reversed(d):
        if quantidade >= int(limite):
            return DESCONTOS[limite]


# -----------

CACHE_DESCONTOS = {}


def calcular_desconto_cache(quantidade):
    if quantidade in CACHE_DESCONTOS:
        return CACHE_DESCONTOS[quantidade]
    else:
        d = sorted(DESCONTOS.keys())
        for limite in reversed(d):
            if quantidade >= int(limite):
                return DESCONTOS[limite]
