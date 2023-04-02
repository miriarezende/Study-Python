""" colocacao= ('Palmeiras', 'Internacional', 'Fluminense', 'Corinthians', 'Flamengo', 'Athletico-PR', 'Atlético-MG', 'Fortaleza', 'São Paulo', 'América-MG', 'Botafogo', 'Santos', 'Goiás', 'Bragantino', 'Coritiba', 'Cuiabá', 'Ceará', 'Atletico-GO', 'Avaí', 'Juventude')
print('primeiros colocados:')
pos=0
for c in range(0, 5):
    pos+=1
    print(f'{pos}° {colocacao[c]}')
print('\nultimos colocados: ')
decre=0
pos=len(colocacao)
for c in range(0,4):
    decre-=1
    print(f'{pos}° {colocacao[decre]}')
    pos-=1
print(f'\n lista em ordem alfabetica: {sorted(colocacao)}')
for c in range(0, len(colocacao)):
    if colocacao[c] == 'Santos':
        print(f'\n {colocacao[c]} esta na {c+1}° posição ') """
#OU
colocacao= ('Palmeiras', 'Internacional', 'Fluminense', 'Corinthians', 'Flamengo', 'Athletico-PR', 'Atlético-MG', 'Fortaleza', 'São Paulo', 'América-MG', 'Botafogo', 'Santos', 'Goiás', 'Bragantino', 'Coritiba', 'Cuiabá', 'Ceará', 'Atletico-GO', 'Avaí', 'Juventude')
print(f'primeiros colocados:{colocacao[0:5]}')
print(f'\nultimos colocados: {colocacao[-4:]}')
print(f'\nlista em ordem alfabetica: {sorted(colocacao)}')
print(f'\nSantos esta na {colocacao.index("Santos")+1}° posição ')