#desafio1
'''
nome_user = input('Qual o seu nome?')
print('olá',nome_user,'Prazer')
'''
'''
#desafio2
dia = input('Qual dia você nacseu?')
mes = input('Qual mes você nasceu?')
ano = input('Qual ano você nasceu?')
print('você nasceu dia',dia,'de',mes,'de',ano,'. Correto?')
'''

'''
#desafio3

n1 = int (input('informe um numero: '))
n2 = int (input('informa segundo numero: '))
soma = n1+n2
print(soma)
'''
'''
n1 = int (input('informe um numero: '))
n2 = int (input('informa segundo numero: '))
soma = n1+n2
print('a soma entre {} e {} vale {}'.format(n1,n2,soma))
'''
'''
n1 = input('Digite alguma coisa: ')
print(n1.isnumeric())
print(n1.isdecimal())
'''
'''
n1 = float(input('informe um numero: '))
n2 = float(input('informa segundo numero: '))
s = n1 + n2
print('a soma entre {} e {} vale {}'.format(n1,n2,s))
'''

info = input('Digite alguma coisa: ')
print('o tipo primitivo dessa valoe é', type(info))

print('Só tem espaços?', info.isspace())

print('é um número?', info.isnumeric())

print('é alfabético?', info.isalpha())

print('é alfanumerico?', info.isalnum())

print('está em maiusculas?', info.isupper())
print('está minusculas?', info.islower())
print('está capitalizada?', info.istitle())