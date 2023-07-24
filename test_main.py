from main import calcular_lucro, calcular_faturamento

def test_calcular_lucro():
    faturamento = calcular_faturamento()
    assert calcular_lucro(faturamento, 500) > 0
    
    





# F -> Falha
# E -> Exceção/ Erro
# . -> Tudo certo

