#113 

#Melhorando função
def leia_int(num):
    while True:
        try:
            analise = int(input(num))

        except ValueError:
            print('ERRO! Valor não é valido.')
        
        except KeyboardInterrupt:
            print('Usuario preferiu não continuar')
            return 0

        else:
           return analise

def leia_real(num):
    while True:
        try:
            analise = int(input(num))
        except ValueError:
            print('ERRO! Valor não é valido.')
        
        except KeyboardInterrupt:
            print('Usuario preferiu não continuar')

        
        else:
            return analise

valor_int = leia_int('Digite um valor inteiro: ')
valor_real = leia_real('Digite um valor Real: ')
print(f'O valor Inteiro foi {valor_int} e o real foi {valor_real}')


 #114
 #verifica se site está acessivel.



