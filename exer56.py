from random import randint
pc= randint(0,10)
player=int(input('de 0 a 10, em que numero estou pensando? '))
tentativa=1
while player!=pc:
    print('ERROU!!\n Tente outra vez...de 0 a 10, em que numero estou pensando? ')
    player=int(input())
    tentativa+=1
print('Acertou!!!\n com total de {} tentativas'.format(tentativa))
#OU
""" from random import randint
pc= randint(0,10)
print('em que numero estou pensando entre 0 e 10? ')
acertou=False
palpite=0
while not acertou:
    player=int(input('dê seu palpite: '))
    palpite+=1
    if player==pc:
        acertou=True
print('acertou com {} tentativas'.format(palpite)) """