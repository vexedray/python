# VERIFICA QUAL MAIOR E MENOR DE UMA LISTA CRIADA EM FOR

# VÁRIAVEIS

menor = 0
maior = 0

# OPERADORES

for a in range (1,5):
  n = int (input ("Digite um número: "))
  if a == 1:
    maior = n
    menor = n
  else:
    if n > maior:
      maior = n
      if n < menor:
        menor = n

# RESULTADO

print ("O maior é", maior)
print ("O maior é", menor)