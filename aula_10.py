#28 desafio
'''
import random


valor_aleatorio = random.randint(0,5)
print('Hora de adivinhar, o pc vai escolher um numero de 1 até e você vai tentar adivinhar')
hit = False

while hit == False:
    chute_user = float(input('Digite um numero: '))
    if chute_user == valor_aleatorio:
        hit = True
        print('Você acertou')
    elif chute_user < valor_aleatorio:
        print('Chute mais alto')
    elif chute_user > valor_aleatorio:
        print('Chute um valor mais baixo')
'''

'''
#29 calculando uma multa

velo_max = 80
valor_multa = 7

print('Vamos verificar se você ganhou multa')
velocidade = float(input('Digite a velocidade do veiculo KM/h:  '))

if velocidade > velo_max:
    diferença = (velocidade - velo_max) * valor_multa
    print('Você foi multado \nO valor da multa é {} por KM/h a mais \nO total da sua multa é R${}'.format(valor_multa, diferença))


elif velocidade <= velo_max:
    print('Você não foi multado')
'''

'''
#30

print('Vamos descobri se um numero é impar ou par')

numero = float(input('Digite qualuqer numero:'))

if numero%2:
    print('Ímpar')
else:
    print('Par')

'''
  
'''
#31

print('Vamos calcular o valor da sua viagem')

distancia = float(input('Informe quantos a estimativa de KM para essa Viagem: Km '))

if distancia <=200:
    valor_distancia = distancia * 0.5
    print('O valor da sua viagem vai ser R${:.2f}' .format(valor_distancia))

else:
    valor_distancia = distancia * 0.45
    print('O valor da sua viagem vai ser R${:.2f}' .format(valor_distancia))
'''

'''
#32
import datetime

print( 'Vamos ver se o ano é Bissexto')

ano = float(input('informe o ano: '))

if ano == 0:
    ano = datetime.date.today().year

if (ano%4==0 and ano%100!=0) or (ano%400==0):
    print('Bissexto')

else:
    print('Não é bissexto')
'''
'''
#33

print('indentificado o numero maior e o menor entre 3 numeros')

N1 = float(input('Digite o primeiro Nª: '))
N2 = float(input('Digite o segundo Nª: '))
N3 = float(input('Digite o terceiro Nª: '))

if (N1 > N2) and (N1 > N3):
    print('O maior é {}'.format(N1))
elif (N2 > N1) and (N2 > N3):
    print('O maior é {}'.format(N2))
elif (N3> N1) and (N3 > N2):
    print('O maior é {}'.format(N3))


if (N1 < N2) and (N1 < N3):
    print('O menor é {}'.format(N1))
elif (N2 < N1) and (N2 < N3):
     print('O menor é {}'.format(N2))
elif (N3 < N1) and (N3 < N2):
    print('O menor é {}'.format(N3))
else:
    print('Todos são iguais')
'''
'''
#34

print('Vamos calcular o aumento do salario com base no valor já recebido hoje')

valor = float(input('Qual o valor do seu salario: R$'))

P1 = valor * 0.10 + valor
P2 = valor * 0.15 + valor

if valor >= 1250:
    print('O seu novo salario é {:.2f}'.format(P1))
else:
    print('O seu novo salario é {:.2f}' .format(P2))
'''
'''
#35

print('analisando 3 seguimentos de reta, vendo se eles formam um triangulo')

r1 = float(input('informe o primeiro seguimento: '))
r2 = float(input('informe p segundo seguimento: '))
r3 = float(input('informe o terceiro seguimento: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os seguimentos acima podem formar um triangulo')
else:
    print('Os seguimentos acima não podem formar um triangulo')
    '''
