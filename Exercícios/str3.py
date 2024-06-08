# Variaveis

n = str (input("Digite um número até 9999: "))

qtd = len(n)
if qtd <= 4:
    un = n[0]
    dz = n[1]
    c = n[2]
    mil = n[3]
    print("Unidade: ", un)
    print("Dezena: ", dz)
    print("Centena: ", c)
    print("Milhar: ", mil)
else:
    print("Não pode ser maior que 9999")


