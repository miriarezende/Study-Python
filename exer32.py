salario = float(input('informe salario: '))
if salario>1250:
    print('aumento de 10% \nnovo salario: {}'.format(salario+(salario*0.1)))
else:
    print('aumento de 15% \nnovo salario: {}'.format(salario+(salario*0.15)))