from datetime import date
sexo= input('''informe seu sexo:
                F feminino
                M masculino\n''').upper()
if sexo == 'M':
    anoatual= date.today().year
    ano= int(input('que ano vc nasceu? '))
    if anoatual-ano == 18:
        print('é hr d se alistar')
    elif anoatual-ano <18:
        print('ainda falta um tempo para se alistar, {} anos\n Seu alistamento sera em {}'.format(18-(anoatual-ano), anoatual+(18-(anoatual-ano))))
    elif anoatual-ano > 18:
        print('ja passou alguns anos de se alistar, {} ano\n Você deveria ter se alistado em {}'.format((anoatual-ano)-18,anoatual-((anoatual-ano)-18)))
elif sexo=='F':
    print('você não precisa realizar alistamento militar obrigatorio')