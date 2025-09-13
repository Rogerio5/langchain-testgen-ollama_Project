import pytest
from src.soma import soma

def test_soma_basico():
    assert soma(2, 3) == 5
    assert soma(-1, 1) == 0
    assert soma(0, 0) == 0
    assert soma(-5, -5) == -10

def test_soma_com_float():
    assert soma(2.5, 3.5) == 6.0
    assert soma(-1.1, 1.1) == 0.0
