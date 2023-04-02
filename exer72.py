numeros= (int(input('informe um numero= ')), int(input('informe um numero= ')), int(input('informe um numero= ')), int(input('informe um numero= ')))
snove=0
print('numeros pares: ')
for c in range(0, len(numeros)):
    if numeros[c]%2==0 and numeros[c]!=0:
        print(f'{numeros[c]}', end=' ')
print(f'\no numero 9 apareceu {numeros.count(9)} vezes')
if 3 in numeros:
    print(f'o numero 3 foi encontrado na posição {numeros.index(3)+1}')
else:
    print(f'o numero 3 não foi encontrado')