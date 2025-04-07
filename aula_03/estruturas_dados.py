# complexidade da lista desordenada = O(n)
a = [5, 1, 4, 2, 3]

# complexidade da lista ordenada = O(n log n)
# pois podemos usar bubble sort para ordenar e depois obter os dados.
a.sort()

# complexidade da pilha = O(n)
# só podemos tirar o primeiro ou o ultimo elemento
from collections import deque

d = deque(range(20))
d.append(100)
print(d)
d.appendleft(-10)
print(d)

i = d.pop()
print("tirei do final", i)
print(d)

i = d.popleft()
print("tirei do inicio", i)
print(d)

# complexidade da fila = O(n)
# ver o exemplo acima

# complexidade da hash table = O(1)
pedidos = {
    "14": ["pao", "leite", "queijo"],
    "15": ["pao", "salame", "queijo"],
    "16": ["pao", "queijo", "leite", "banana"],
    "17": ["queijo", "leite"],
}

# o acesso é direto!
print(pedidos["14"])

# complexidade da arvore = O(log n)
from bigtree import Node, find

# criar uma arvore
root = Node(1, valor="1")
a = Node(2, valor="2", parent=root)
b = Node(9, valor="9", parent=root)

c = Node(3, valor="3", parent=a)
d = Node(4, valor="4", parent=a)
e = Node(5, valor="5", parent=a)

f = Node(6, valor="6", parent=b)
g = Node(7, valor="7", parent=b)

root.show()

item = find(root, lambda node: node.valor == "7")
print(item)
# Para esta busca, precisou percorrer tres niveis.
