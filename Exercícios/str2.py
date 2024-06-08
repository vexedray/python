# Variaveis

name = str (input("Digite um nome: "))

separar = name.split()

qtd = len(separar)
last = qtd - 1

print("Nome: ", name)
print("Primeiro nome: ", separar[0])
print("Último nome: ", separar[last])
