# Calcular a média e verificar o resultado

nota1 = float(input('Informe a primeira nota: '))
nota2 = float(input('Informe a segunda nota: '))

media = (nota1 + nota2) / 2

# print('A sua média foi {:.1f}'.format(media))

print(f'A sua média foi {media:.1f}')
if media >= 6:
    print('Aprovado')
else:
    print('Exame final')