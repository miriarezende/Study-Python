""" pessoas= []
datas= []
pesada= []
leve= []
while True:
    datas.append(input('nome: '))
    datas.append(float(input('peso: ')))
    pessoas.append(datas[:])
    datas.clear()
    resp=input('deseja continuar? ').upper()
    while resp not in 'SN':
        resp=input('tente novamente, deseja continuar? ').upper()
    if resp=='N':
        break
for c in range (0, len(pessoas)):
        if pessoas[c][1] >= 90:
            pesada.append(pessoas[c][0])
        elif pessoas[c][1] <= 65:
            leve.append(pessoas[c][0])
print(f'{len(pessoas)} pessoas foram cadastradas' )
print(f'lista de pessoas mais pesadas: {pesada}')
print(f'lista de pessoas mais leves {leve}')  """
#OU
pessoas= []
datas= []
while True:
    datas.append(input('nome: '))
    datas.append(float(input('peso: ')))
    pessoas.append(datas[:])
    datas.clear()
    resp=input('deseja continuar? (S/N)').upper()
    while resp not in 'SN':
        resp=input('tente novamente, deseja continuar? ').upper()
    if resp=='N':
        break
print(f'foram cadastradas {len(pessoas)} pessoas')
for c in range (0, len(pessoas)):
    if c==0:
        print('pessoas mais pesadas:')
    if pessoas[c][1] >= 90:
        print(end=' 'f'{pessoas[c][0]}')
for c in range(0, len(pessoas)):
    if c==0:
        print('\npessoas mais leves:')
    if pessoas[c][1] <= 65:
        print(end=' ' f'{pessoas[c][0]}')
#OU
""" pessoas= []
datas= []
while True:
    datas.append(input('nome: '))
    datas.append(float(input('peso: ')))
    if len(pessoas)==0:
        maior= menor= datas[1]
    else:
        if maior<datas[1]:
            maior= datas[1]
        if menor>datas[1]:
            menor= datas[1]
    pessoas.append(datas[:])
    datas.clear()
    resp=input('deseja continuar? (S/N)').upper()
    while resp not in 'SN':
        resp=input('tente novamente, deseja continuar? ').upper()
    if resp=='N':
        break
print(f'foram cadastradas {len(pessoas)} pessoas')
print(f'maior peso foi {maior}kg. peso de ', end='')
for p in pessoas:
    if p[1]==maior:
        print(f'{p[0]}', end='')
print()
print(f'menor peso foi {menor}kg. peso de ', end='')
for p in pessoas:
    if p[1]==menor:
        print(f'{p[0]}', end='')
"""