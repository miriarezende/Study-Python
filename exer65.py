from random import randint
ven=0
while True:
    n= int(input('bora jogar par ou impar, jogue seu numero: '))
    pc= randint(1,10)
    soma= n+pc
    jogada= input('[P] par ou [I]: ').upper()
    while jogada not in 'PI':
        jogada= input('digite um valor valido, [P] par ou [I]: ').upper()
    if soma%2==0 and jogada=='p':
        print(f'você: {n} computador: {pc} total= {soma}\n deu par, vc VENCEU!!')
        ven+=1
    elif soma%2!=0 and jogada=='I':
        print(f'você: {n} computador: {pc} total= {soma}\n deu impar, vc VENCEU!!')
        ven+=1
    else:
        print(f'você: {n} computador: {pc} total= {soma}')
        print(f'PERDEU, {ven} vitorias consecutivas')
        break