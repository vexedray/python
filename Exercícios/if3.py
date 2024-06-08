# DA MULTA COM CONDIÇÃO DE VELOCIDADE

# VÁRIAVEIS

km = int (input ("Digite a velocidade: "))

# OPERADORES

if km > 100:
    valor = km - 100
    multa = valor * 8
    print("Você excedeu o limite de velocidade, e sua multa é de: ", multa)
else: 
    print("OK")