"""
desafio: Dado um array (ou lista) de números inteiros nums, determine se algum valor aparece pelo menos duas vezes no array. Retorne True se qualquer valor aparecer duas ou mais vezes, e False se todos os elementos forem distintos.
"""

from typing import List


# usando força bruta
def tem_duplicadas(nums: List[int]) -> bool:
    """
    Verifica se há duplicatas usando força bruta (comparações par a par).
    """
    n = len(nums)
    if n < 2:
        return False

    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] == nums[j]:
                return True
    
    return False
