while True:
    n=int(input('informe um numero(numero negativo para encerrar): '))
    if n<0:
        break
    for c in range(1,11):
        tabu= c*n
        print(f'{c}x{n}= {tabu}')