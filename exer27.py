velocidade= int(input('velocidade do carro: '))
if velocidade>80:
    print('vc foi multado, a multa ficou R${}'.format((velocidade-80)*7))
else:
    print('está dentro da velocidade permitida')