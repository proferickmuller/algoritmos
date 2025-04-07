def fibonacci_dinamico(n, memo={}):
    """
    Calcula o n-ésimo número de Fibonacci usando programação dinâmica (memoization).

    Args:
        n (int): O índice do número de Fibonacci a ser calculado.
        memo (dict): Um dicionário para armazenar os resultados já calculados.

    Returns:
        int: O n-ésimo número de Fibonacci.
    """
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci_dinamico(n - 1, memo) + fibonacci_dinamico(n - 2, memo)
    return memo[n]