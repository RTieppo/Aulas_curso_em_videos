#aula 8 inportação de modulos e dicas para arendodamento

'''
import math

num = int(input('Digite um número: '))
raiz = math.sqrt(num)

print('A raiz de {} é igual a {:.2f}' .format(num, raiz))
'''

'''
#16
import math

print('Vamos mostra somente o numero inteiro de uma variavel')

num = float(input('Digite um valor Flutuante: '))

print('O Nº {} tem como sua parte inteira {}.' .format(num, math.trunc(num)))
'''
'''
#17
#opção 1:

print('Vamos calcular o comprimento da hipotenusa')

cateto_adjacente = float(input('Digite o valor do cateto_adjacente: '))
cateto_oposto = float(input('Digite o valor do cateto oposto: '))

soma_catetos = cateto_adjacente ** 2 + cateto_oposto ** 2
hipotenusa = soma_catetos ** (1/2)

print('-' * 50)
print('A hipotenusa do triangulo é {}' .format(hipotenusa))

#opção 2: import math / hi= math.hypoy(cateto_adjacente, hipotenusa) 
'''

'''
#18
import math
print('Calculando seno, cosseno e tangente') 
angulo = float(input('Digite o angulo: '))

seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))


print('O angulo de {}° \nTem como seu Seno: {:.2f}; \nSeu cosseno é {:.2f}; \n já a sua tangente é {:.2f}.'.format(angulo, seno, cosseno, tangente))
'''

'''
#19
import random

print('Escolhendo um aluno para apagar o quadro')

a1 = input('Aluno 1: ')
a2 = input('Aluno 2: ')
a3 = input('Aluno 3: ')
a4 = input('Aluno 4: ')

alunos = [a1, a2, a3, a4]
escolha = random.choice(alunos)

print('O aluno escolhido foi:  {}!' .format(escolha))
'''

'''
#20
import random
print('vamos definir a ordem de apresentação')

a1 = input('Aluno1: ')
a2 = input('Aluno2: ')
a3 = input('Aluno3: ')
a4 = input('Aluno4: ')

alunos = [a1, a2, a3, a4]
embaralhar = random.shuffle(alunos)

print('A ondem é {}'.format(alunos))
'''

'''
#21

import pygame

pygame.mixer.init()
pygame.init()
pygame.mixer_music.load('1.mp3')
pygame.mixer_music.play(loops=2, start=0.5)
pygame.event.wait()
'''