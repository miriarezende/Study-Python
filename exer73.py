""" produto= ('fone', 358.00, 'tenis', 200.00)
for c in range(0,len(produto)):
    if c==0 or c%2==0:
        print(f'{produto[c]} ','.'*30, f'{produto[c+1]}')  """
#OU
produto= ('fone', 358.00, 'tenis', 200.00, 'mouse', 150.53)
for c in range(0, len(produto)):
    if c%2==0:
        print(f'{produto[c]:.<30}', end='')
    else:
        print(f'R${produto[c]:>7.2f}')