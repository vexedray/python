# FUNÇÃO QUE VERIFICA SE EXISTE UM SOBRENOME EM UMA STRING

# VÁRIAVEIS

n = str (input("Digite um nome completo: "))

# OPERADORES

if n.find("Silva") > 0:
    print("Tem Silva")
else:
    print("Não tem Silva")