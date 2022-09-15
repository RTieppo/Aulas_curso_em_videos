'''
#57
print('Valindo o sexo de uma pessoa')


S = str(input('Qual o seu sexo [M/F]: ')).strip().upper()[0]

while S not in 'MF':
    S = str(input('Qual o seu sexo [M/F]: ')).strip().upper()[0]
print('Valido')
'''
'''
#58

import random

#opção 1
print('Vamos brincar de adivinhar')
print ('Acabei de pensar em um numero de 1 até 50')

n_a = int(random.randint(1, 50))
P = int(input('Qual o seu palpite: '))
t = 0
while P != n_a:
    if P > n_a:
        print('Menos... Tente novamente!')
        P = int(input('Qual o seu palpite: '))
        t += 1
    elif P < n_a:
        print('Mais... Tente novamente!')
        P = int(input('Qual o seu palpite: '))
        t += 1
print('Acertou com {} tentaivas.'.format(t+1))
'''
'''
#opção 2
from random import randint

c = randint(1,10)
print("sou o seu computador.. acabei de pensar em um Número entre 0 e 10.")
print('Será que você consegue adivinhar qual foi?')

acertou = False
palpites = 0

while not acertou:
    jogador = int(input('Qual é o seu palpite? '))
    palpites += 1
    if jogador == c:
        acertou = True
    else:
        if jogador < c:
            print('Mais... Tente mais uma vez.')
        elif jogador > computador:
            print('Menos... tente mais uma vez.')
print('Acertou com {} tentativas. Parabéns!'. format(palpites))
'''
'''
#59
from time import sleep
print('Menu de opções')

Final = False

n1 = float(input('Primeiro Nº:'))
n2 = float(input('Segundo Nº: '))

while not Final:
    print('[1] Somar'
    '\n[2] Multplicar'
    '\n[3] Maior Nº'
    '\n[4] Novos Nº'
    '\n[5] Sair do programa')
    opçao =  int(input(">>>> Qual é a sua opção? "))

    if opçao == 1:
        print('\033[32mA soma entre {} + {} é {}.\033[m'. format(n1,n2, n1+n2))
        print('==-=='*8)
    
    elif opçao == 2:
        print('\033[32mO resultado de {} x {} é {}.\033[m' .format(n1, n2, n1*n2))
        print('==-=='*8)
    
    elif opçao == 3:
        if n1 > n2:
            print('\033[32mO maior Nº é {}.\033[m' .format(n1))
            print('==-=='*8)
        elif n2 > n1:
            print('\033[32mO maior Nº é {}.\033[m' .format(n2))
            print('==-=='*8)
        else:
            print('\033[32mOs dois são iguais\033[m')
            print('==-=='*8)

    elif opçao == 4:
        print('informe os novos Nº:')
        n1 = float(input('Primeiro Nº:'))
        n2 = float(input('Segundo Nº: '))
        print('==-=='*8)
    
    elif opçao == 5:
        Final = True
        print('\033[33mFinalizando...\033[m')
        print('==-=='*8)
        sleep(3)
    
    else:
        print('\033[31mOpção invalida. Tente novamente\033[m')
        print('==-=='*8)

print('\033[32mFim do programa! Volte sempre!\033[m')
'''

#60
'''
print('Calculando o fatorial de um numero')
 #opção 1 usando o math
from math import factorial
n = int(input('Digite o Nº desejado: '))
fa = factorial(n)
print('O fatorial do {} é {}.' .format(n, fa))
'''
'''
print('Calculando o fatorial de um numero')
# opção 2 usando o While

n = int(input('Digite o Nº desejado: '))
calcula = n
multi_f = 1

print('Calculando {}! = '.format(n), end='')

while calcula > 0:
    print('{}'.format(calcula), end='')
    print(' x ' if calcula > 1 else ' = ', end='')
    multi_f *= calcula
    calcula -= 1
print('{}' .format(multi_f))
'''
'''
print('Calculando o fatorial de um numero')
# opção 2 usando o for

n = int(input('Digite o Nº desejado: '))

cal_f = n
multi = 1

print('Calculando {}! = '.format(n), end='')
for fa in range(n, 0, -1):
    print('{}'.format(fa), end='')
    print(' x ' if fa > 1 else' = ', end='')
    multi *= fa
print('{}' .format(multi))
'''
'''
#61
#gerando uma PA com While
print('gerador de PA')
print('-='*10)

P_termo = int(input('Qual vai ser o Termo: '))
razã0 = int(input('Razão: '))
contador = 1

while contador <= 10:
    print('{} - ' .format(P_termo), end='')
    P_termo += razã0
    contador += 1
print('Fim')
'''
'''
#62
print('Aprimorando o gerador de PA')
print('gerador de PA')
print('-='*10)


primeiro = int(input('Qual o primeiro termo: '))
razao = int(input('Qual a razão: '))
termo = primeiro
contador = 1
total = 0
nv = 10

while nv != 0:
    total = total + nv
    while contador <= total:
        print('{} - '.format(termo), end='')
        termo += razao
        contador += 1
    print('Pausa')
    nv = int(input('Quantos termos você quer mostrar a mais? '))

print('Fim do Programa! \nforam mostrados {} termos.' .format(contador))
'''
'''
#63

print('mostrando a sequencia de fibonacci')
print('-'*30)
print('Fibonacci')
print('-'*30)

n = int(input('Quantos termos você quer mostrar? '))

t1 = 0
t2 = 1

print('-' *30)
print('{} - {} - '.format(t1, t2), end='')
conta = 3

while conta <= n:
    soma = t1 + t2
    print('{} - '.format(soma), end='')
    conta += 1
    t1 = t2
    t2 = soma

print('fim')
'''
'''
#64

print('Vamos somas os termos ignorando um especifico')

final = True
conta = soma = 0

while final == True:
    n = int(input('Digite um número [999 para parar]: '))
    if n != 999:
        conta += 1
        soma += n
    else:
        final = False
print('A soma de {} é {}.' .format(conta, soma))
'''

#65
#minha versão

'''
print('lendo varias variaveis e apresentando media, maior e menor')

fim = False
conta = soma = 0
maior = 0
n_z = int(input('Digite um numero: '))
menor = n_z

while not fim:
    p = str(input('Quer continuar? [S/N]')).upper().strip()[0]

    if p == 'S':
        n_c = int(input('Digite um numero: '))
        conta += 1
        soma += n_c

        if n_c > maior:
            maior = n_c

        else:
            menor = n_c

    elif p == 'N':
        fim = True
    
    else:
        print('Caracter invalido')

print('Você digitou {} Nº a media deles foi {}' .format((conta+1), (soma+n_z)/(conta+1)))
print('O maior numero foi {} e o menor foi {}'.format(maior, menor))
'''

#versão corrigida
'''
resp = 'S'

soma = quant = media = maior = menor = 0

while resp in 'Ss':
    num = int(input('Digite um numero: '))
    soma += num
    quant += 1

    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num

    resp = str(input('Quer continuar? [S/N]')).upper().strip()[0]

media = soma/quant

print('Você digitou {} Nº a media deles foi {}' .format(quant, media))
print('O maior numero foi {} e o menor foi {}'.format(maior, menor))
'''



