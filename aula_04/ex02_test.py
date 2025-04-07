from ex02_sol02 import multiplicar_enormes


def test_multiplicar_enormes():    
    assert multiplicar_enormes(123456789, 987654321) == 121932631112635269
    assert multiplicar_enormes(0, 123456789) == 0
    assert multiplicar_enormes(123456789, 0) == 0
    assert multiplicar_enormes(123456789, 1) == 123456789
    assert multiplicar_enormes(1, 123456789) == 123456789
    assert multiplicar_enormes(123456789, 123456789) == 15241578750190521
    assert multiplicar_enormes(999999999, 999999999) == 999999998000000001
    assert multiplicar_enormes(12345678901234567890, 98765432109876543210) == 1219326311370217952237463801111263526900
    

def test_multiplicar_pequenos(): 
    assert multiplicar_enormes(10, 20) == 200    
    pass

