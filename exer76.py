valores=[]
for c in range(0,5):
    valores.append(int(input(f'digite um valor para a posição {c}: ')))
    if c==0:
        maior= menor=valores[c]     
    else:
        if maior<valores[c]:
            maior=valores[c]
        if menor>valores[c]:
            menor=valores[c]
print(f'maior valor é {maior}, está na posição ', end='')
for i, v in enumerate(valores):
    if v==maior:
        print(f'{i}.. ', end='')
print(f'\nmenor valor é {menor}, está na posição ', end= '')
for i, v in enumerate(valores):
    if v==menor:
        print(f'{i}.. ', end='')
print(f'\nvalores informados {valores}')