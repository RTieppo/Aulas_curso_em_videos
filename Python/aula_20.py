#Def
'''
#96
#função que calcula área

def calculo_area(l,c):
    print(f'A área de um terreno {l}x{c} é de {l*c}m².')


print ('Controle de Terreno')
print('----'*10)

calculo_area(float(input('Largura (m): ')), float(input('Comprimeto (m): ')))
'''
'''
#97

#print especial

def print_e(valor):
    print('--'*len(valor))
    print(f'{valor:^10}')
    print('--'*len(valor))

print_e(str(input('Digite o alguma coisa: ')))
'''
'''
#98
#função de contagem
from time import sleep


def contador(inicial,fim,intervalo):

    if intervalo == 0:
        intervalo = 1
    
    if intervalo < 0:
        intervalo *= -1

    if inicial < 0:
        inicial *= -1
    
    if fim < 0:
        inicial *= -1

    print('==='*10)
    print(f'Contagem de {inicial} até {fim} de {intervalo} em {intervalo}')
    
    if inicial < fim:
        for n in range(inicial,fim+1,intervalo):
            print(f'{n}', end=' ', flush=True)
            sleep(0.1)

        print('FIM!')
    
    else:
        conta = inicial
        while conta >= fim:
            print(f'{conta}', end=' ', flush=True)
            conta -= intervalo
            sleep(0.1)
        print('FIM!')



contador(1,10,1)
contador(1,10,2)

print('==='*10)
print('Sua vez:')
contador(int(input('Início: ')), int(input('Fim: ')), int(input('Passo: ')))

'''
