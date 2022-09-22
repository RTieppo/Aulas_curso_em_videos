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

