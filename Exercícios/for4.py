# VERIFICA VOGAL EM UMA STRING COM LISTA

# VÁRIAVEIS

frase = (input("Digite uma frase: "))

# OPERADORES

vogais = ["a", "e", "i", "o", "u"]

ocorrencia = frase.count(" ")
ocorrencia2 = frase.count()

cont = 0 

for vogal in vogais:
    ocorrencia2 = frase.count(vogal)
    cont += 1

# RESULTADO

print("O tanto de espaços é: ", ocorrencia)
print("O tanto de vogais é: ", cont)