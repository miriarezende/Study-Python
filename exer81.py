expre= input('informe a expressão: ')
lista= []
for simbolo in expre:
    if simbolo == '(':
        lista.append('(')
    elif simbolo == ')':
        if len(lista)>0:
            lista.pop()
        else:
            lista.append(')')
            break
if len(lista) ==0:
    print ('sua expressão é valida')
else:
    print('sua expressão está errada')