casa= float(input('valor da casa: '))
salario= float(input('qual o seu salario? '))
anos= int(input('em quantos anos vai pagar? '))
prestação = casa/(anos*12)
if prestação > salario*30/100:
    print('emprestimo negado')
else:
    print('emprestimo aprovado')