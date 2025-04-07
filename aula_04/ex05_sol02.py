def selecionar_atividades(atividades):
    """
    Seleciona o número máximo de atividades que podem ser realizadas sem sobreposição.
    
    Args:
        atividades: Lista de tuplas (inicio, fim) representando os horários de início e fim de cada atividade.
    
    Returns:
        Lista de tuplas das atividades selecionadas.
    """
    # Ordenar as atividades pelo horário de término
    atividades_ordenadas = sorted(atividades, key=lambda x: x[1])
    
    atividades_selecionadas = []
    
    # Selecionar a primeira atividade (a que termina mais cedo)
    if atividades_ordenadas:
        atividades_selecionadas.append(atividades_ordenadas[0])
    
    # Para cada atividade restante
    for i in range(1, len(atividades_ordenadas)):
        # Obtém o horário de início da atividade atual
        inicio_atual = atividades_ordenadas[i][0]
        
        # Obtém o horário de término da última atividade selecionada
        fim_ultima = atividades_selecionadas[-1][1]
        
        # Se a atividade atual começar após o término da última atividade selecionada
        if inicio_atual >= fim_ultima:
            # Adicionar a atividade atual à lista de atividades selecionadas
            atividades_selecionadas.append(atividades_ordenadas[i])
    
    return atividades_selecionadas


def main():
    # Exemplo de atividades: (horário de início, horário de término)
    atividades = [(1, 4), (3, 5), (0, 6), (5, 7), (3, 9), (5, 9), (6, 10), (8, 11), (8, 12), (2, 14), (12, 16)]
    
    resultado = selecionar_atividades(atividades)
    
    print("Atividades selecionadas:")
    for inicio, fim in resultado:
        print(f"Início: {inicio}, Fim: {fim}")
    print(f"Total de atividades: {len(resultado)}")


if __name__ == "__main__":
    main()