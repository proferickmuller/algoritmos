
def lcs(X, Y):
    '''
    Função: lcs(X, Y)

    Descrição:
    A função `lcs` encontra a subsequência comum mais longa (LCS - Longest Common Subsequence) entre duas strings, X e Y. 
    Uma subsequência é uma sequência que aparece na mesma ordem em ambas as strings, mas não necessariamente de forma contínua. 
    Por exemplo, para as strings "AGGTAB" e "GXTXAYB", a LCS é "GTAB".

    O algoritmo utiliza uma técnica chamada programação dinâmica, que resolve problemas complexos dividindo-os em subproblemas menores e armazenando os resultados intermediários para evitar cálculos repetidos.

    Parâmetros:
    - X (str): A primeira string.
    - Y (str): A segunda string.

    Retorno:
    - str: A subsequência comum mais longa entre X e Y.

    Como funciona o algoritmo:
    1. **Criação de uma tabela (matriz):**
        - O algoritmo cria uma tabela chamada `dp` com dimensões (m+1) x (n+1), onde `m` é o tamanho de X e `n` é o tamanho de Y.
        - Cada célula da tabela armazena o comprimento da LCS para os prefixos das strings X e Y até aquele ponto.

    2. **Preenchimento da tabela:**
        - A tabela é preenchida linha por linha, comparando os caracteres de X e Y.
        - Se os caracteres forem iguais, o valor da célula atual é incrementado em relação ao valor da célula diagonal anterior.
        - Se os caracteres forem diferentes, o valor da célula atual é o maior valor entre a célula acima ou à esquerda.

    3. **Reconstrução da LCS:**
        - Após preencher a tabela, o algoritmo reconstrói a LCS percorrendo a tabela de trás para frente.
        - Sempre que encontra caracteres iguais, eles são adicionados à LCS.
        - O resultado final é invertido, pois a LCS é construída de trás para frente.

    Exemplo:
    Para as strings X = "AGGTAB" e Y = "GXTXAYB":
    - A tabela `dp` é preenchida com os comprimentos das subsequências comuns.
    - A LCS é reconstruída como "GTAB".

    Vantagens:
    - O uso de programação dinâmica torna o algoritmo eficiente, evitando cálculos redundantes.
    - A solução é clara e sistemática, adequada para problemas de subsequências.

    Limitações:
    - O algoritmo consome memória proporcional ao tamanho das strings, o que pode ser um problema para strings muito grandes.
    '''

    """
    Função para encontrar a subsequência comum mais longa (LCS) entre duas strings X e Y.
    Utiliza programação dinâmica para resolver o problema.
    """
    m = len(X)
    n = len(Y)

    # Criar uma matriz (tabela) para armazenar os resultados parciais
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Preencher a tabela dp
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:  # Se os caracteres forem iguais
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:  # Caso contrário, pegar o maior valor entre as opções
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # Reconstruir a LCS a partir da tabela dp
    lcs_result = []
    i, j = m, n
    while i > 0 and j > 0:
        if X[i - 1] == Y[j - 1]:  # Se os caracteres forem iguais, fazem parte da LCS
            lcs_result.append(X[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:  # Mover para a direção com maior valor
            i -= 1
        else:
            j -= 1

    # A LCS foi construída de trás para frente, então invertemos
    lcs_result.reverse()
    return ''.join(lcs_result)


# Exemplo de uso
if __name__ == "__main__":
    X = "AGGTAB"
    Y = "GXTXAYB"
    print("A subsequência comum mais longa é:", lcs(X, Y))