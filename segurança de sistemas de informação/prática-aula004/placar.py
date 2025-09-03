golA = int(input('Informe os gols do primeiro time: '))
golB = int(input('Informe os gols do segundo time: '))
if golA == golB:
    print(f'O placar foi: {golA} X {golB} , ou seja, um Empate!')
elif golA >= golB:
    print(f'O placar foi: {golA} X {golB} , ou seja, Vitória do Primeiro Time!')
elif golA >= golB:
    print(f'O placar foi: {golA} X {golB} , ou seja, Vitória do Segundo Time! ')