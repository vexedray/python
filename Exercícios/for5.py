# VERIFICA QUANTIDADE DE MAIORIDADES DENTRO DE UMA ESTRUTURA DE REPETIÇÃO

# VÁRIAVEIS

total = 0

# OPERADORES

for a in range (1, 6):
  ano = int (input ("Digite o ano do nascimento da pessoa {} : ".format(a)))
  if ano <= 2006:
    print ("É de maior")
    total = total + 1
  else:
    print ("Não é de maior")
print("Exite {} pessoas maiores de idade".format(total))