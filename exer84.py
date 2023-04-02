""" matriz=[]
linha=[]
for i in range(0,3):
    for j in range(0,3):
        linha.append(int(input('informe os valores: ')))
    matriz.append(linha[:])
    linha.clear()
for c in range(0,3):
    print(matriz[c]) """
#OU
matriz=[]
linha=[]
for i in range(0,3):
    for j in range(0,3):
        linha.append(int(input('informe os valores: ')))
    matriz.append(linha[:])
    linha.clear()
for i in range(0,3):
    for j in range(0,3):
        print(matriz[i][j], end=' ')
    print()
#OU
""" matriz=[[0,0,0], [0,0,0], [0,0,0]]
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'digite um valor para[{l}, {c}]: '))
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]', end=' ')
    print() """