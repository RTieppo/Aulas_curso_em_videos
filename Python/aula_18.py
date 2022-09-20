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