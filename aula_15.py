# aula 15 fstr dicas de formatação
# print com 20 espaços = {:20}, alinhamento c {:^}, centralizado com complemento {:-^20}, < alinhamento a esquerda > direita.

'''
#66
print('somando varios valores do loop')

conta = soma = 0

while True:
    n = int(input('Digite um valor (999 para parar): '))
    if n == 999:
        break
    conta += 1
    soma += n

print(f'A soma dos {conta} valores foi {soma:.2f}!')
'''

'''
#67

print('Tabuada infinita')

while True:

    print('=-='*20)
    n = int(input('Quer ver a tabuada de qual valor? '))

    if n < 0:
        break
    print('=-='*20)

    for conta in range(1,11):
        print(f'{n} x {conta} = {n*conta}')

print('=-='*20)
print('Fim do programa')
'''
'''
#68
from random import randint

print('=-=' *20)
print('VAMOS JOGAR PAR OU ÍMPAR \nMelhor de 3')
print('=-='*20)

conta_p = conta_J =  0

while True:
    soma_con = conta_J + conta_p
    if soma_con < 3:
        
        n_pc = int(randint(1,10))
        n_jogador = int(input('Digite um valor: '))
        Pergunta1 = str(input('Par ou ímpar? [P/I]: ')).upper().strip()[0]
        print('---'*20)

        soma = n_pc + n_jogador
        
        print(f'Você jogou {n_jogador} e o computador {n_pc}. total de {soma} ', end='')

        if Pergunta1 == 'P':

            if soma %2 == 0:
                print('DEU PAR')
                print('---'*20)
                print('Você Ganhou!')
                conta_J += 1
            
            else:
                print('DEU ÍMPAR')
                print('---'*20)
                print('Você PERDEU!')
                conta_p += 1
        
        elif Pergunta1 == 'I':
            if soma %2 != 0:
                print('DEU ÍMPAR')
                print('---'*20)
                print('Você Ganhou!')
                conta_J += 1
            
            else:
                print('DEU PAR')
                print('---'*20)
                print('Você PERDEU!')
                conta_p += 1

    else:
        break

print('=-='*20)
print(f'Game over! você venceu {conta_J} vezes.')
'''
'''
#69

print('Vamos cadastrar um serumaninho')

conta_maior = conta_hom = conta_mul_menor = 0
while True:

    print('----'*20)
    print('Cadastre uma pessoa')
    print('----'*20)

    idade = int(input('Idade: '))
    if idade > 18:
        conta_maior += 1

    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).upper().strip()[0]
        if sexo == 'M':
            conta_hom += 1

        elif sexo == 'F' and idade < 20:
            conta_mul_menor += 1
        else:
            print('Digite [M/F]')

    print('----' *20)

    Continuar = ' '
    while Continuar not in 'SN':
        Continuar = str(input('Quer continuar? [S/N] ')).upper().strip()[0]

        if Continuar == 'S':
            pass
        elif Continuar == 'N':
            break
        
        else:
            print('Digite [S/N]')


print(f'Total de pessoas com mais de 18 anos: {conta_maior}')
print(f'Ao todo temos {conta_hom} homens cadastrados.')
print(f'E temos {conta_mul_menor} com menos de 20 anos.')

'''
'''
#70

print('Avaliando compras de produto')

nome = 'LOJA SUPER BARATÃO'

print('---'*20)
print(f'{nome:^50}')
print('---'*20)

contador_m_1000 = soma_produtos = valida_menor_valor = menor = 0

grava_produto = ' '

while True:

    nome = str(input('Nome do produto: '))
    valor = int(input('Preço: R$ '))

    valida_menor_valor += 1
    soma_produtos += valor

    if valor > 1000:
        contador_m_1000 += 1
    
    if valida_menor_valor == 1 or valor < menor:
        menor = valor
        grava_produto = nome

    pergunta_user = ' '

    while pergunta_user not in 'SN':
        pergunta_user = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    
    if pergunta_user == 'S':
        pass
    
    elif pergunta_user == 'N':
        break
    

fim = 'FIM DO PROGRAMA'
print(f'{fim:-^50}')

print(f'O total da compra foi R${soma_produtos:.2f}.')
print(f'Temos {contador_m_1000} Produtos custando mais de R$1000.00')
print(f'O Produto mais barato foi {grava_produto} que custa R${menor}')
'''

#71
B= 'BANCO TIEPPO'
print('=='*20)
print(F'{B:^40}')
print('=='*20)

saque = int(input('Qual valor você quer sacar? R$ '))
total = saque

cedula = 50

soma_c = 0

while True:
    
    if total >= cedula:
        total -= cedula
        soma_c += 1
    
    else:
        if soma_c > 0:
            print(f'Total de {soma_c} Cédulas de R${cedula}')
        if cedula == 50:
            cedula = 20

        elif cedula == 20:
            cedula = 10

        elif cedula == 10:
            cedula = 1
        
        soma_c = 0
        
        if total == 0:
            break