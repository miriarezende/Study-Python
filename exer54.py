media=0
mulhermenos20=0
maior=0
for c in range(0,4):
    nome= input('nome: ')
    idade= int(input('idade: '))
    sexo= input('''F feminino 
M masculino
    sexo: ''').upper()
    media+=idade
    if sexo=='F' and idade<20:
        mulhermenos20+=1
    if c==0 and sexo =='M':
        maior=idade
        homemvelho=nome
    if sexo=='M' and idade>maior:
        maior=idade
        homemvelho=nome
    
    
print('media da idade do grupo: {:.2f}'.format(media/4))
print('homem mais velho é: {}'.format(homemvelho))
print('quantidade de mulheres com menos de 20 anos são: {}'.format(mulhermenos20))