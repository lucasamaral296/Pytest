from main import calcular_lucro, calcular_faturamento
import pytest

def test_calcular_lucro():
    faturamento = calcular_faturamento()
    assert calcular_lucro(faturamento, 500) > 0
    
# faturamento
@pytest.mark.faturamento
def test_calcular_faturamento():
    assert calcular_faturamento() > 0




# F -> Falha
# E -> Exceção/ Erro
# . -> Tudo certo

# pytest -v   DÁ MAIS INFORMAÇÕES DO TESTE
# pytest arquivo.py testa apenas o arquivo 


# marcadores, categoriza os testes. no terminal usar pytest -m nomedomarcador 
