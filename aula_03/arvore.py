import random
from typing import List, Self

numeros_usados = set()
while len(numeros_usados) < 7:
    num = random.randint(1, 5000)
    if num not in numeros_usados:
        numeros_usados.add(num)


class TreeNode:
    def __init__(
        self,
        valor: int,
    ):
        self.valor = valor
        self.dependentes: list[Self] = []

    def dependentes(self):
        return self.dependentes

    def add_dependente(self, s: Self):
        if len(self.dependentes) >= 2:
            raise Exception("Apenas dois itens.")
        self.dependentes.append(s)

    def listagem_em_profundidade(self) -> List[int]:
        """Returns values in depth-first order (pre-order)"""
        result = [self.valor]
        for dependente in self.dependentes:
            result.extend(dependente.listagem_em_profundidade())
        return result

    def listagem_em_largura(self) -> List[int]:
        """Returns values in breadth-first order"""
        result = []
        fila = [self]
        while fila:
            atual = fila.pop(0)
            result.append(atual.valor)
            fila.extend(atual.dependentes)
        return result

    def __str__(self):
        to_return = f"Root: {self.valor}\n"        
        if self.dependentes:            
            for s in self.dependentes:
                to_return += "\t Dependente: " + str(s.valor) + "\n"
        return to_return + "\n"

class Tree:
    root: TreeNode = None

    def __init__(self, root: TreeNode):
        self.root = root

    def listagem_em_profundidade(self) -> List[int]:
        """Depth-first traversal starting from root"""
        return self.root.listagem_em_profundidade()

    def listagem_em_largura(self) -> List[int]:
        """Breadth-first traversal starting from root"""
        return self.root.listagem_em_largura()

    def busca_em_profundidade(self, valor: int) -> TreeNode | None:
        """Searches for a value in the tree in depth-first order"""
        pilha = [self.root]
        operacoes = 0
        while pilha:
            atual = pilha.pop()
            operacoes += 1
            if atual.valor == valor:
                print(f"Quantidade de operações: {operacoes}")
                return atual
            pilha.extend(reversed(atual.dependentes))
        return None

    def busca(self, valor: int) -> TreeNode | None:
        """Searches for a value in the tree"""
        fila = [self.root]
        operacoes = 0
        while fila:
            atual = fila.pop(0)
            operacoes += 1
            if atual.valor == valor:
                print(f"Quantidade de operações: {operacoes}")
                return atual
            fila.extend(atual.dependentes)

        print(f"Quantidade de operações, com o item não encontrado: {operacoes}")
        return None

    def balancear(self):
        """Balanceia a árvore"""
        self.root = self.balancear_node(self.root)

    def balancear_node(self, node: TreeNode) -> TreeNode:
        """Balanceia um node"""
        if not node:
            return node

        # ordenar a lista de dependentes
        node.dependentes.sort(key=lambda x: x.valor)

        # encontrar o meio da lista de dependentes
        meio = len(node.dependentes) // 2

        # criar um novo node para o meio
        novo_meio = TreeNode(node.dependentes[meio].valor)

        # criar a sub-arvore esquerda
        esquerda = self.balancear_node(TreeNode("esquerda"))
        for i in range(meio):
            esquerda.add_dependente(node.dependentes[i])

        # criar a sub-arvore direita
        direita = self.balancear_node(TreeNode("direita"))
        for i in range(meio + 1, len(node.dependentes)):
            direita.add_dependente(node.dependentes[i])

        # criar a arvore balanceada
        novo_meio.add_dependente(esquerda)
        novo_meio.add_dependente(direita)

        return novo_meio

    def __str__(self):
        return "inicio da árvore - " + str(self.root) + "\n"


def preencher_arvore_2(lista: list[int], root_node: TreeNode):        
    for _ in range(2):
        if len(lista) == 0:
            break
        node = TreeNode(lista.pop())
        root_node.add_dependente(node)
    
    if len(root_node.dependentes) > 0 and len(root_node.dependentes) < 2: 
        for d in root_node.dependentes:
            preencher_arvore_2(lista, d)
   
    print(root_node)
    return root_node

def show_lista(arvore: TreeNode, is_root = False):
    if is_root: 
        print("raiz: {}".format(arvore.valor))
    pad_str = ""
    if len(arvore.dependentes) > 0:
        if not is_root:
            pad_str = '\t'
        for d in arvore.dependentes:                        
            print("{}\tdependente: {}".format(pad_str ,d.valor))
            show_lista(d)

lista = list(numeros_usados)
n = TreeNode(999999999)
lista_base = preencher_arvore_2(
    lista=lista,    
    root_node=n
)

# print(lista[0:2])

show_lista(lista_base, True)


# print(t)
#
# t.balancear()
#
# print(t)
#
# print("Depth-first traversal:", t.listagem_em_profundidade())
# print("Breadth-first traversal:", t.listagem_em_largura())
#
# print("Search:", t.busca("filha de inicial"))
