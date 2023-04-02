campeonato= {}
gols=[]
total=0
campeonato['nome']=input('nome: ')
partidas=int(input(f'quantas partidas {campeonato["nome"]} jogou? '))
for c in range(0, partidas):
    n=int(input(f'quantos gols na partida {c}: '))
    gols.append(n)
    total+=n
campeonato['gols']=gols
campeonato['total']=total
print(campeonato)
for k, v in campeonato.items():
    print(f'{k} tem valor {v}')
print(f'o jogador {campeonato["nome"]} jogou {partidas} partidas')
for c in range(0, partidas):
    print(f'na partida {c+1}, fez {gols[c]} gols')
print(f'total foi de {total} gols')