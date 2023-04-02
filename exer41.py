n1= float(input('reta 1: '))
n2= float(input('reta 2: '))
n3= float(input('reta 3: '))
if n1+n2 > n3 and n1+n3>n2 and n2+n3>n1:
    print('é possivel formar um triangulo')
    if n1==n2==n3:
        print('formara triangulo equilatero')
    elif n1!=n2!=n3!=n1:
        print('formara triangulo escaleno')
    else:
        print('formara triangulo isosceles')
else:
    print('não é possivel formar um triangulo')