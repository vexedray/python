# CONTA VOGAIS E ESPAÇOS DE UMA FRASE

# OPERADORES

def contar(ocorrencia):
    espaco = ocorrencia.count(" ")
    vogais = ["a", "e", "i", "o", "u"]
    cont = 0
    for vogal in vogais:
        v = ocorrencia.count(vogal)
        cont = cont + v
    return print("O tanto de espaços foram:", espaco, "\nO tanto de vogais foram: ", cont)

# VÁRIAVEIS

frase = input("Digite uma frase: ")

# RESULTADO

contar(frase)
