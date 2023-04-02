def leiaint(text):
    while True:
        try:
            n=int(input(text))
        except(KeyboardInterrupt):
            print('entrada de dados interrompida pelo usuario')
            return 0
        except:
            print('\033[31mERRO\033[m')
        else:
            return n

def leiafloat(text):
    while True:
        try:
            n=float(input(text).strip())
        except(ValueError,TypeError):
            print('\033[31mERRO\033[m')
            continue
        except(KeyboardInterrupt):
            print('entrada de dados interrompida pelo usuario')
            return 0
        else:
            return n

n2=leiaint('informe um numero inteiro: ')
n1=leiafloat('informe um numero real: ')
print(f'numero inteiro digitado é {n2} e o real {n1}')