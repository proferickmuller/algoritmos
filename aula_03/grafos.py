class Grafo:
    def __init__(self):
        self.adjacencias = {}

    def adicionar_vertice(self, vertice):
        if vertice not in self.adjacencias:
            self.adjacencias[vertice] = []

    def adicionar_aresta(self, origem, destino):
        if origem not in self.adjacencias:
            self.adicionar_vertice(origem)
        if destino not in self.adjacencias:
            self.adicionar_vertice(destino)
        self.adjacencias[origem].append(destino)
        self.adjacencias[destino].append(origem)  # Para grafos não direcionados

    def mostrar_grafo(self):
        for vertice, vizinhos in self.adjacencias.items():
            print(f"{vertice}: {', '.join(map(str, vizinhos))}")

# Exemplo de uso
if __name__ == "__main__":
    grafo = Grafo()
    grafo.adicionar_vertice(1)
    grafo.adicionar_vertice(2)
    grafo.adicionar_aresta(1, 2)
    grafo.adicionar_aresta(1, 3)
    grafo.mostrar_grafo()