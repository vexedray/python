# Variaveis

name = str (input("Digite o nome completo: "))

# Operadores

name_up = name.upper()
name_lower = name.lower()
spc = name.count(" ")
letras = len(name) - spc
one = name.split()
qtd = len(one[0])



print ("SEU NOME MAIUSCULO: ", name_up)
print ("seu nome minusculo: ", name_lower)
print ("Quantidade de letras: ", letras)
print ("Quantidade do primeiro nome: ", qtd)