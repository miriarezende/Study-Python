pares = []
impares = []
n=[]
while True:
    numero=int(input('informe um numero:'))
    n.append(numero)
    if numero%2==0:
        pares.append(numero)
    else:
        impares.append(numero)
    resp=input('deseja continuar: ').upper()
    while resp not in 'SN':
        resp=input('deseja continuar: ').upper()
    if resp=='N':
        break
print(f'lista geral: {n} \nlista pares: {pares} \nlista impares: {impares}') 