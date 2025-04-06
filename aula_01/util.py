import random

def gera_lista_aleatoria(tamanho, limite):
    """Gera uma lista de tamanho com numeros entre 1 e limite,
    sem numeros repetidos."""
    assert tamanho <= limite, "Tamanho da lista maior que o limite"
    
    # Usando um conjunto (set) para verificação O(1) de pertinência
    numeros_usados = set()
    lista = []
    
    while len(lista) < tamanho:
        num = random.randint(1, limite)
        if num not in numeros_usados:
            numeros_usados.add(num)
            lista.append(num)
    
    return lista