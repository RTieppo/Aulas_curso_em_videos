#função part 2

'''
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
'''
'''
#102

#função para fatorial

def fatorial(n_c,show=False):
    """
    -> calcula o fatorial de um número.
    :param n_c: O número a ser calculado.
    :param show: (opcional) Mostra a conta ou não.
    """
    if show == True:
        multi = 1
        for num in range(n_c, 0, -1):
            print('x', end=' ')
            print(f'{num}', end=' ')
            multi *= num
        print(f'= {multi}')
        

    else:
        multi = 1
        for num in range(n_c,0,-1):
            multi *= num
        print(f'{multi}')

numm = int(input('Qual Nº você quer ver o fatorial? '))

valida = str(input('Quer ver o calculo? [S/N]')).upper().strip()[0]
if valida == 'S':
    valida = True
fatorial(numm, valida)

help(fatorial)
'''

