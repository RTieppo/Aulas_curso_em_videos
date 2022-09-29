#Def
'''
#96
#função que calcula área

def calculo_area(l,c):
    print(f'A área de um terreno {l}x{c} é de {l*c}m².')


print ('Controle de Terreno')
print('----'*10)

calculo_area(float(input('Largura (m): ')), float(input('Comprimeto (m): ')))
'''
'''
#97

#print especial

def print_e(valor):
    print('--'*len(valor))
    print(f'{valor:^10}')
    print('--'*len(valor))

print_e(str(input('Digite o alguma coisa: ')))
'''
'''
#98
#função de contagem
from time import sleep


def contador(inicial,fim,intervalo):

    if intervalo == 0:
        intervalo = 1
    
    if intervalo < 0:
        intervalo *= -1

    if inicial < 0:
        inicial *= -1
    
    if fim < 0:
        inicial *= -1

    print('==='*10)
    print(f'Contagem de {inicial} até {fim} de {intervalo} em {intervalo}')
    
    if inicial < fim:
        for n in range(inicial,fim+1,intervalo):
            print(f'{n}', end=' ', flush=True)
            sleep(0.1)

        print('FIM!')
    
    else:
        conta = inicial
        while conta >= fim:
            print(f'{conta}', end=' ', flush=True)
            conta -= intervalo
            sleep(0.1)
        print('FIM!')



contador(1,10,1)
contador(1,10,2)

print('==='*10)
print('Sua vez:')
contador(int(input('Início: ')), int(input('Fim: ')), int(input('Passo: ')))

'''

'''
#99
#Função que descobre o maior

from time import sleep

def analise(* núm):
    valor_base = 0
    print('=='*30)
    print('Analisando os valores passados...')
    for n in núm:
        print(f'{n}', end=' ', flush=True)
        sleep(0.2)
        if n >valor_base:
            valor_base = n
    print(f'Foram informados {len(núm)} valores ao todo')
    print(f'O maior valor informado foi {valor_base}')


analise(10,5,6,8)

analise(10,2,5,11,15)

analise(0)

analise()
'''
'''
 #100
#função para sortear e somar
from random import randint
from time import sleep
aletorio = list()

def sorte():
    print('Sorteando 5 valores da lista: ', end='')
    for nu in range(0,5):
        numero = randint(0,10)
        print(f'{numero}', end=' ', flush=True)
        sleep(0.3)
        aletorio.append(numero)

def soma():
    soma = 0
    for par in aletorio:
        if par %2 == 0:
            soma += par
    print(f'\nSomando os valores sorteados {aletorio}, temos: {soma}')

exetuta = sorte()
exetuta1 = soma()
'''