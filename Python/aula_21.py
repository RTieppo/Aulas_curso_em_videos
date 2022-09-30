#função part 2

 #101
from datetime import date

def voto(nascimento):
    idade = date.today().year - nascimento 
    return(idade)

def analise():
    idade = voto(pergunta)
    if idade < 16:
        print(f'Com {idade} anos: Não vota!')
    
    elif idade > 70 or 16 == idade < 18:
        print(f'Com {idade} anos: Voto não obrigatorio')
    
    else:
        print(f'Com {idade} anos: Voto obrigatorio!')


pergunta = (int(input('Em que ano você nacse? ')))
voto(pergunta)
analise()