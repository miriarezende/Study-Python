from sistem.menu import *
from sistem.arquivo import *
from time import sleep

arq='cadastro.txt'
if not arquivoexiste(arq):
    criararquivo(arq)

while True:
    resp=menu({'ver pessoas cadastradas',  'cadastrar nova pessoa', 'sair do sistema'})
    if resp==1:
        cabeçalho('pessoas cadastradas')
        lerarquivo(arq)
    elif resp==2:
        cabeçalho('novo cadastro')
        novocadastro(arq)
    elif resp==3:
        cabeçalho('saindo do sistema..')
        break
    else:
        print('\033[31mErro! digite uma opção valida\033[m')
    sleep(2)
