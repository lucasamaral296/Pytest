# Sistema Gerencial

# Calculra Faturamento
def calcular_faturamento():
    vendas = [100, 200, 300, 400, 500]
    faturamento = sum(vendas)
    return faturamento

# Calcular Custo
def calcular_custo(cotacao_dolar):
    custo = 1000 * cotacao_dolar
    return custo

# Calcular Lucro

def calcular_lucro(faturamento, custo):
    lucro = faturamento - custo
    return lucro

