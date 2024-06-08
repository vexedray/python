# FUNÇÃO QUE CALCULA IMPOSTO DE PRODUTO

# OPERADORES

def calcula_imposto (custo, taxa):
    soma = (taxa / 100) * custo
    venda = custo + soma
    return venda

# VÁRIAVEIS

valor = int (input("Quanto é o produto: "))
mais = float (input("Quanto é a taxa: "))

# CHAMADA DE FUNÇÃO

print(calcula_imposto(valor, mais))