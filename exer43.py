valor= float(input('preço a ser pago pelo produto: '))
formapagamento= int(input('''
    1. para a vista
    2. a vista cartão
    3. 2x no cartão
    4. 3x ou mais no cartão
informe a forma de pagamento:'''))
if formapagamento==1:
    valorfinal = valor-(valor*10/100)
elif formapagamento==2:
    valorfinal=valor-(valor*5/100)
elif formapagamento==3:
    valorfinal=valor
    print('A compra será parcelada em 2x de R${:.2f}'.format(valorfinal/2))
elif formapagamento==4:
    valorfinal= valor+(valor*20/100)
    parcelas= int(input('deseja parcelar em quantas vezes? '))
    print('A compra será parcelada em {}x de R${:.2f}'.format(parcelas, valorfinal/parcelas))
else:
    print('forma de pagamento invalida')
print('preço final= R${}'.format(valorfinal))