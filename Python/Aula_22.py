#Modularização em python
''''
#107

from Modulos_aula_21 import exercicio_107

valor = float(input('Digite o preço: R$'))
print(f'A metade de R${valor} é R${exercicio_107.metade(valor)}')
print(f'O dobro de R${valor} é R${exercicio_107.dobro(valor)}')
print(f'Aumentando 10%, temos R${exercicio_107.porcento(valor)}')
'''
'''
#108
#formatando moeda

from Modulos_aula_21 import exercicio_108

valor = float(input('Digite o preço: R$'))
print(f'A metade de {exercicio_108.moeda(valor)} é R${exercicio_108.moeda(exercicio_108.metade(valor))}')
print(f'O dobro de {exercicio_108.moeda(valor)} é R${exercicio_108.moeda(exercicio_108.dobro(valor))}')
print(f'Aumentando 10%, temos R${exercicio_108.moeda(exercicio_108.porcento(valor))}')
'''
'''
#109

#Melorando função de retono

from Modulos_aula_21 import exercicio_109

valor = float(input('Digite o preço: R$'))
print(f'A metade de {exercicio_109.moeda(valor)} é {exercicio_109.metade(valor,True)}')
print(f'O dobro de {exercicio_109.moeda(valor)} é {exercicio_109.dobro(valor,True)}')
print(f'Aumentando 10%, temos: R${exercicio_109.porcento(valor,True)}')
print(f'Reduzindo o valor em 15%, temos: {exercicio_109.menos_porcentagem(valor,True)}')
'''

'''
#110
#Reduzindo ainda mais seu programa

from Modulos_aula_21 import exercicio_110

valor = float(input('Digite o preço: R$'))
exercicio_110.resumo(valor)
'''
'''
#111
#ajustando modulos

from Modulos_aula_21.utilidades_cv import moeda

valor = float(input('Digite o preço: R$'))
moeda.resumo(valor)

'''