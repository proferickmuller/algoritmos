class GrafoMatriz:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.matriz_adjacencia = [[0] * num_vertices for _ in range(num_vertices)]

    def adicionar_aresta(self, origem, destino, peso=1):
        self.matriz_adjacencia[origem][destino] = peso
        self.matriz_adjacencia[destino][origem] = peso  # Para grafos não direcionados

    def remover_aresta(self, origem, destino):
        self.matriz_adjacencia[origem][destino] = 0
        self.matriz_adjacencia[destino][origem] = 0  # Para grafos não direcionados

    def exibir_grafo(self):
        for linha in self.matriz_adjacencia:
            print(linha)

# Exemplo de uso
if __name__ == "__main__":
    grafo = GrafoMatriz(5)
    grafo.adicionar_aresta(0, 1)
    grafo.adicionar_aresta(0, 2, 3)
    grafo.adicionar_aresta(1, 3)
    grafo.exibir_grafo()