contagem= ('zero', 'um', 'dois', 'tres','quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    while True:
        n=int(input('digite um numero entre 0 e 20: '))
        if 0<=n<=20:
            break
        print('tente novamente')
    print(contagem[n])
    resp=input('deseja continuar? ')
    while resp not in 'NnSs':
        resp=input('tente novamente, deseja continuar? ')
    if resp=='n':
        break