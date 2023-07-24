from main import calcular_faturamento
import pytest

@pytest.mark.faturamento
# faturamento
def test_calcular_faturamento():
    assert type(calcular_faturamento()) == int