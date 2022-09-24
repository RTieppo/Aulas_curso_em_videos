 #90
# Dicionario
'''
aluno = dict()

print('==='*10)
print('Analisando situação do aluno')
print('==='*10)

aluno['nome'] = str(input('Nome: '))

aluno['media'] =  float(input(f'Media de {aluno["nome"]}: '))

if aluno['media'] >= 7:
    aluno['situação'] =  'Aprovado'

elif 5 <= aluno['media']< 7:
    aluno['situação'] = 'Recuperação'

else:
    aluno['situação'] = 'Reprovado'

print('==='*10)

print(f'- Aluno {aluno["nome"]}')
print(f'- Média do aluno é {aluno["media"]}')
print(f'- Situação: {aluno["situação"]}')
'''
'''
#91
#jogo de dados automatico

from random import randint
from time import sleep
from operator import itemgetter

jogadores = dict()
ranking = list()

print('Sortenado valores')

for joga in range(0,4):
    numero = randint(0,6)
    jogadores[f'Jogador{joga+1}'] = numero


for jogador, num in jogadores.items():
    print(f'{jogador} tirou {num} no dado.')
    sleep(0.5)

print('==='*10)

ranking = sorted(jogadores.items(),key=itemgetter(1), reverse=True)

print(f'{"== RANKING DOS JOGADORES ==":^32}')

for i, v in enumerate(ranking):
    print(f'    {i+1}º lugar: {v[0]} com {v[1]}')
    sleep(0.5)
'''

'''
#92

from datetime import date

cadastro_pessoal = dict()

cadastro_pessoal['nome'] = str(input('Nome: '))
cadastro_pessoal['ano_nasc'] = int(input('Ano de Nascimento: '))
cadastro_pessoal['n_carteira'] = int(input('Nº da carteira de trabalho (0 se não tem): '))

if cadastro_pessoal['n_carteira'] > 0:
    cadastro_pessoal['ano_contrato'] = int(input('Ano da Primeira contratação: '))
    cadastro_pessoal['salario'] = float(input('Salário Atual: R$'))

    print('==='*10)

    print(f'- Nome no cadastro : {cadastro_pessoal["nome"]}')
    print(f'- Idade atual: {date.today().year - cadastro_pessoal["ano_nasc"]}')
    print(f'- Nº da carteira: {cadastro_pessoal["n_carteira"]}')
    print(f'- Contratação realizada em {cadastro_pessoal["ano_contrato"]}')
    print(f'- Salário atual é : {cadastro_pessoal["salario"]}')
    print(f'- Para a aponsentadoriam faltam: {65 - (date.today().year - cadastro_pessoal["ano_contrato"])} anos')

else:
    cadastro_pessoal['n_carteira'] = 'Não Disponivel'
    print(f'- Nome no cadastro : {cadastro_pessoal["nome"]}')
    print(f'- Idade atual: {date.today().year - cadastro_pessoal["ano_nasc"]}')
    print(f'- Nº da carteira: {cadastro_pessoal["n_carteira"]}')
'''
'''
#93
#Cadastro de jogador de futebol

ficha_jogador = dict()
gols = list()

ficha_jogador['nome']  = str(input('Nome do Jogador: '))
partidas = int(input(f' Quantas partida {ficha_jogador["nome"]} jogou? '))

for q in range(0,partidas):
    gols.append(int(input(f'    Quantos gols ele fez na {q+1}? ')))

ficha_jogador['gols'] = gols
ficha_jogador['total'] = sum(gols)

print('==='*10)
print(ficha_jogador)
print('==='*10)

for cha,dado in ficha_jogador.items():
    print(f'O campo {cha} tem o valor {dado}')

print('==='*10)
print(f'O jogador {ficha_jogador["nome"]} jogou {len(gols)} Partidas.')

for N_P, G_P in enumerate(gols):
    print(f'    => Na partida {N_P + 1}, ele fez {G_P} gols.')

print(f'Foi um total de {ficha_jogador["total"]} gols.')
'''
'''
#94
#unindo dicionario nas listas


dados = dict()

cadastro_geral = list()

media = 0

print('Cadastro de pessoas')

while True:
    print('=='*20)
    dados['nome'] = str(input('\nNome: '))
    while True:
        sexo = str(input('Sexo: [M/F]')).upper().strip()[0]

        if sexo in 'MF':
            dados['Sexo'] = sexo
            break
        else:
            print('\nErro! por favor, digite apenas M ou F.')
    
    dados['idade'] = int(input('Idade: '))
    media += dados['idade']

    while True:
        continua = str(input('Quer continuar? [S/N]')).upper().strip()[0]

        if continua in'SN':
            cadastro_geral.append(dados.copy())
            break
        else:
            print('\nErro! por favor, digite apenas S ou N.')
    
    if continua == 'S':
        dados.clear()

    elif continua == 'N':
        break


print('===' *10)
print(f'A) Ao todo temos {len(cadastro_geral)} pessoas cadastradas.')
print(f'B) A média de idade é de {media/len(cadastro_geral):.2f} anos.')

print(f'C) As mulheres cadastradas Foram: ',end='')
for s in cadastro_geral:
    if s['Sexo'] in 'F':
        print(f'{s["nome"]} ', end='')

print('\nD) A lista de pessoas que estão acima da média é:')

for pe in cadastro_geral:
    if pe['idade'] > media/len(cadastro_geral):
        print(f'nome = {pe["nome"]}; sexo = {pe["Sexo"]}; idade = {pe["idade"]}\n')

print('<< Encerrando >>')

'''

#95
#aprimorando os dicionarios

from operator import le


ficha_jogador = dict()

gols = list()

geral_jogadores = list()

while True:
    print('==='*10)
    ficha_jogador['nome']  = str(input('Nome do Jogador: '))
    partidas = int(input(f' Quantas partida {ficha_jogador["nome"]} jogou? '))

    for q in range(0,partidas):
        gols.append(int(input(f'    Quantos gols ele fez na {q+1}? ')))
    

    ficha_jogador['gols'] = gols[:]
    ficha_jogador['total'] = sum(gols)
    
    while True:
        continua = str(input('Quer continuar? [S/N] ')).upper().strip()[0]

        if continua in 'SN':
            geral_jogadores.append(ficha_jogador.copy())
            break
        else:
            print('ERRO! Entrada invalida digite S ou N.')
    
    if continua == 'S':
        gols.clear()
        ficha_jogador.clear()

    else:
        break

print('==='*10)
print('Cod. nome    gols    Total')

#formatação de terminal no exercicio
for cod,info in enumerate(geral_jogadores):
    print(f'{cod}   {info["nome"]}  {info["gols"]}  {info["total"]}')

print('==='*10)

while True:
    infor = int(input('Mostrar dados gerais de qual jogador? (999 para parar) '))

    if infor == 999:
        print('<< Encerrando >>')
        break
    
    elif infor >= len(geral_jogadores):
        print(f'ERRO! Cod. {infor} de jogador invalido ')
    
    else:
        print(f'-- Levantamento do jogador {geral_jogadores[infor]["nome"]}:')
        
        for chave, info in enumerate(geral_jogadores[infor]['gols']):
            print(f'    No jogo {chave+1} fez {info}')
    print('==='*10)
    
