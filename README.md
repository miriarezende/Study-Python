# GUIA DE ESTUDO EM <=PYTHON=>


## Tipos de variaveis
    - int - inteiro 1 
    - float - real 0.5
    - bool - boleano True/False
    - str - texto 'palavra' '2.3'

## Operadores aritmeticos
    + adição
    - subtração
    * multiplicação
    / divisão
    ** potencia OU pow(perde, precedencia)
    // div (parte inteira da divisão)
    **(1/2) raiz quadrada (25//(1/2))
    **(1/3) raiz cubica
    "sqrt" raiz quadrada
    % mod(resto da divisão)
        ordem de precedencia
            ()
            **
            * / // %
            + - 

## Formatação
    \n                     quebra linha
    end=''                 não quebra linha
    :.NUMEROdpsVIRGULAf    ex.: print('texto {:.2f}'.format(variavel))

## Importação
    "import biblioteca"                 importa biblioteca inteira
    "from biblioteca importa função"    importa função especifica
    math                                biblioteca matematica
    random                              biblioteca aleatoria

    #exemplo
        from math import sqrt, trunc, hypot, sin, cos, tan, radians
        from random import choice, shuffle

## Strings
        --> cadeia de caracteres
    Fatiamento
            --> sempre exclui ultima posição
        - variavel[index]       unico caractere
        - variavel[começo:fim]  vai pegar aquele intervalo de caracteres
        - variavel[começo:fim:pulaintervalo]
        - variavel[:fim]        começa do 0 ate o index indicado
        - variavel[inicio:]     começa do index indicado ate o final

    Analise
        - len(variavel)                                  mostra a quantidade de caracteres da string
        - variavel.count('caractere')                    mostra quantas vezes aparece esse caractere
        - variavel.count('caractere', inicio, fim)       mostra quantas vezes aparece esse caractere no fatiamento especificado
        - variavel.find('sequenciadecaracteres')         mostra em q index começa a sequencia de caracteres a ser encontrada
        -'sequenciadecaracteres' in variavel             retorna true ou false se existe tal sequencia na string
        - variavel.replace('caracteres','substitução')   substitui a primeira sequencia pela segunda
        - variavel.upper()                               transforma caracteres em maisculos
        - variavel.lower()                               transforma em minusculo
        - variavel.capitalize()                          tranforma so a primeira letra em maisculo
        - variavel.title()                               tranforma maisculo as primeiras letras de cada palavra dentro da string
        - variavel.strip()                               remove os espaços do começo e fim
        - variavel.rstrip()                              remove os espaços apenas da direita
        - variavel.lstrip()                              remove os espaços apenas da esquerda
        - variavel.split()                               divide cada palavra a partir dos espaços, recomeça o index de cada palvra e cada palvra novo elemento d uma lista
        -  '-'.join(variavel)                            junta cada elemento usanddo o caracter especificado
    
    obs.: """ IMPRIMI O TEXTO EM BLOCO NA TELA """

## REPETIÇÃO

    Estrutura FOR
        for variavel in range(inicio,fim, passo):
            s+=n

    Interronpendo o while
        while True:
           programa
           break

##  TUPLA                    é imutavel
        variavel(' ', ' ',....)
        for c in range(0, len(variavel))
            print(lanche[c])                forma de mostrar conteudo tupla

        for i, c in enumerate(variavel):
           print(c, i)                      'i' mostra a posição do elemento

        for c in lanche:
           print(c)

        del(variavel)                           apaga tupla


## LISTAS                    são mutaveis
    variavel= [2,3,2,...]
    variavel= list(range(4,11))
    variavel.sort()                     ordenar de forma crescente
    variavel.sort(reverse=True)         ordenar de forma decrescente
    variavel.append(7)                  adicionar novo valor
    variavel.insert(2,0)                adionar na posição 2 o valor 0
     if valor in variavel:
       variavel.remove(valor)
    variavel=variavel[:]                copia d lista
    variavel.clear()                    limpa lista

## DICIONARIOS
    variavel={'index': 'elemento', 'index':'elemento'}
    variavel= dict()
    variavel['nomeindex']='elemento'
    del variavel['nomeindex']                           deleta o index
    print(variavel.values())                            mostra elementos
    print(variavel.keys())                              mostra index
    print(variavel.itemn())                             mostra index e elementos
    for k,v in variavel.items():
        print(f'o{k} é {v}')                            mostra todos elementos do dict
    variavel.append(variavel.copy())                    fazer copia na leitura

 

## COMANDO HELP
    help(funçao)                    saber como funciona de terminada função ex:.help(print)

## FUNCTIONS 
    def funçao(parametro1=0, parametro2=0, parametro):          parametros opcionais
        codigo
        return variavel
    variavel=funcação()


## TRATAMENTO DE ERRO
    try:
       tente fazer isso(comando)
    except:
       se der problemas(comando)
    else:
       se der certo(comando)
    finally:
       acontece sempre(comando)