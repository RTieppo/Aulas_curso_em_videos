#listas part 2
'''
 # 84

dados = list()

cadastro = list()

menor = maior = 0


print('=='*20)

print('{:^40}'.format('Cadastro de pessoas'))

print('=='*20)

print('{:^40}'.format('Insira as informaçôes'))

while True:
    dados.append(str(input('Nome: '))) 
    dados.append(float(input('Peso: ')))

    if len(cadastro) == 0:
        maior = menor = dados[1]
    
    else:
        if dados[1] > maior:
            maior = dados[1]

        if dados[1] < menor:
            menor = dados[1]

    cadastro. append(dados[:])
    novo_cadastro = str(input('Quer continuar? [S/N]')).strip().upper()[0]

    if novo_cadastro == 'S':
        print('=='*20)
        print('{:^40}'.format('Novo cadastro'))
        dados.clear()
        pass

    elif novo_cadastro == 'N':
        print('=='*20)
        break

    else:
        print('Entrada invalida Tente novamente')

print(f'Ao todo, você cadastrou {len(cadastro)} pessoas.')

print(f'O maior peso foi {maior}kg.', end='')
for p in cadastro:
    if p[1] == maior:
        print(f'{p[0]}', end=' ')

print(f'\nO menor peso foi {menor}kg. ', end='')
for p in cadastro:
    if p[1] == menor:
        print(f'{p[0]}', end=' ')

'''
'''
# 85

# coletando 7 valores e dividindo entre impar e par em ordem decrecente

valores = [[], []]

for valor in range(1,8):
    valor_user = int(input(f'Digite o {valor}º valor: '))
    
    if valor_user %2 == 0:
        valores[0].append(valor_user)

    else:
        valores[1].append(valor_user)

print('=='*20)

print('Os valores pares digitados foram: ', end='')
valores[0].sort()
for ajuste in valores[0]:
    print(ajuste, end=' ')

print('\nOs valores ímpares digitados foram: ', end='')
valores[1].sort()
for ajuste in valores[1]:
    print(ajuste, end=' ')
'''

'''
gerando matriz 3x3
#86

matriz3x3 = [[0, 0, 0], [0, 0, 0], [0, 0, 0,]]
 
for linha in range(0,3):
    for coluna in range(0,3):
        matriz3x3 [linha] [coluna] = int(input(f'Digite o valor da posição [{linha},{coluna}]: '))

print('==' *20)

print('A matrix gerada foi')

for linha in range(0,3):
    for coluna in range(0,3):
        print(f'{matriz3x3[linha][coluna]:^5}', end=' ')
    print()

'''
'''
#87

#gerando matriz 3x3 somando valores pares, somando a terceira coluna toda e vendo qual o maior valor da segunda coluna.


matriz = [[0,0,0], [0,0,0], [0,0,0]]
soma = soma_2 = compara = 0

for linha in range(0,3):
    for coluna in range(0,3):
        matriz[linha] [coluna] = int(input(f'Digite o valor da posição [{linha},{coluna}]: '))

        if matriz[linha] [coluna] %2 == 0:
            soma += matriz[linha] [coluna]

print('=='*20)
print('A matriz gerada foi: ')

for linha in range(0,3):
    for coluna in range (0,3):
        print(f'{matriz[linha] [coluna]:^5}', end='')
    print()

for linha in range(0,3):
    soma_2 += matriz[linha][2]

for maior in matriz[1]:
    if maior > compara:
        compara = maior

print(f'A soma dos valores pares foi {soma}')

print(f'A soma dos valores da 3 coluna é {soma_2}')

print(f'O maior valor da segunda linha é {compara}')
'''

'''
#88

#palpites para a mega sena

import random
from time import sleep

jogos = numeros = 0

lista_numeros = list()


print('--'*16)
print('{:^32}'.format('NUMEROS MEGA SENA'))
print('--'*16)

palpites = int(input('Quantos jogos você quer sortear? '))

print(f'Sorteando {palpites} jogos')

while jogos < palpites:
    
    while numeros < 6:
        
        sorteio = random.randint(0,60)

        if sorteio in lista_numeros:
            pass

        else:
            lista_numeros.append(sorteio)
            numeros += 1
            
    jogos += 1
    numeros = 0
    lista_numeros.sort()
    print(f'Jogo {jogos}: {lista_numeros}')
    lista_numeros.clear()
    sleep(0.5)

print('Boa sorte')
'''

#89
#boletim com listas compostas

lista_alunos = list()

print('Cadastro de notas')

while True:

    nome = str(input('Nome: ')) 
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1+nota2)/2 
    lista_alunos.append([nome,[nota1,nota2],media])

    continuar = str(input('Quer continuar? [S/N]'))

    if continuar in 'Nn':
        break
    
print('==='*10)
print(f'{"Nº":<4}{"NOME":<10}{"MÉDIA":>8}')
print('---'*10)

for indi, alu in enumerate(lista_alunos):
    print(f'{indi:<4}{alu[0]:<10}{alu[2]:>8.1f}')

while True:
    print('--'*10)

    notas = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    
    if notas == 999:
        print(' FINALIZANDO...')
        break

    if notas <= len(lista_alunos) -1:
        print(f'Notas de {lista_alunos[notas][0]} são {lista_alunos[notas][1]}')
print('<<< VOLTE SEMPRE >>>')
