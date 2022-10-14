#115
#sistema de cadastro e consulta de cadastro ja criados

from modulos_aula_115 import *
from time import sleep


verifica_cria = valida_arquivo()
print(verifica_cria)

while True:
    resposta_user = menu(['Ver pessoa cadastrada','Cadastrar nova Pessoa', 'Sair do Sistema'])

    if resposta_user == 1:
        cabeçalho('Pessoas Cadastradas')
        leitor_ark()
    
    elif resposta_user == 2:
        cabeçalho('Cadastro de Pessoa')
        cadastra_pesoas()
    
    elif resposta_user == 3:
        cabeçalho('Saindo so Programa')
        break

    else:
        print('\033[31mERRO! Digite uma opção Válida!\033[m')
    
    sleep(2)