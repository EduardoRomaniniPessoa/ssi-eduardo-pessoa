idade = int(input('Informe a idade de seu nadador!: '))
if idade >= 5 and idade <= 7:
    print('Seu nadador permanece na classificação Infantil A!')
elif idade >= 8 and idade <= 11:
    print('Seu nadador permanece na classificação Infantil B!')
elif idade >= 12 and idade <= 13:
    print('Seu nadador permanece na classificação Juvenil A!')
elif idade >= 14 and idade <= 17:
    print('Seu nadador permanece na classficação Juvenil B!')
elif idade >= 18:
    print('Seu nadador permanece na classificação Adulto!')
else:
    print('Seu nadador ainda não tem idade válida! ')