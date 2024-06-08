# Verificar triângulo

# Váriaveis

n1 = float (input ("Digite o primeiro número: "))
n2 = float (input ("Digite o segundo número: "))
n3 = float (input ("Digite o terceiro número: "))

# Operadores

if (n1 + n2) > n3 and (n1 + n3) > n2 and (n3 + n2) > n1:
    print ("É triângulo")
    if n1 == n2 == n3:
        print ("É equilatero")
    else:
        if n1 == n2 or n1 == n3 or n2 == n3:
            print ("É isósceles")
        else:
            if n1 != n2 != n3:
                print("É escaleno")
else:
    print ("Não é triângulo")