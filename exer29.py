distancia = int(input('distancia da viagem em Kilometros: '))
if distancia > 200:
    print('passagem custa R${:.2f}'.format(distancia*0.45))
else:
    print('passagem custa R${:.2f}'.format(distancia*0.5))