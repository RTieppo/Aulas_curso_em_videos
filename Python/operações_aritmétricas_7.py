#ordem de precedencia
'''
1 = ()
2 = **
3 = * / // %
4 = + -

** = potencia
// =  divisão inteira
% = sobra da divisão inteira

Aula 7 dicas de print muito usaveis

'''
'''
#5
print('Vamos descobri o antecessor de um numero e o sucessor')
n = int(input('Digite o Nº: '))

print('o antecessor de {} é {}, o seu sucessor é {}.'.format(n, n-1 , n+1))
'''
'''
#6
print('Vamos descobri o dobro do numero informado o seu triplo e a sua raiz')
n = int(input('Digeto o valor desejado: '))
d = n*2
t = n*3
q = n**(1/2)
print('O dobro de {} é {} o seu triplo é {} já a sua Raiz quadrada é {:.2f}.'.format(n, d, t, q))
'''
'''
#7
print('vamos calcular a media de um aluno, usando duas notas como base')
n1 = int(input('Digite a primeira nota:'))
n2 = int(input('Digite a segunda nota:'))

m = (n1+n2)/2

print('a media do aluno é {}'.format(m))
'''
'''
#8
print('Vamos realizar converções de metros para centrimetro e milimetros')
m = int(input('Quantos Metros você quer converter: '))

km = m/1000
hm = m/100
dam = m/10
dm = m*10
cm= m*100
mm = m*1000

print('A conversão de {}M para cm é {}'.format(m, cm))
print('A conversão de {}M para mm é {}'.format(m, mm))
print('A conversão de {}M para km é {}'.format(m, km))
print('A conversão de {}M para hm é {}'.format(m, hm))
print('A conversão de {}M para dam é {}'.format(m,dam))
print('A conversão de {}M para dm é {}'.format(m,dm))
'''
'''
#9
print('Hora da Tabuada')
n = int(input('Digite o numero inteiro: '))

print('A tabuada de {} é'.format(n))
print(' 1 x {} \n 2 x {} \n 3 x {} \n 4 x {} \n 5 x {} \n 6 x {} \n 7 x {} \n 8 x {} \n 9 x {} \n 10 x {}' .format(n*1, n*2, n*3, n*4, n*5, n*6, n*7, n*8, n*9, n*10))
'''

'''
#10
print('Conversor de moeda de R$ para $')
v = int(input('Qual o valor gostaria de realizar a converção R$: '))

d = 5.27
c = v/d

print('O valor atual do dolar é R${} \nAtualmente o valor que você tem disponivel é ${:.2f}' .format(d,c))
'''
'''
#11
#conversor de litros em tinta

print('Vamos descobrir quantos litros de tinta vai ser usado para pintar a sua parede')

l = float(input('Qual a largura da parede? '))
a = float(input('Qual a altura da parede? '))

ar= l*a
t= ar/2

print('A area total da pardede é {}m²\nA tinta usada para essa pintura tem uma cobertura de 2m² por litro \nVocê vai precisar de {} litros para essa pintura' .format(ar, t))
'''
'''
#12
#calculando desconto

print('Dia de promoção')

valor_produto = int(input('Qual o valor do produto R$: '))
valor_desconto = int(input('Qual a % do desconto: '))

converte_desconto = valor_desconto/100

aplica_desconto = 1.0 - converte_desconto

valor_promo = valor_produto*aplica_desconto

print('O valor final com desconto é R$:{}' .format(valor_promo))
'''
'''
#13
# Aumento de salario por %

print('Vamos calcular o aumento de salario conforme % informada')

salario = float(input('Digite o salario base: '))
aumento = float(input('informe a % do aumento: '))

conversor_porcentagem = aumento/100

aplica_aumento = 1 + conversor_porcentagem

salario_final = salario*aplica_aumento

print('O salario com o aumento ficara R$:{}' .format(salario_final))
'''

'''
#14
#conversor de graus

print("Vamos converter ºC em fahrenheit")
g_c = float(input('Informe a temperatura em ºC: '))

fa = (g_c * 9/5) + 32

print('{}°C corresponde a {}°F!' .format(g_c, fa))
'''
'''
#15
#Aluguem de carro

print('Vamos definir o valor de aluguel de um carro')
d = float(input('Por quantos dias ele vai ser alugado? '))
k = float(input('Quantos kms vão ser rodados? '))

valor_dia = d*60
valor_km_rodado = k*0.15

print('Dias alugado: {} \nPrevisão de Km Rodado {}\nValor previsto do aluguel:R${:.2f}' .format(d, k, (valor_dia+valor_km_rodado)))
'''