from math import  hypot, sqrt
co = float(input('digite comprimento cateto oposto: '))
ca= float(input('digite comprimento cateto adjacente: '))
#h= sqrt((co**2)+(ca**2))   ou 
h= hypot(co,ca)
print('hipotenusa= {:.2f}'.format(h))