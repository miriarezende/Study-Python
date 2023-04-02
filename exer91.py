""" lista=[]
mulher=[]
pessoas= {}
idade=0
while True:
    pessoas['nome']=input('nome: ')
    pessoas['sexo']=input('sexo (F/M) ').upper()[0]
    while pessoas['sexo'] not in 'FM':
        pessoas['sexo']=input('Invalido, sexo (F/M): ').upper()[0]
    pessoas['idade']=int(input('idade: '))
    lista.append(pessoas.copy())
    idade+=pessoas['idade']
    if pessoas['sexo'] == 'F':
        mulher.append(pessoas['nome'])
    resp=input('deseja continuar (S/N)? ').upper()[0]
    while resp not in 'NS':
        resp=input('Invalido, deseja continuar (S/N)? ').upper()[0]
    if resp=='N':
        break
media=idade/len(lista)
print(lista)
print(f'foram cadastradas {len(lista)} pessoas')
print(f'media das idades= {media:.2f}')
print('mulheres cadastradas: ')
for m in mulher:
    print(m)
print('pessoas acima da media: ')
for c in range (0, len(lista)):
    if media<=lista[c]['idade']:
        print(f'{lista[c]["nome"]}') """
#OU
lista=[]
pessoas= {}
idade=0
while True:
    pessoas.clear()
    pessoas['nome']=input('nome: ')
    while True:
        pessoas['sexo']=input('sexo (F/M): ').upper()[0]
        if pessoas['sexo'] in 'FM':
            break
        print('erro! digite apenas M ou F')
    pessoas['idade']=int(input('idade: '))
    lista.append(pessoas.copy())
    idade+=pessoas['idade']
    while True:
        resp=input('deseja continuar (S/N)? ').upper()[0]
        if resp in 'SN':
            break
        print('erro! digite apenas S ou N')
    if resp=='N':
        break
media=idade/len(lista)
print(f'foram cadastradas {len(lista)} pessoas')
print(f'media das idades= {media}')
print('mulheres cadastradas: ', end='')
for p in lista:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]} ', end='')
print()
print('pessoas acima da media: ')
for p in lista:
    if p['idade']>=media:
        print(' ', end='')
        for k,v in p.items():
            print(f'{k} = {v} ', end='')
        print()