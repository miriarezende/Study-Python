""" def leiaint(msg):
    while True:
        n=input(msg)
        if n.isnumeric():
            n=int(n)
            print(f'você acabou de digitar o numero {n}')
            break
        else:
            print(f'\033[0;31mERRO! digite um nummero inteiro.\033[m')


leiaint('digite um numero: ')  """ 
#OU
def leiaint(msg):
    ok=False
    valor=0
    while True:
        n=input(msg)
        if n.isnumeric():
            valor=int(n)
            ok=True
        else:
            print('\033[0;31mERRO! digite um numero inteiro valido. \033[m')
        if ok:
            break
    return valor
n=leiaint('digite um numero: ')
print(f'você acabou de digitar o numero {n}')