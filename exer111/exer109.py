from pacote.modulos import moeda

p=float(input('preço: R$'))
print(f'aumentando 10%, temos {(moeda.aumentar(p, 10, True))}')
print(f'diminuindo 20%, temos{(moeda.diminuir(p, 20, True))}')
print(f'dobro de {moeda.real(p)} é {(moeda.dobro(p, True))}')
print(f'metade de {moeda.real(p)} é {moeda.metade(p, True)}')