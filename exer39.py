n1= float(input('nota 1: '))
n2= float(input('nota 2: '))
media= (n1+n2)/2
if media<5 and media>=0:
    print('REPROVADO')
elif media>=5 and media<=6.9:
    print('RECUPERAÇÃO')
elif media>=7 and media<=10:
    print('APROVADO')
else:
    print('nota invalida')