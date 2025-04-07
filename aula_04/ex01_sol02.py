"""
desafio: Dado um array (ou lista) de números inteiros nums, determine se algum valor aparece pelo menos duas vezes no array. Retorne True se qualquer valor aparecer duas ou mais vezes, e False se todos os elementos forem distintos.
"""

from typing import List


def tem_duplicadas(nums: List[int]) -> bool:
    """
    Verifica se há duplicatas ordenando o array primeiro.
    """
    n = len(nums)
    if n < 2:
        return False

    nums.sort()

    for i in range(n - 1):
        if nums[i] == nums[i+1]:
            return True
            
    return False
