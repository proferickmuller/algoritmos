import util

print("Gerando lista...") 

lista_atual = util.gera_lista_aleatoria(900_000,10_000_000)
lista_atual.sort()    # ordenando a lista automaticamente

numero_buscar = 212


print("Iniciando busca...") 

encontrado = False

iteracoes = 1
posicao_atual = len(lista_atual) - 1
posicao_inicial = 0
posicao_final = len(lista_atual) - 1

while not encontrado and posicao_atual > 1:       
   
    posicao_atual = len(lista_atual) // 2
    print(posicao_atual)


    if posicao_atual == 0:
        break
    
    if lista_atual[posicao_atual] == numero_buscar:
        encontrado = True
    else:
        if numero_buscar > lista_atual[posicao_atual]:
            lista_atual = lista_atual[posicao_atual:posicao_final+1]
        else:
            lista_atual = lista_atual[posicao_inicial:posicao_atual+1]
        
        iteracoes = iteracoes + 1

print("Finalizado.")
if encontrado:
    print(f"Numero {numero_buscar} encontrado apos {iteracoes} iteracoes")
else:
    print(f"Numero {numero_buscar} NAO encontrado apos {iteracoes} iteracoes")