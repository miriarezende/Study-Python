from random import randint
aleatorio= (randint(0,10), randint(0,10), randint(0,10), randint(0,10), randint(0,10))
print('valores sorteados: ')
for c in aleatorio:
    print(f'{c}', end=' ')
print(f'\nmaior valor= {max(aleatorio)}')
print(f'menor valor= {min(aleatorio)}')