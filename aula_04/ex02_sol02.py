cache_resultados = {}

def multiplicar_enormes(x, y):

    if (x, y) in cache_resultados:
        return cache_resultados[(x, y)]    # se ja existir no cache, retorna o resultado sem fazer o calculo

    """
    Multiplica dois números grandes usando uma abordagem de divisão e conquista (algoritmo de Karatsuba).
    
    Args:
        x: O primeiro número (inteiro).
        y: O segundo número (inteiro).

    Retorna:
        int: O produto de x e y (como um inteiro).        
    """

    # Convert numbers to strings for easier digit manipulation
    x_str = str(x)
    y_str = str(y)

    n = max(len(x_str), len(y_str))

    # Base case: If numbers are small enough, just multiply directly
    if n <= 1:
        return x * y

    # Divide
    half_n = n // 2

    a = int(x_str[:-half_n] if len(x_str) > half_n else '0')
    b = int(x_str[-half_n:])
    c = int(y_str[:-half_n] if len(y_str) > half_n else '0')
    d = int(y_str[-half_n:])

    # Conquer (recursive calls)
    ac = multiplicar_enormes(a, c)
    bd = multiplicar_enormes(b, d)
    ad_plus_bc = multiplicar_enormes(a + b, c + d) - ac - bd

    # Combine
    resultado = ac * (10**(2 * half_n)) + ad_plus_bc * (10**half_n) + bd

    cache_resultados[(x, y)] = resultado
    
    return resultado

print(multiplicar_enormes(10, 20))
print(multiplicar_enormes(12345678901234567890, 98765432109876543210))