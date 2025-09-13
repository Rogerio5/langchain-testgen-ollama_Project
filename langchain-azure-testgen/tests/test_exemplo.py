import pytest

  # importa a função do seu módulo
from src.exemplo import dias_entre_datas




def test_dias_entre_datas():
    assert dias_entre_datas("2022-01-01", "2022-01-02") == 1
    assert dias_entre_datas("2022-01-02", "2022-01-01") == 1
    assert dias_entre_datas("2022-01-05", "2022-01-02") == 3
    assert dias_entre_datas("2022-12-31", "2023-01-01") == 1
    assert dias_entre_datas("2022-09-30", "2022-10-01") == 1
    assert dias_entre_datas("2022-06-30", "2022-07-01") == 1
    assert dias_entre_datas("2022-05-31", "2022-06-01") == 1

def test_data_invalida():
    with pytest.raises(ValueError):
        dias_entre_datas("2022-02-29", "2022-03-01")  # 2022 não é bissexto
