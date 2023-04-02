from datetime import date
anoatual= date.today().year
ano= int(input('ano de nascimento do atleta: '))
idade= anoatual-ano
if idade <= 9:
    print('MIRIN')
elif idade <= 14 :
    print('INFANTIL')
elif idade<=19:
    print('JUNIOR')
elif idade<=25:
    print('SENIOR')
else:
    print('MASTER')