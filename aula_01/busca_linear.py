import util

lista_numeros = util.gera_lista_aleatoria(9_000_000,10_000_000)

numero_buscar = 1263

print("Iniciando busca...") 

posicao_atual = 0

encontrado = False

while not encontrado and (posicao_atual < len(lista_numeros)):
    
    if lista_numeros[posicao_atual] == numero_buscar:
        encontrado = True
    else: 
        posicao_atual += 1
        

print("Finalizado.")
if encontrado:
    print(f"Numero {numero_buscar} encontrado apos {posicao_atual} iteracoes")
else:
    print(f"Numero {numero_buscar} NAO encontrado apos {posicao_atual} iteracoes")
