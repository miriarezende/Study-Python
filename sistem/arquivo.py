from sistem.menu import *

def arquivoexiste(nome):
    try:
        a= open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def criararquivo(nome):
    try:
        a= open(nome, 'wt+')
        a.close()
    except:
        print('Ocorreu um erro ao criar o arquivo')
    else:
        print(f'arquivo {nome} criado com sucesso')

def lerarquivo(nome):
    try:
        a=open(nome,'rt')
    except:
        print('erro ao ler o arquivo')
    else:
        for linha in a:
            dado=linha.split(';')
            dado[1]=dado[1].replace('\n', '')
            print(f'{dado[0]:<18}{dado[1]:>4} anos')
    finally:
        a.close()

def novocadastro(arq):
    try:
        nome=leianome('nome: ')
        idade=leiaint('idade: ')
        a=open(arq,'at')        
    except:
        print('ERRO na abertura do arquivo')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('ERRO na hora de escrever os dados')
        else:
            print('novo registro adicionado.')
            a.close()