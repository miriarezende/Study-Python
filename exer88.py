from random import randint
from operator import itemgetter
jogo={}
ranking=[]
jogo['jogador 1']=randint(1,6)
jogo['jogador 2']=randint(1,6)
jogo['jogador 3']=randint(1,6)
jogo['jogador 4']=randint(1,6)
print('valores sorteados: ')
for k, v in jogo.items():
    print(f'O {k} tirou {v}')
print('Ranking dos jogadores:')
ranking=sorted(jogo.items(), key=itemgetter(1), reverse=True)
for i,v in enumerate(ranking):
    print(f'{i+1}° lugar: {v[0]} com {v[1]}')