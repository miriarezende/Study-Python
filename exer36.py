n1= int(input('informe um numero: '))
print('''        1 para binario
        2 para octal
        3 para hexadecimal
escolha a base de convesão: ''')
conversao= int(input())
if conversao == 1:
    print('{} convertido pra binario é: {}'.format(n1, bin(n1)[2:]))
elif conversao == 2:
    print('{} convertido pra octal é: {}'.format(n1, oct(n1)[2:]))
elif conversao == 3:
    print('{} convertido pra hexadecimal é: {}'.format(n1, hex(n1)[2:]))
else:
    print('opção inavalida')