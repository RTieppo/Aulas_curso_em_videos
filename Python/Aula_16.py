#dica de aplicação do for na tupla em 31:57 minutos da aula 16


#72
'''
print('Vamos escrever um numero')

nome = ('zero', 'um', 'dois', 'Trés', 'Quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
'onze', 'doze', 'treze', 'Quatroze', 'quinze', 'dezeseis', 'desesete', 'dezoito', 'dezenove', 'vinte')

#versão corrigida mais desafio extra

while True:
    valor_usuario = int(input('Digite um valor entre 0 e 20: '))
    if 0 <= valor_usuario <=20:
        print(f'Você Digitou: {nome[valor_usuario]}')
        break
    print('Tente novamente. ', end='')
while True:
    continuar = str(input(f'Quer continuar [Sim/Não]: ')).upper().strip()
    if continuar[0] == 'N':
        print('Obrigado! Até breve!')
        break
    elif continuar[0] == 'S':
        novo_valor = int(input('Digite um valor entre 0 e 20: '))
        print(f'Você Digitou: {nome[novo_valor]}')
    else:
        print('Tente novamente. ', end='')
'''

'''
#Minha versão
while True:
    valor_usuario = int(input('Digite um valor entre 0 e 20: '))

    if valor_usuario > 20:
        print('Valor invalido! ', end='')
    
    elif valor_usuario < 0:
        print('Valor invalido! ', end='')
    
    else:
        print(f'Você Digitou: {nome[valor_usuario]}')
        break
'''

'''
#73

print('Apresentando Tabela brasileirão')

Times = ('Palmeiras', 'Corinthians', 'Fluminense', 'Atlético Paranaense', 'Flamengo', 'Internacional',
'Atlético Mineiro', 'Red Bull Bragantino', 'Santos', 'América', 'São Paulo', 'Botafogo', 'Goiás EC GO', 'Ceará',
'Coritiba', 'Avaí', 'Fortaleza-CE', 'Cuiaba Esporte Clube MT', 'Atlético Goianiense', 'EC Juventude RS')
 
print('\n','=-=' * 20)
print('\n{:^60}\n'.format('Os 5 primeiros na tabela são:'))

for primeiros in range(0,5):
    print(Times[primeiros])

print('\n','=-=' * 20)
print('\n{:^60}\n'.format('4 ultimos na tabela são:'))

for ultimos in range(19,15,-1):
    print(Times[ultimos])

print('\n','=-=' * 20)
print('\n{:^60}\n'.format('Os times em ordem alfabética:'))

for ordem in sorted(Times):
    print(ordem)

print('\n','=-=' * 20)
print(f'o Avaí está na {Times.index("Avaí")+1}º posição')
'''

'''
#74
import random
maior = menor = 0

print('Os valores escolhidos foram: ', end = '')

for numero in range(0,5):
    sorteio = int(random.randint(0, 10))
    print(sorteio, end=' ')


    if numero == 0:
        maior = sorteio
        menor = sorteio
    
    else:
        if sorteio > maior:
            maior = sorteio
        
        if sorteio < menor:
            menor = sorteio

print(f'\nO maior valor sorteado foi: {maior}')
print(f'O menor Valor sorteado Foi: {menor}')
'''
'''
#75

numeros = (int(input('Digite um Nº: ')), int(input('Digite outro Nº: ')),
int(input('Digite mais um Nº: ')), int(input('Digite o ultimo Nº: ')))

print(f'O valo 9 apareceu {numeros.count(9)} vezes;')

if 3 in numeros:
    print(f'O valor 3 apareceu na {numeros.index(3)+1}ª posição;')
else:
    print('O valor 3 não foi digitado')

print(f'Os Valores pares digitados foram:')

for n in numeros:    
    if n %2 == 0:
        print(n, end=' ')
'''
'''
#76

listagem = ('Lapis', 1.75, 'Borracha', 2, 'caderno', 15 , 'Mochila', 50 , 'estojo', 5)

print('-'*40)
print(f'{"Listagem de preços":^40}')
print('-'*40)

for local in range(0,len(listagem)):
    if local %2 == 0:
        print(f'{listagem[local]:.<30}', end='')
    
    else:
        print(f'R${listagem[local]:>7.2f}')
print('-'*40)
'''
'''
#77

palavras = ('Eu', 'Casa', 'Livro', 'Nadas', 'Andar', 'Morder', 'Morrer', 'Roleta', 'Russa')

for palavra in palavras:
    print(f'\nNa palavra {palavra.upper()} temos ', end='')
    for letra in palavra:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')

'''