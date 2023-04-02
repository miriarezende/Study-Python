saque= int(input('valor a ser sacado: '))
ced=50
totalced=0
while True:
    if saque>=ced:
        saque-=ced
        totalced+=1
    else:
        if totalced>0:
            print(f'total de {totalced} cedulas de R${ced}')
        if ced==50:
            ced=20
        elif ced==20:
            ced=10
        elif ced==10:
            ced=1
        totalced=0
        if saque==0:
            break