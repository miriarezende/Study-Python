"""from datetime import date
def voto(ano): 
    if 18 <=ano <=70:
        return 'obrigatorio'
    if ano>70 or 16<=ano<=17:
        return 'opcional'
    else:
        return 'negado'

year=int(input('ano de nascimento: '))
ano=date.today().year-year
print(f'com {ano} anos: voto {voto(ano)}') """
#OU

def voto(ano):
    from datetime import date
    idade=date.today().year-ano
    if 16>idade:
        return f'com {idade} anos: NAO VOTA'
    if idade>70 or 16<=idade<18:
        return f'com {idade} anos: VOTO OPCIONAL'
    else:
        return f'com {idade} anos: VOTO OBRIGATORIO'


print(voto(int(input('em que ano você nasceu? '))))