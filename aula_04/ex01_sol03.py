from typing import List


def tem_duplicadas(nums: List[int]) -> bool:
    """
    Verifica se há duplicatas usando um conjunto hash (set).
    """
    vistos = set()

    for numero in nums:
        if numero in vistos:
            return True
        vistos.add(numero)

    return False
