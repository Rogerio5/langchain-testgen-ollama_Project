import pytest
from src.divisao import divisao

def test_divisao_basica():
    assert divisao(10, 2) == 5
    assert divisao(9, 3) == 3
    assert divisao(-6, 2) == -3

def test_divisao_com_float():
    assert divisao(5.0, 2.0) == 2.5
    assert divisao(1, 4) == 0.25

def test_divisao_por_zero():
    with pytest.raises(ValueError):
        divisao(5, 0)
