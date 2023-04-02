from pacote.modulos import moeda

p=float(input('preço: R$'))
print(f'aumentando 10%, temos {moeda.real(moeda.aumentar(p, 10))}')
print(f'diminuindo 20%, temos {moeda.real(moeda.diminuir(p, 20))}')
print(f'dobro de {moeda.real(p)} é {moeda.real(moeda.dobro(p),"R$")}')
print(f'metade de {moeda.real(p)} é {moeda.real(moeda.metade(p))}')