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