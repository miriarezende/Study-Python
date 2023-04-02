
dicio={}
dicio['nome']= input('nome: ')
dicio['media']=float(input('media: '))
if dicio['media']<7:
    dicio['situação']= 'reprovado'
else:
    dicio['situação']= 'aprovado'
for k, v in dicio.items():
    print(f'{k}={v}')