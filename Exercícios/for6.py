# VERIFICA SE EXISTE NÚMERO PRIMO EM UMA ESTRUTURA DE REPETIÇÃO

# VÁRIAVEIS

numero  = int (input("Digite um número: "))
total = 0

# OPERADORES

for a in range (1, numero+1):
  if numero % a == 0:
    total = total + 1

if total == 2:
      print ("É primo")
else:
    if total > 2:
      print ("Não é primo")