def multiplicar_enormes(x, y):    
    x_str = str(x)
    y_str = str(y)
    n = len(x_str)
    m = len(y_str)
    
    # Usando uma lista para armazenar o resultado
    produto = [0] * (n + m)

    for i in range(n - 1, -1, -1):
        carregado = 0
        for j in range(m - 1, -1, -1):
            produto[i + j + 1] += int(x_str[i]) * int(y_str[j]) + carregado
            carregado = produto[i + j + 1] // 10
            produto[i + j + 1] %= 10
        produto[i] += carregado

    resultado = "".join(map(str, produto))
    
    # Remove leading zeros
    pos_primeiro_digito = 0
    while pos_primeiro_digito < len(resultado) - 1 and resultado[pos_primeiro_digito] == '0':
        pos_primeiro_digito += 1
    
    return resultado[pos_primeiro_digito:]


print(multiplicar_enormes(10, 20))
print(multiplicar_enormes(123456789, 987654321))