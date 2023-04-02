total= maisd= maisb=0
while True:
    nome= input('nome do produto: ')
    preço= float(input('preço:'))
    total+=preço
    if preço>1000:
        maisd+=1
    if maisb==0 or maisb>preço:
        maisb=preço
        nomebarato=nome
    resp= ' '
    while resp not in 'SN':
        resp= input('''
        [S] sim
        [N] não
        deseja continuar? ''').upper()
    if resp=='N':
        break
print(f'produto mais barato é {nomebarato}, custando R${maisb}\n{maisd} acima de R$1000\ntotal= {total:.2f}')