# Verificar maior que o terceiro número

# Váriaveis
valor = float (input ("Digite o valor do imóvel: "))
salario = float (input ("Digite seu sálario: "))
meses = int (input ("Digite a quantidade de meses a pagar: "))
valor_prestacao = valor / meses
validacao_salario = salario * 0.30
# Operadores

if valor_prestacao < validacao_salario:
    print ("Valor da mensalidade fica igual à: ", valor_prestacao)
else:
    print ("Você não podera pagar pois a parcela passa de trinta porcento do seu sálario")