class GrafoListaAdjacencia:
    def __init__(self):
        self.grafo = {}

    def adicionar_vertice(self, vertice):
        if vertice not in self.grafo:
            self.grafo[vertice] = []

    def adicionar_aresta(self, vertice1, vertice2):
        if vertice1 in self.grafo and vertice2 in self.grafo:
            self.grafo[vertice1].append(vertice2)
            self.grafo[vertice2].append(vertice1)  # Para grafos não direcionados

    def remover_aresta(self, vertice1, vertice2):
        if vertice1 in self.grafo and vertice2 in self.grafo:
            if vertice2 in self.grafo[vertice1]:
                self.grafo[vertice1].remove(vertice2)
            if vertice1 in self.grafo[vertice2]:
                self.grafo[vertice2].remove(vertice1)

    def remover_vertice(self, vertice):
        if vertice in self.grafo:
            for adjacente in self.grafo[vertice]:
                self.grafo[adjacente].remove(vertice)
            del self.grafo[vertice]

    def exibir_grafo(self):
        for vertice, adjacentes in self.grafo.items():
            print(f"{vertice}: {adjacentes}")


# Exemplo de uso
if __name__ == "__main__":
    grafo = GrafoListaAdjacencia()
    grafo.adicionar_vertice("A")
    grafo.adicionar_vertice("B")
    grafo.adicionar_vertice("C")
    grafo.adicionar_aresta("A", "B")
    grafo.adicionar_aresta("A", "C")
    grafo.exibir_grafo()