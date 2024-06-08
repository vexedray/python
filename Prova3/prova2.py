# VERIFICA MÉDIA DE UM GRUPO DE 5 ALUNOS

# VÁRIAVEIS

n = []
prova = []

aluno = {"nome" : [] , "nota" : []}

# OPERADORES

for a in range (0,5):
    n.append(input("Insira seu nome: "))
    aluno["nome"] = n
    prova.append(float (input ("Digite sua nota: ")))
    aluno["nota"] = prova

soma = sum(prova)
media = soma / 5

# RESULTADO

print("Aluno:", aluno['nome'][0], "\nNota:", aluno['nota'][0])
print("Aluno:", aluno['nome'][1], "\nNota:", aluno['nota'][1])
print("Aluno:", aluno['nome'][2], "\nNota:", aluno['nota'][2])
print("Aluno:", aluno['nome'][3], "\nNota:", aluno['nota'][3])
print("Aluno:", aluno['nome'][4], "\nNota:", aluno['nota'][4])
print("A média geral é: ", media)