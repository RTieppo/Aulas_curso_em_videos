'''
#46
import time
import emoji

print('Contagem regresiva de fogos')

for c in range(10, -1, -1):
    print(c)
    time.sleep(0.5)

print(emoji.emojize('🤩Feliz ano novo🤩'))
'''

'''
#47
from time import sleep

print('indentificando numero pares')

n1 = int(input('Informe o primeiro Nº: '))
n2 = int(input('Informe o segundo Nº: '))

for c in range(n1, n2+1):
    resto =  c%2
    if resto == 0:
        print(c ,end=',')


'''
'''
#48

print('Vamos indentificar os numeros impares e somar o ')

n1 = int(input('Informe o primeiro Nº: '))
n2 = int(input('Informe o segundo Nº: '))

soma = 0
cont = 0

for inpar in range(n1, n2+1):
    if inpar %2 != 0:
        if inpar %3  == 0:
            soma += inpar
            cont += +1
            
print(cont)
print(soma)
'''
'''
#49
print('Tabuada em laço')

n1 = int(input('Qual tabuaba você quer consultar: '))

for tabuada in range(1,11):

    print('{} x {:2} = {}'.format(n1, tabuada, n1*tabuada)) 
'''
'''
#50

print('somando os numero inpares')
soma = 0
cont = 0
for n in range(1,7):
    num = int(input('Digite o {}° valor: '. format(n)))
    if num %2 == 0:
        soma += num
        cont += 1
print('{} - {}'.format(soma, cont))
'''
'''
#51
print('Vamos mostrar uma PA')

primeiro_t = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = primeiro_t + (10 - 1) * razao
for c in range(primeiro_t, decimo + 1, razao): #usar a razão ou mais 1
    print('{}'.format(c), end='-')
print('Fim')
'''
'''
#52

print('indentificando numeros primos')

n = int(input('Qual numero será verificado: '))
conta_divisiveis = 0

for c in range(1,n+1):
    
    if n % c == 0:
        print('\033[31m{}' .format(c), end=' ')
        conta_divisiveis += 1
    else:
        print('\033[33m{}' .format(c), end=' ')

if conta_divisiveis == 2:
    print('\033[m\nO Nº {} é divisivel {} vezes.\nsendo assim um numero \033[32mPrimo\033[m'.format(n, conta_divisiveis))
else:
    print('\033[m\nO Nº {} é divisivel {} vezes.\nsendo assim ele não é um numero \033[31mPrimo\033[m'.format(n, conta_divisiveis))
'''
'''
#53

print('indentificando um palavra palindromo')

frase = str(input('Digite a palavra ou frase: ')).strip().upper()

palavras = frase.split()
unificar = ''.join(palavras)
inverso = ''
#inverso = junto[::-1] opção usando somente o fatiamento de str
for letra in range(len(unificar) -1, -1, -1):
    inverso += unificar[letra]
if inverso == unificar:
    print('Palindromo')

else:
    print('Não é palindromo')
'''
'''
#54

import datetime

print('Validando maior idade')
ano = datetime.date.today().year
soma1 = 0
soma2 = 0

for pergunta in range(1,8):
    ano_P = int(input('Em que ano a {}º pessia nasceu? '.format(pergunta)))

    if ano - ano_P < 18:
        soma1 += 1

    if ano - ano_P >= 18:
        soma2 += 1

print('Temos {} adultos e {} menores de idade.' .format(soma2, soma1))
'''
'''
#55

print('analisando o maio e o menor')
maior = 0
menor = 0
for p in range(1,6):
    peso = float(input('Peso da {}º pessoa: '.format(p)))

    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

print('O maior peso lido foi {}KG o menor {}KG'. format(maior, menor))
'''
'''
#56

print('Analisando informações das pessoa')

conta_m_20 = 0
soma = 0
maio_h = 0
nome_mais_velho = ''

for perguntas in range(1,5):
    print('-' *10,'{}º Pessoa'.format(perguntas) ,'-'*10)
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).upper()
    soma += idade

    if perguntas == 1 and sexo =='M':
        maio_h = idade
        nome_mais_velho = nome
    
    if sexo == 'M' and idade > maio_h:
        maio_h = idade
        nome_mais_velho = nome

    if idade < 20 and sexo == 'F':
        conta_m_20 += 1
    
media = soma/4
print('A media de idade do grupo é {} anos;'.format(media))
print('O homem mais velho tem {} anos e se chama {};'.format(maio_h, nome_mais_velho))
print('Ao todo são {} mulheres com menos de 20 anos.'.format(conta_m_20))
'''





