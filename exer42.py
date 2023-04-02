peso= float(input('qual seu peso: '))
altura= float(input('qual sua altura: '))
imc= peso/(altura*altura)
if imc<18.5:
    print('abaixo do peso {:.2f}' .format (imc))
elif 18.5<= imc <25:
    print('peso ideal {:.2f}' .format (imc))
elif 25<= imc<30:
    print('sobrepeso')
elif 30<= imc<40:
    print('obesidade')
else:
    print('obesidade morbida')