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