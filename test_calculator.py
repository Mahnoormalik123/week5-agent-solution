from src.utils_calc import calculate

def test_calc():
    assert calculate("2+3") == 5
    assert calculate("10/2") == 5
