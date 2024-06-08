# AUMENTA O SÁLARIO COM UMA CONDIÇÃO

# VÁRIAVEIS

salario_atual = float(input('Informe o salário atual: '))

# OPERADORES

if salario_atual <= 1340:
    aumento = salario_atual * 15/100
else:
    aumento = salario_atual * 10/100

salario_novo = salario_atual + aumento

# RESULTADO

print('O novo salário e: {}'.format(salario_novo))

