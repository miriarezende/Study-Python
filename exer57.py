from time import sleep
n1=float(input('informe primeiro valor: '))
n2= float(input('informe segundo valor: '))
op=0
while op!=5:
    op=int(input('''        1 somar
        2 multiplicar
        3 maior
        4 novos numeros
        5 sair do programa
        selecione a operação que deseja realizar: '''))
    if op==1:
        print('soma= {}'.format(n1+n2))
    if op==2:
        print('multiplicar= {}'.format(n1*n2))
    if op==3:
        if n1>n2:
            print('maior= {}'.format(n1))
        else:
            print('maior= {}'.format(n2))
    if op==4:
        n1=float(input('informe novo primeiro valor: '))
        n2= float(input('informe novo segundo valor: '))
    if 0<op>5:
        print('codigo da operação invalido!!')
    
print('SAINDO...')
sleep(2)
print('FIM')