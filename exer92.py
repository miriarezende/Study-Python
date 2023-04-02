aproveitammento=[]
campeonato= {}
gols=[]
while True:
    campeonato.clear()
    gols.clear()
    campeonato['nome']=input('nome: ')
    partidas=int(input(f'quantas partidas {campeonato["nome"]} jogou? '))
    for c in range(0, partidas):
        gols.append(int(input(f'quantos gols na partida {c}: ')))
    campeonato['gols']=gols[:]
    campeonato['total']=sum(gols)
    aproveitammento.append(campeonato.copy())
    resp=input('deseja continuar (S/N)? ').upper()
    while resp not in 'NS':
        resp=input('Invalido, deseja continuar (S/N)? ').upper()
    if resp=='N':
        break
print('cod ', end='')
for i in campeonato.keys():
    print(f'{i:<15}', end='')
print()
for k, v in enumerate(aproveitammento):
    print(f'{k:>2} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
while True:
    cod= int(input('mostrar dados de qual jogador? (999 para parar) '))
    if cod==999:
        break
    if cod>= len(aproveitammento):
        print(f'erro! nao exite jogador com codigo {cod}')
    else:
        print(f'levantamento do jogador {aproveitammento[cod]["nome"]}:')
        for i, v in enumerate(aproveitammento[cod]['gols']):
            print(f'no jogo {i+1} fez {v} gols.')
