class DisjointSetUnion:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [0] * size

    def encontrar(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.encontrar(self.parent[x])  # Path compression
        return self.parent[x]

    def unir(self, x, y):
        root_x = self.encontrar(x)
        root_y = self.encontrar(y)

        if root_x != root_y:
            if self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
            elif self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
            else:
                self.parent[root_y] = root_x
                self.rank[root_x] += 1

    def is_conectado(self, x, y):
        return self.encontrar(x) == self.encontrar(y)
    
       
dsu = DisjointSetUnion(10)

# Perform some unions
dsu.unir(1, 2)
dsu.unir(2, 3)
dsu.unir(4, 5)
dsu.unir(6, 7)
dsu.unir(5, 6)

# Check if elements are connected
print(dsu.is_conectado(1, 3))
print(dsu.is_conectado(4, 7))
print(dsu.is_conectado(0, 9))

# Find the root of an element
print(dsu.encontrar(3))  
print(dsu.encontrar(7))  
