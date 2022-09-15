#78
'''
numero = list()

for posicao in range(0,5):
    numero.append(int(input(f'Digite um valor para a Posição {posicao}: ')))

for N in numero:
    print(N, end=' ')

print(f'\nO maior valor digitado foi {max(numero)} nas posições ', end='')

for P, N in enumerate(numero):
    if N == max(numero):
        print(f'{P}...', end='')

print(f'\nO menor numero digitadoi foi {min(numero)} nas posições ', end='')

for po, nu in enumerate(numero):
    if nu == min(numero):
        print(f'{po}...' , end='')

'''
'''
#79

lista = list()
resposta = ''

while True:
    if resposta == 'N':
        break

    numero = (int(input('Digite um valor: ')))
    
    if numero in lista:
        print('Valor duplicado! Não foi adicionado...')
    
    else:
        lista.append(numero)
        print('Valor adicionado com sucesso...')
    
    while True:

        pergunta = str(input('Quer continuar? [S/N]: ')).upper().strip()
        if pergunta[0] == 'N':
            resposta = pergunta[0]
            break

        elif pergunta[0] == 'S':
            break
        
        else:
            print('entrada invaloda ')

print('Você digitou os valores: ', end=' ')
for n in sorted(lista):
    print(n, end=' ')
'''
'''
#80

lista = list()

for perguntas in range(0,5):
        numero = int(input('Digite um valor: '))
        if perguntas == 0 or numero > lista[-1]:
            lista.append(numero)
            print('Adicionado ao final da lista...')
        else:
            pos = 0
            while pos < len(lista):
                if numero <= lista[pos]:
                    lista.insert(pos, numero)
                    print(f'Adicionado na posição {pos} da lista...')
                    break
                pos += 1
print('-=' *30)
print(f'Os valores digitados em ordem foram {lista}')

'''
'''
#81

lista = list()
conta = 0
para = ' '

while True:
    if para == 'N':
        break
    else:
        lista.append(int(input('Digite um valor: ')))
        conta += 1

        while True:
            pergunta = str(input('Quer continuar? [S/N] ')).upper().strip()
            if pergunta[0] == 'S':
                break
            elif pergunta[0] == 'N':
                para = pergunta[0]
                break
            else:
                print('Valor invaido!')

print('-='*30)
print(f'Você digirou {conta} valores')
print('Os valores digitados em ordem decrescente são: ', end=' ')

lista.sort(reverse = True)
for valores in lista:
    print(valores, end=' ')

if 5 in lista:
    print(f'\nO valor 5 faz parte da lista e está nas posiçãos: ', end=' ')
    for p,n in enumerate(lista):
        if n == 5:
            print(f'{p}', end= ' ')
        
else:
    print('\nO valor 5 não foi encontado na lista')


'''
'''
#82

lista = list()

parar = ' '

while True:
    if parar == 'N':
        break
    else:
        lista.append(int(input('Digite um número: ')))

        while True:
            pergunta = str(input('Quer continuar? [S/N]')).upper().strip()

            if pergunta[0] == 'S':
                break
            elif pergunta[0] == 'N':
                parar = pergunta[0]
                break
            else:
                print('Valor invalido')

print('A lista completa é ', end='')
for n in lista:
    print(n, end=' ')

print('\nA lista de pares é ', end='')
for pares in lista:
    if pares %2 == 0:
        print(pares, end=' ')

print('\nA lista de ímpares é ', end='')
for inpares in lista:
    if inpares %3 == 0:
        print(inpares, end=' ')
'''
'''
#83

expressao = str(input('Digite a expressão: '))
pilha = list()

for simbolo in expressao:
    if simbolo == '(':
        pilha.append('(')
    elif simbolo == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão é valida')
else:
    print('Sua expressão é invalida')
'''