# VERIFICA A MÉDIA DE IDADE EM UMA ESTRUTURA DE REPETIÇÃO

# VÁRIAVEIS

total = 0
soma = 0

# OPERADORES

for a in range (1, 6):
  idade = int (input("Digite a idade {} : ".format(a)))
  total = total + 1
  soma = soma + idade
divisao = soma / total

# RESULTADOS

print ('A média ficou: ', divisao)