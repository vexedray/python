# 1 - Verificar idade

# Váriaveis

idade = int (input ("Insira a idade que deseja classificar: "))

# Operadores

if (idade == 0 or idade <= 11):
    print ("É criança")
else:
    if idade == 12 or idade <= 18:
        print ("É adolescente")
    else:
        if idade == 19 or idade <= 24:
            print ("É adulto")
        else:
            if idade == 41 or idade <= 60:
                print ("É meia idade")
            else:
                print ("É idoso")