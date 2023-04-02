from time import sleep

def ajuda(com):
    titulo(f"  Acessando manual do comando '{com}'",5)
    print(c[6], end='')
    help(com)
    print(c[0], end='')
    sleep(2)

def titulo(msg, cor=0):
    print(c[cor], end='')
    print('^'*(len(msg)+4))
    print(msg)
    print('^'*(len(msg)+4))
    print(c[0], end='')
    sleep(1)

c=('\033[m',            #0-sem cor  
    '\033[0;30;41m',    #1-vermelho
    '\033[0;30;42m',    #2-verde
    '\033[0;30;43m',    #3-amarelo
    '\033[0;30;44m',    #4-azul
    '\033[0;30;45m',    #5-roxo
    '\033[7;30m',      #6-branco
)

while True:
    titulo('  SISTEMA DE AJUDA PyHELP', 4)
    comando=input('Função ou biblioteca> ')
    if comando.lower() == 'fim':
        break
    else:
        ajuda(comando)
titulo('  ATE LOGO!',1)