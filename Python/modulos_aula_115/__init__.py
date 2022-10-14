def linha():
    return '---'*10

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

def cabeçalho(txt):
    print(linha())
    print(txt.center(30))
    print(linha())

def menu(lista):
    cabeçalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\033[33m{c}\033[m - \033[34m{item}\033[m')
        c += 1
    print(linha())
    opção = leia_int('\033[32mSua Opção: \033[m')
    return opção

def valida_arquivo():
    import os

    