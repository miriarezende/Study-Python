""" def factorial (n, show=True):  
     calcula o fatorial de um numero
        :param n: o numero a ser calculado
        :param show: (opcional) mostrar ou não a conta
        :return: o valor do fatoral de um numero n  
    f=1
    while n>0:
        if show:
            if n==1:
                print(f'{n} = ', end='')
            else:
                print(f'{n} x ', end='') 
        f*= n
        n-=1
    return f
print(factorial(4, True))
help(factorial) """
#OU
def factorial (n, show=True):
    """ calcula o fatorial de um numero
        :param n: o numero a ser calculado
        :param show: (opcional) mostrar ou não a conta
        :return: o valor do fatoral de um numero n """
    f=1
    for c in range(n,0,-1):
        if show:
            print(c, end='')
            if c>1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f*=c
    return f

help(factorial)
print(factorial(4, True))