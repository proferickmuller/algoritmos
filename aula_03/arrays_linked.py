from typing import Optional, Self

# uma lista

frutas = ["banana", "maçã", "uva", "manga", "abacate", "abacaxi"]
print(frutas[2])  # uva
print(frutas[2 : len(frutas)])


# lista ligada
class NodeListaLigada:
    def __init__(self, valor: int, proximo: Optional[Self]):
        self.valor = valor
        self.proximo = proximo

    def __str__(self):
        if self.proximo is None:
            return "Meu valor é " + str(self.valor) + ", e não tenho um próximo."
        return (
            "Meu valor é "
            + str(self.valor)
            + ", e o valor do próximo é "
            + str(self.proximo.valor)
        )


# criar uma lista ligada, modelo fifo
node_inicial = NodeListaLigada(1, None)
node_2 = NodeListaLigada(2, node_inicial)
node_3 = NodeListaLigada(3, node_2)
node_4 = NodeListaLigada(4, node_3)

print(node_inicial)
print(node_2)
print(node_3)
print(node_4)


# percorrer a lista

print("\nPercorrendo a lista.")


def traverse(n: NodeListaLigada):
    """Dado um Node Inicial, vamos ler todos os itens"""
    atual = n
    while atual is not None:
        print(atual)
        atual = atual.proximo


traverse(node_4)


def pop(node: NodeListaLigada) -> int:
    """pop tira o ultimo item da lista, o que não tem nenhuma referencial"""
    current_node: NodeListaLigada = node
    last_node: NodeListaLigada = None

    while current_node.proximo is not None:
        last_node = current_node
        current_node = current_node.proximo

    value = current_node.valor
    last_node.proximo = None
    return value


print("\nVamos tirar o ultimo item")
traverse(node_4)
print("--- Tirando o valor: " + str(pop(node_4)))
traverse(node_4)
