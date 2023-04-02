from datetime import date
anoatual= date.today().year
maior=0
menor=0
for c in range(0,7):
    nasc=int(input('ano de nascimento, participante {}: '.format(c+1)))
    idade=anoatual-nasc
    if idade>=18:
        maior+=1
    else: 
        menor+=1
print('maiores de idade: {}\nainda não atingiram a maioridade:{}'.format(maior, menor))