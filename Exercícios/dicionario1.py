# VERIFICA APROVAÇÃO DE ALUNO COM DICIONÁRIO

# VÁRIAVEIS

nome = input("Digite seu nome: ")
media = float (input ("Digite a média do aluno: "))


aluno = {"nome" : nome , "média" : media, "passou?" : ""}

if media >= 7:
    aluno ["passou?"] = "sim"
else:
    aluno ["passou?"] = "não"

print(aluno)