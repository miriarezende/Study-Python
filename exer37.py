n1= int(input('informe o primeiro numero: '))
n2= int(input('informe o segundo numero: '))
if n1>n2:
    print('primeiro valor {} é maior'.format(n1))
elif n2>n1:
    print('segundo valor {} é maior'.format(n2))
else:
    print('valores iguais')