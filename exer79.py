lista= []
while True:
    lista.append(int(input('informe um valor: ')))
    resp=input('deseja continuar? ').upper()
    while resp not in 'SN':
        resp=input('deseja continuar? ').upper()
    if resp=='N':
        break
lista.sort(reverse=True)
print(f'{lista} \nforam informados {len(lista)} numeros.')
if 5 in lista:
    print('valor 5 encontrado')
else:
    print('valor 5 não encontrado')