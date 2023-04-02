#ANSI
print('\033[4;32;47m okay\033[m')
a=3
b=5
print('valores são \033[33m{}\033[m e \033[31m{}\033[m !!'.format(a,b))

name='nomequalquer'

print('ola, prazer {}{}{}'.format('\033[33m', name, '\033[m'))

cores = {'limpa':'\033[m',
            'red':'\033[31m',
            'blue':'\033[34m',
            'blackwhite':'\033[7;30m'}
print('ola, prazer {}{}{}'.format(cores['red'], name, cores['limpa']))