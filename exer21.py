n1= int(input('informe um numero: '))
u= n1//1 %10
d= n1//10 %10
c= n1//100 %10
m= n1//1000 %10
print('numero informado: {} \n milhar: {} \n centena: {} \n dezena: {} \n unidade: {}'.format(n1, m, c, d,u))