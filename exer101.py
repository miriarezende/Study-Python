def ficha(nome='desconhecido', gols=0):
    return (f'jogador {nome} fez {gols} gol(s)')
    
nome=input('nome do jogador: ')
gols=input('numero de gols: ')
if gols.isnumeric():
    gols=int(gols)
else:
    gols=0
if nome.strip() == '':
    print(ficha(gols=gols))
else:
    print(ficha(nome, gols))