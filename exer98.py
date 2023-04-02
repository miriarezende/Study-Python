from random import randint
def sorte():
    print(f'sorteando {len(lista)} valores da lista:', end='')
    for c in range(0,5):
        lista.append(randint(1,10))
        print(end=' 'f'{lista[c]}')
    print()
    
def somapar():
    s=0
    for c in range(0,5):
        if lista[c]%2==0:
            s+=lista[c]
    print(f'soma valores pares de {lista} é {s}')


lista = []
sorte()
somapar()