from time import sleep
def maior(*num):
    cont=maior=0
    for valor in num:
        print(f'{valor} ', end='', flush=True)
        sleep(0.3)
        if cont==0:
            maior=valor
        else:
            if valor>maior:
                maior=valor
        cont+=1
    print(f'foram informados {cont} valores ao todo')
    print(f'maior valor informado foi {maior}')


maior(2,9,4,5,7,1)
maior(0,2)
maior(5)
maior()