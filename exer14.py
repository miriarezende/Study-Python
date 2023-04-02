""" import math
n1 = int(input('digite  um numero: '))
raiz = math.sqrt(n1)
print('raiz quadrada de {} é {:.2f}'.format(n1,raiz)) """

from math import sqrt, floor
n1 = int(input('digite  um numero: '))
raiz = sqrt(n1)
print('raiz quadrada de {} é {}'.format(n1,floor(raiz)))