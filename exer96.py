""" from time import sleep
def contador(inicio, fim, passo):
    if passo==0:
        passo=1
    if passo<0:
        passo*=-1
    print(f'contagem de {inicio} ate {fim} de {passo} em {passo}')
    if inicio>fim:
        fim=fim-passo
        passo= -passo
    for c in range(inicio, fim+1, passo):
        print(c, end=' ', flush=True)
        sleep(0.5)
    print('fim')

contador(1,10,1)
contador(10,0,2)
contador(inicio=int(input('inicio= ')), fim=int(input('fim= ')), passo=int(input('passo= '))) """
#OU
from time import sleep
def contador(i, f, p):
    if p==0:
        p=1
    if p<0:
        p*=-1
    print(f'contagem de {i} ate {f} de {p} em {p}')
    sleep(2.5)

    if i<f:
        cont=i
        while cont<=f:
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont+=p
        print('fim')
    else:
        cont=i
        while cont>=f:
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont-=p
        print('fim')


contador(1,10,1)
contador(10,0,2)
print('personalize o contador: ')
ini= int(input('inicio: '))
fim=int(input('fim: '))
pas=int(input('passo: '))
contador(ini, fim, pas)