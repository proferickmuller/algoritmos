def calcular_troco_minimo(valor, moedas):
    """
    Calcula o troco mínimo utilizando o algoritmo greedy.
    
    :param valor: Valor total do troco a ser dado.
    :param moedas: Lista de valores das moedas disponíveis (em ordem decrescente).
    :return: Dicionário com a quantidade de cada moeda usada.
    """
    troco = {}
    for moeda in moedas:
        if valor == 0:
            break
        quantidade = valor // moeda
        if quantidade > 0:
            troco[moeda] = quantidade
            valor -= quantidade * moeda
    if valor > 0:
        raise ValueError("Não é possível dar o troco exato com as moedas disponíveis.")
    return troco

# Exemplo de uso
if __name__ == "__main__":
    moedas_disponiveis = [100, 50, 25, 10, 5, 1]  # Valores em centavos
    valor_troco = 287  # Valor do troco em centavos (exemplo: R$2,87)
    
    try:
        resultado = calcular_troco_minimo(valor_troco, moedas_disponiveis)
        print("Troco mínimo:")
        for moeda, quantidade in resultado.items():
            print(f"{quantidade} moeda(s) de {moeda} centavo(s)")
    except ValueError as e:
        print(e)