from pacote.modulos import moeda
def leiadinheiro():
    while True:
        p=input('preço: R$').replace(',','.').strip()
        if p.isalpha() or p=='':
            print(f'\033[31mERRO! informe valor valido.\033[m')
        else:
            p=float(p)
            print(moeda.resumo(p, 10, 20))
            break