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
'''
#103
#ficha do jogador

def cadastro(nome='<Desconhecido>', gols=0):
    print(f'O jogador{nome} fez {gols} gol(s) no campeonato.')

n = str(input('Nome do jogador: '))
g = str(input('Número de gols: '))

if g.isnumeric():
    g = int(g)

if n.strip() == '':
    cadastro(gols = g)

else:
    cadastro(n,g)
'''
'''
#104
#validaddor de dados em python

def le_numero(valor):
    ok = False
    numerico = 0

    while True:
        numero = str(input(valor)).upper().strip()
        print('=='*20)
        if numero.isnumeric():
            numerico = int(numero)
            ok = True
        else:
            print('\033[0;31mErro! Digite um número inteiro válido.\033[m')
        
        if ok:
            break
    return numerico

numero = le_numero('Digite um número: ')

print(f'O numero que você digitou foi {numero}')
'''
'''
#105
#Analisando e gerando Dicionários


def notas(*n,sit=False):
    info_situação = dict()
    info_situação['Total: '] = len(n)
    info_situação['Maior: '] = max(n)
    info_situação['Menor: '] = min(n)
    info_situação['Média: '] = sum(n)/len(n)
    if sit == True:
        if info_situação['Média: '] >= 7:
            info_situação['Situação: '] = 'Boa'
        elif info_situação['Média: '] >= 5:
            info_situação['Situação: '] = 'Razoável'
        
        else:
            info_situação['Situação: '] = 'Ruim'
    return info_situação


notas_entrada = notas(5,10,2.5,9,5, sit= True)
print(notas_entrada)
'''
'''
#106
#Interactive helping system in Python

from time import sleep

cores = ('\033[m', #0 - sem cor
'\033[0;30;41m', #1 - vermelho
'\033[0;30;42m', #2 - verde
'\033[0;30;43m', #3 - amarelo
'\033[0;30;44m', #4 - azul
'\033[0;30;45m', #5 - roxo
'\033[7;30m', #6 - branco
);

def ajuda(comando):
    titulo(f'Acessando o manual do comando \'{comando}\'',4)
    print(cores[6],end='')
    help(comando)
    print(cores[0], end='')
    sleep(2)

def titulo(mensagem, cor=0 ):
    tamanho = len(mensagem) + 4
    print(cores[cor], end='')
    print('~'*tamanho)
    print(f'{mensagem}')
    print('~'* tamanho)
    print(cores[0], end='')
    sleep(1)

comando = ''

while True:
    titulo('SISTEMA DE AJUDA PyHALP',2)
    comando = str(input('Função ou Biblioteca > '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)

titulo('Até logo!',1)
'''