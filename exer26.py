from random import randint
from time import sleep
n1= randint(0,5+1)
rp= int(input('tente descobrir o numero sorteado entre 0 e 5: '))
print('processando...')
sleep(2)
print('era {}'.format(n1))
if n1==rp:
    print('venceu')
else:
    print('perdeu')