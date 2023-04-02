nome=input('informe um nome: ')
bm= ('Bom dia, {}!!'.format(nome))
if nome == 'gustavo':
    print('vc tem um belo nome, gustavo\n', bm)
elif nome == 'ana' or nome == 'maria' or nome == 'joão':
    print('vc tem um nome popular no brasil\n',bm)
elif nome in 'Ana Claudia Jessica Joana':
    print('belo nome\n',bm)
else:
    print(bm)