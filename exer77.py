numeros= []
while True:
    numero=int(input('digite um valor: '))
    if numero not in numeros:
        numeros.append(numero)
    else: 
        print('numero repetido, não adicionado')
    resp=input('deseja continuar? (S/N)').lower()
    while resp not in 'sSnN':
        resp=input('tente novamente, deseja continuar? (S/N)').lower()
    if resp=='n':
        break
numeros.sort()
print(numeros)