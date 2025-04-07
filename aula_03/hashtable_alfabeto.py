class HashTableAlfabeto: 
    """ Implementação de uma tabela hash que armazena palavras em listas. """

    def __init__(self):
        self.itens = []

    def inserir(self, palavra):
        primeira_letra = palavra[0].lower()
        
        letras = [i[0] for i in self.itens]
        
        if primeira_letra not in letras:
            self.itens.append([primeira_letra,[]])
            self.itens.sort()
        for letra, lista in self.itens:
            if letra == primeira_letra:
                lista.append(palavra)
                lista = list(set(lista))  # Remove duplicatas
                lista.sort()
                return
        

    def obter(self, p_letra):
        p_letra = p_letra.lower()
        for letra, lista in self.itens:
            if letra == p_letra:
                return lista
        

    def __str__(self):
        return str(self.itens)
    


ht = HashTableAlfabeto()
ht.inserir("banana")
ht.inserir("abacaxi")
ht.inserir("abacate")
ht.inserir("uva")

print(ht.obter("a"))  # Deve retornar ['abacate', 'abacaxi']
print(ht.obter("b"))  # Deve retornar ['banana']
print(ht.obter("u"))  # Deve retornar ['uva']