'''
 #36

print('simulando um emprestimo')

v_casa = float(input('Qual o valor do Imovel: R$ '))
salario = float(input('Qual o valor do seu salario? '))
anos = float(input('Em quantos anos você deseja pagar? '))

M_converte = anos * 12
parcela = v_casa / M_converte
gera_porcentagem = salario * 0.3

if parcela <= gera_porcentagem:
    print('O valor mensal da parcela é R$ {:.2f} \nSeu emprestimo foi ... \n\033[32mAprovado!\033[m \nTotal de parcelas: {:.2f} ' .format(parcela, M_converte))

elif parcela > gera_porcentagem:
    print('O valor da sua parcela ficaria de R$ {:.2f},'
    'seu emprestimo foi \n\033[31mNegado!\033[m \nPois o valor da parcela'
    'é maior que \033[31m30%\033[m do seu salario.' .format(parcela))
'''
'''
#37
print('Sistema de conversão para binario, octal e hexadecimal')

numero = int(input('Digite um numero: '))
print('Escolha uma das bases para conversão:'
'\n1 - Binário; \n2 - Octal; \n3 - Hexadecimal')

opção = int(input('Sua Opção: '))

if opção == 1:
    print('O Nº {} convertido para Binário é {}.' .format(numero, bin(numero)[2:]))

elif opção == 2:
        print('O Nº {} convertido para Octal é {}.' .format(numero, oct(numero)[2:]))

elif opção == 3:
    print('O Nº {} convertido para Hexadecimal é {}' .format(numero, hex(numero)[2:]))

else:
    print('Opção invalida')
'''

'''
#38

print('Vamos comparar numeros')

n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))

if n1 > n2:
    print('O primeiro numero é maior')

elif n2 > n1:
    print('o segundo numero é maior')

else:
    print('Não existe valor maior, os dois são iguais')
'''

'''
#39
import datetime

print('Vamos ver se está na hora de se alistar')

nascimento = int(input('Em qual ano você nacseu? '))
ano = datetime.date.today().year
idade = ano - nascimento

if idade < 18:
    tempo =  18 - idade
    print('Ainda não está na hora de se alistar \nfaltam aproximadamente {} anos pare o alistamento' .format(tempo))
    alista = ano + tempo
    print('Seu alistamento vai ser no ano {}' .format(alista))

elif idade == 18:
    print('Está na hora de se alistar')

else:
    tempo = idade - 18
    print('Você ja pssou da idade para o alistamento cerca de {}!' .format(tempo))
    alista = ano - tempo
    print('Seu alistamento deveria ser no ano {}' .format(alista))
'''
'''
#40

print('Vamos calcular a media de duas notas')

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

calcula_n = (n1 + n2) / 2

if calcula_n < 5:
    print('\033[31mReprovado')

elif calcula_n == 5 or calcula_n <= 6.9:
    print('\033[33mRecuperação')

else:
    print('\033[32mAprovado')
'''

'''
#41
import datetime

print('vamos descobrir a categoria do atleta')
cores = {'vermelho' : '\033[31m',
'amarelo': '\033[33m', 'verde' : '\033[32m', 'limpa' : '\033[m'}

ano_n = int(input('Qual o ano de nacsimento do atleta: '))
ano_at = datetime.date.today().year

idade = ano_at - ano_n

if idade <= 9:
    print('A tualmente o atleta tem {}{}{} anos'
    '\nSua Categogia atual é MIRIM'. format(cores['verde'], idade, cores['limpa']))

elif idade > 9 and idade <= 14:
    print('A tualmente o atleta tem {}{}{} anos'
    '\nSua Categogia atual é Infantil'. format(cores['verde'], idade, cores['limpa']))

elif idade > 14 and idade <=19:
    print('A tualmente o atleta tem {}{}{} anos'
    '\nSua Categogia atual é Junior'. format(cores['amarelo'], idade, cores['limpa']))

elif idade == 20:
    print('A tualmente o atleta tem {}{}{} anos'
    '\nSua Categogia atual é Sênior'. format(cores['vermelho'], idade, cores['limpa']))
else:
    print('A tualmente o atleta tem {}{}{} anos'
    '\nSua Categogia atual é Master'. format(cores['vermelho'], idade, cores['limpa']))

'''
'''
#42

print('analisando 3 seguimentos de reta e vendo se eles formam um triangulo'
'\ne definindo o seu tipo')

r1 = float(input('Informe o primeiro seguimento: '))
r2 = float(input('Informe o segundo seguimento: '))
r3 = float(input('Informe o terceiro seguimento: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 +r2:
    print('Formam um triangulo:')

    if r1 == r2 == r3:
        print('Equilátero')

    elif r1 != r2 != r3 != r1:
        print('Escaleno')
    
    else:
        print('Isósceles')

else:
    print('Os seguimentos acima não podem formar um triangulo')

'''
'''
#43

print('Vamos Calcular o seu IMC')

altura = float(input('Qual a sua Altura: '))
peso = float(input('Qual o seu peso atual: '))

calcula = peso / (altura * altura)

if calcula <= 18.5:
    print('Seu IMC é {:.2f}'
     '\nVocê está abaixo do Peso' .format(calcula))
     
elif calcula == 18.6 or calcula <= 25:
    print('Seu IMC é {:.2f}'
    '\nPeso ideal' .format(calcula))

elif calcula == 25.1 or calcula <= 30:
    print('Seu IMC é {:.2f}'
    '\nSobrepeso' .format(calcula))

elif calcula == 30.1 or calcula <= 40:
    print('Seu IMC é {:.2f}'
    '\nObesidade' .format(calcula))

elif calcula > 40.1:
    print('Seu IMC é {:.2f}'
    '\nObesidade mórbida' .format(calcula))

'''

'''
#44

print('Calculando preço do produto')

produto = float(input('Qual o valor do produto: R$ '))
print(('Escolha uma das forma de pagamento:
1 - À Vista Dinheiro / Cheque;
2 - À Vista no cartão;
3 - Cartão parcelado.'))
print('Digite (1, 2 ou 3) abaixo para escolher a opção desejada.')

forma_pagamento = int(input('Qual a forma de pagamento: '))

if forma_pagamento == 1:
    desconto = produto * 0.1
    novo_valor = produto - desconto
    print('O valor do produto é R${}'
    '\nPagando à vista você ganha R${}'
    '\nO valor com o desconto é R${}' .format(produto, desconto, novo_valor))

elif forma_pagamento == 2:
    desconto = produto * 0.05
    novo_valor = produto - desconto
    print('O valor do produto é R${}'
    '\nPagando à vista você ganha R${}'
    '\nO valor com o desconto é R${}' .format(produto, desconto, novo_valor))

elif forma_pagamento == 3:
    parcelas = int(input('Escolha a quantidade de parcelas: '))
    valor_parcela = produto / parcelas
    if parcelas <= 2:
        print('O valor do produto é R$ {}'
        '\nO valor da parcela é R$ {}' .format(produto, valor_parcela))
    elif parcelas >=3:
        juros = produto * 0.2
        novo_valor = produto + juros
        print('O valor Original do produto é R${}'
        '\nDevido ao parcelamento serão cobrados R${} de juros'
        '\nO falor final é R${}' .format(produto, juros, novo_valor)) 
else:
    print('item informado é invalido')
'''
'''
#45

import random

print('Vamos jogar jokempô')
opção = ['PEDRA', 'PAPEL', 'TESOURA']
Escolha = random.choice(opção)

print('Escolha entre Pedra, Papel ou Tesoura'
'\nEm quanto Você escolhe o PC também vai escolher!')
escolha_user = str(input('Digite a sua opção: ')).upper()

print('O PC escolheu {}!'
'\nVocê escolheu {}!' .format(Escolha, escolha_user))

if escolha_user == Escolha:
    print('Empatou')

elif escolha_user != Escolha:
    if escolha_user == 'PEDRA' and Escolha == 'TESOURA':
        print('Você Ganhou')
    
    elif escolha_user == 'PEDRA' and Escolha == 'PAPEL':
       print('O PC ganhou') 
    
    elif escolha_user == 'PAPEL' and Escolha == 'TESOURA':
        print('O PC Ganhou')
    
    elif escolha_user == 'PAPEL' and Escolha == 'PEDRA':
        print('Voce ganhou')
    
    elif escolha_user == 'TESOURA' and Escolha == 'PAPEL':
        print('Você Ganhou')

    elif escolha_user == 'TESOURA' and Escolha == 'PEDRA':
        print('O PC ganhou')
else:
    print('Informação fora de parametro, digite as opções informadas acima')
'''