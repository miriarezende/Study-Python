soma= div=0
continuar='S'
while continuar in 'Ss':
    n=int(input('informe um valor: '))
    soma+=n
    div+=1
    if div==1:
        maior= menor=n
    else:
        if maior<n:
            maior=n
        if menor>n:
            menor=n
    continuar=input('deseja informa mais valores:')
media=soma/div
print('media= {}\n maior= {}\n menor= {}'.format(media, maior, menor))