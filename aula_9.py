'''
frase = 'curso em video py'
print(frase[3:])
'''
'''
#22
#Opção 1
print('Desmenbrando uma string')

nome = str(input('Qual o seu nome completo? ')).strip()

integra = nome.split()
integra2 = ''.join(integra)

print(nome.lower())
print(nome.upper())
print(len(integra2))
print(len(integra[0]))
'''
'''
#22
#opção 2

nome = str(input('Digite seu nome completo: ')).strip()
separa = nome.split()
junta_e_tira_espaço_do_meio = ''.join(separa)
print('Analisando seu nome...')

print('Seu nome em maiúsculas é {}' .format(nome.upper()))
print('Seu nome em minúsculas é {}' .format(nome.lower()))
print('Seu nome tem ao todo {} letras' .format(len(junta_e_tira_espaço_do_meio)))
print('Seu primeiro nome é {} e ele tem {} letras' .format(separa[0], len(separa[0])))
'''
'''
#23

print('vamos desmembar um numero de 0 até 9999')

numero = int(input('Digite um numero de 0 até 9999: '))

u = numero // 1 % 10
d = numero // 10 % 10
c = numero // 100 % 10
m = numero // 1000 % 10

print('A unidade é: {}'.format(u))
print('A dezena é: {}'.format(d))
print('A centena é: {}'.format(c))
print('O milhar é: {}'.format(m))
'''
'''
#24

print('vamos verificar se o nome da cidade começa com santo')

nome = str(input('Digite o nome da cidade: '))
minuscula = nome.lower()
divide = minuscula.split()

print('santo' in divide[0])
'''
'''
#25
print('Vamos descobrir se o nome tem silva em seu nome')

nome = str(input('Digite o nome de usuario: '))

print('seu nome tem silva? {}'.format('silva' in nome.lower()))
'''
'''
#26
print('Vamos mostrar quantas vezes a letra a Aparece em uma frase')

#Quantas vezes ela aparece
#primeira possição que ela aparece
#segunda possição que ela aparece

frase = str(input('Escreva uma frase: ')).lower().strip()

print('Existem {} letras a' .format(frase.count('a')))
print('O a Aparece na possição {} na primeira vez.' .format(frase.find('a')))
print('A ultima possição do a é {}' .format(frase.rfind('a')))
'''
'''
#27

print('Vamos desmembra um nome')

nome = str(input('Digite o seu nome completo: ')).strip()
nome_divide = nome.split()

print('Oie, prazer em te conhecer!')
print('Seu primeiro nome é {}'.format(nome_divide[0].upper()))
print('Seu ultimo nome é {}'.format(nome_divide[len(nome_divide)-1]))

'''
