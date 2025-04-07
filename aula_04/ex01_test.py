from ex01_sol01 import tem_duplicadas

"""
desafio: Dado um array (ou lista) de números inteiros nums, determine se algum valor aparece pelo menos duas vezes no array. Retorne True se qualquer valor aparecer duas ou mais vezes, e False se todos os elementos forem distintos.
"""

def testa_com_duplicadas(): 
    # arrange
    nums = [1, 2, 3, 1]
    expected = True

    # act
    returned = tem_duplicadas(nums)

    # assert
    assert expected == returned
    

def testa_com_poucos_itens():

    # arrange
    nums = [99]
    expected = False

    # act
    returned = tem_duplicadas(nums)

    # assert
    assert expected == returned


def testa_sem_duplicadas(): 
    # arrange
    nums = [1, 2, 3, 4]
    expected = False

    # act
    returned = tem_duplicadas(nums)

    # assert
    assert expected == returned
