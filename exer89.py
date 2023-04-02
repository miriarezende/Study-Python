from datetime import date
datas={}
anonascimento= int(input('ano de nascimento: '))
anoatual= date.today().year
nascimento=anoatual-anonascimento
datas['nome']=input('Nome: ')
datas['idade']= nascimento
datas['ctps']=int(input('carteira de trabalho (0 não tem): '))
if datas['ctps']!=0:
    datas['contratação']=int(input('ano de contratação: '))
    datas['salario']=float(input('salario: '))
    aposentadoria= anoatual-datas['contratação']
    if aposentadoria<35:
        aposentadoria=datas['contratação']+35
        aposentadoria=aposentadoria-anonascimento
        datas['aposentadoria']=aposentadoria
    else:
        datas['aposentadoria']=nascimento
print(datas)
for k, v in datas.items():
    print(f'{k} tem valor {v}')