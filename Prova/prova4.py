# Verificar aposentadoria

# Váriaveis

idade = int (input ("Insira sua idade: "))
tempo = int (input ("Digite quantos anos você já trabalhou: "))

# Operadores

if (idade > 65) or (tempo >= 30):
    print ("Está apto a se aposentar")
else:
    if (idade >= 60 and tempo >= 25):
        print ("Está apto a se aposentar")
    else:
        print ("Não está apto a se aposentar")