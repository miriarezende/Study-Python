qntd= soma=0
while True:
    n=int(input('informe um numero (999 para parar): '))
    if n==999:
        break
    qntd+=1
    soma+=n
print(f'foram informados {qntd}, a soma deles {soma}')