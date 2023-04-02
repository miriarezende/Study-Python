from random import choice
from time import sleep

jogador= input('vamos jogar Jokenpô!! \n Faça sua jogada: ').lower()
print('JO ')
sleep(1)
print('KEN')
sleep(1)
print('PO!!')
jokenpo= ['pedra', 'papel', 'tesoura']
jokenpo= choice(jokenpo)

if (jokenpo=='pedra' and jogador=='papel')or (jokenpo=='tesoura' and jogador=='pedra') or (jokenpo=='papel' and jogador=='tesoura'):
    print('voce: {}\ncomputador: {} \nvocê VENCEU!!'.format(jogador, jokenpo))
elif (jogador=='pedra' and jokenpo=='papel')or (jogador=='tesoura' and jokenpo=='pedra') or (jogador=='papel' and jokenpo=='tesoura'):
    print('voce: {}\ncomputador: {} \nvocê PERDEU!!'.format(jogador, jokenpo))
elif jogador==jokenpo:
    print('voce: {}\ncomputador: {} \nEMPATAMOS'.format(jogador, jokenpo))
else:
    print('jogada invalida')