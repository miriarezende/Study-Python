def aumentar(v=0,n=0, resp=False):
    v+=(n*v)/100
    if resp:
        return real(v)
    else:
        return v


def diminuir(v=0,n=0, resp=False):
    v-=(n*v)/100
    if resp:
        return real(v)
    else:
        return v


def dobro(v=0, resp=False):
    v*=2
    if resp:
        return real(v)
    else:
        return v


def metade(v=0, resp=False):
    v/=2
    if resp:
        return real(v)
    else:
        return v
    

def real(v=0, m='R$'):
    return f'{m}{v:>.2f}'.replace('.',',')

def resumo(a=0,b=15,c=11):
    print('-'*30)
    print(f'resumo do valor'.center(30))
    print('-'*30)
    print(f'preço analisado: \t{real(a)}')
    print(f'{b}% de aumento: \t{aumentar(a,b, True)}')
    print(f'{c}% de redução: \t{diminuir(a,c,True)}')
    print(f'dobro do preço: \t{dobro(a, True)}')
    print(f'metade do preço: \t{(metade(a,True))}')
    print('-'*30)