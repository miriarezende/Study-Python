from math import sin, cos, tan, radians

n1 = float(input('digite angulo: '))
s= sin(radians(n1))
c= cos(radians(n1))
t= tan(radians(n1))
print('Seno de {:.0f} é {:.2f}'.format(n1, s))
print('Cosseno de {:.0f} é {:.2f}'.format(n1, c))
print('Tangente de {:.0f} é {:.2f}'.format(n1, t))