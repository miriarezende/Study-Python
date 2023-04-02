from random import randint
jogo=[]
palpites=[]
n=int(input('quantos jogos deseja fazer? '))
for c in range(0,n):
    for i in range(0,6):
        sorteado=randint(1,60)
        palpites.append(sorteado)
    jogo.append(palpites[:])
    palpites.clear()
for c in range(0, n):
    print(f'palpite para o {c+1}° jogo: {jogo[c]}')