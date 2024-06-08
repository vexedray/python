# Biblioteca

import math

# Tela

while True:
    
    print("\n***CALCULADORA***")
    print("\n1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("5 - Potência")
    print("6 - Seno")
    print("7 - Cosseno")
    print("8 - Raiz")
    print("9 - Percentual")
    print("10 - Fatorial")
    print("11- Sair")
    operacao =  int (input("\nDigite o número da operação desejada: "))

# Operadores

    if operacao == 1:
        numero1 = float (input("Digite o primeiro número: "))
        numero2 = float (input("Digite o segundo número: "))
        resultado = numero1 + numero2
        print("O resultado é: ", resultado)

    if operacao == 2:
        numero1 = float (input("Digite o primeiro número: "))
        numero2 = float (input("Digite o segundo número: "))
        resultado = numero1 - numero2
        print("O resultado é: ", resultado)

    if operacao == 3:
        numero1 = float (input("Digite o primeiro número: "))
        numero2 = float (input("Digite o segundo número: "))
        resultado = numero1 * numero2
        print("O resultado é: ", resultado)

    if operacao == 4:
        numero1 = float (input("Digite o primeiro número: "))
        numero2 = float (input("Digite o segundo número: "))
        resultado = numero1 / numero2
        print("O resultado é: ", resultado)
	
    if operacao == 5:
        numero1 = input("Digite o número: ")
        numero2 = input("Digite a potência: ")
        resultado = numero1 ** numero2
        print("O resultado é: ", resultado)

    if operacao == 6:
        ang = int (input("Digite o ângulo: "))
        rad = math.radians(ang)
        resultado = round(math.sin(rad), 3)

    if operacao == 7:
        ang = int (input("Digite o ângulo: "))
        rad = math.radians(ang)
        resultado = round(math.con(rad), 3)
        print("O resultado é: ", resultado)

    if operacao == 9:
        parte = float(input("Digite a parte: "))
        total = float(input("Digite o total: "))
        resultado =  (parte / total) * 100
        print("O resultado é: ", resultado)

    if operacao == 10:
        numero = int(input("Digite um número inteiro: "))
        if numero < 0:
            print("Erro: Fatorial de número negativo não é permitido.")
        resultado = math.factorial(numero)
        print("O resultado é: ", resultado) 

    if operacao == 11:
        print("Encerrando a calculadora...")
        break