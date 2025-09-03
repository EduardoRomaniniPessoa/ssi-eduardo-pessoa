valorCompra = float(input('Digite o valor de sua compra: '))
tempo = int(input('Informe quantos meses de prestações sua compra terá: '))
prestacoes = valorCompra/tempo

print (f'Sua compra, com o valor de R${valorCompra}, terá prestações de {prestacoes} pelo período de {tempo} meses!')