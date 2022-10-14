#115
#sistema de cadastro e consulta de cadastro ja criados

from modulos_aula_115 import *
from time import sleep

while True:
    resposta_user = menu(['Ver pessoa cadastrada','Cadastrar nova Pessoa', 'Sair do Sistema'])

    if resposta_user == 1:
        cabeçalho('Opção 1')
    
    elif resposta_user == 2:
        cabeçalho('Opção 2')
    
    elif resposta_user == 3:
        cabeçalho('Opção 3')
        break

    else:
        print('\033[31mERRO! Digite uma opção Válida!\033[m')
    
    sleep(2)