""" def texto(text):
    print(f'~'*len(text))
    print(text)
    print(f'~'*len(text))


texto('okay OKAY okay') """
#OU
def escreva(msg):
    tam= len(msg)+4
    print('~'*tam)
    print(f'  {msg}')
    print('~'*tam)


escreva('curso em video')
escreva('cep')