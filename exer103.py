""" def notas(*nota, situ=False):
     função para analisar notas e situação de varios alunos
    :param nota: uma ou mais notas e situação de varios alunos
    :param situ: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionario com varias informações sobre a situação da turma 
    dic=dict()
    maior=menor=media=0
    for c in range(0,len(nota)):
        if c==0:
            maior=menor=nota[c]
        else:
            if maior<nota[c]:
                maior=nota[c]
            if menor>nota[c]:
                menor=nota[c]
        media+=nota[c]
    dic['quantidade']=len(nota)
    dic['maior']=maior
    dic['menor']=menor
    dic['media']=media/len(nota)
    if situ==True:
        if dic['media']>=7:
            dic['situação']='boa'
        elif 5<=dic['media']<7:
            dic['situação']='razoavel'
        else:
            dic['situação']='ruim'
    return dic
print(notas(5,10,8,4,10,6,7, situ=True))
#help(notas) """
#OU
def notas(*nota, situ=False):
    """ função para analisar notas e situação de varios alunos
    :param nota: uma ou mais notas e situação de varios alunos
    :param situ: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionario com varias informações sobre a situação da turma  """
    scor=dict()
    scor['total']=len(nota)
    scor['maior']=max(nota)
    scor['menor']=min(nota)
    scor['media']=sum(nota)/len(nota)
    if situ:
        if scor['media']>=7:
            scor['situação']='BOA'
        elif scor['media']>=5:
            scor['situação']='RAZOAVEL'
        else:
            scor['situação']='RUIM'
    return scor


resp= notas(5.5,2.5,1.5,situ=True)
print(resp)
help(notas)