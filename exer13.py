km= int(input('quantos km percorrido: '))
qd= int(input('quantos dias: '))
preco= (60*qd) + (km*0.15)
print('valor a ser pago pelo aluguel do carro é R${:.2f}'.format(preco))