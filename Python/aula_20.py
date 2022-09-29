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

