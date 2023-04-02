def leiaint(msg):
    while True:
        try:
            n=int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO! digite um numero inteiro valido\033[m')
            continue
        except (KeyboardInterrupt):
            print('usuario preferiu não informa um numero')
            return 0
        else:
            return n

def leianome(msg):
    while True:
            nome=input(msg)
            mud=nome.strip().replace(' ', 'a')
            if not mud.isalpha():
                print('nome invalido')
            else:
                return nome
                
def linha(tam=42):
    return '-'*tam

def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())

def menu(lista):
    cabeçalho('menu principal')
    c=1
    for item in lista:
        print(f'{c} - {item}')
        c+=1
    print(linha())
    opc=leiaint('sua opção: ')
    return opc