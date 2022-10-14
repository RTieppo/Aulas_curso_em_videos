
def linha():
    return '---'*10

def leia_int(num):
    while True:
        try:
            analise = int(input(num))

        except ValueError:
            print('\033[31mERRO! Valor não é valido.\033[m')
        
        except KeyboardInterrupt:
            print('\033[31mUsuario preferiu não continuar\033[m')

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

    while True:
        pasta = os.listdir(r'C:\Users\Public')

        if 'cadastro' in pasta:
            ark = os.listdir(r'C:\Users\Public\cadastro')
            if 'ark.txt' in ark:
                return 'Arquivo encontrado'

            else:
                cria_txt = open(r'C:\Users\Public\cadastro\ark.txt','w', encoding='UTF-8')
                cria_txt.write('')
                cria_txt.close()
                return 'Arquivo criado.'
            
        else:
            os.makedirs(r'C:\Users\Public\cadastro')

def leitor_ark():
    l_ark = open(r'C:\Users\Public\cadastro\ark.txt', 'r', encoding='UTF-8').read()
    print(l_ark)

def cadastra_pesoas():
    while True:
            nome = str(input('Nome: ').strip())
            if nome.isalpha():
                grava = open(r'C:\Users\Public\cadastro\ark.txt','a',encoding='UTF-8')
                grava.write(nome)
                grava.close
                break
            else:
                print('\033[31mEntrada invalida\033[m')

    while True:
        try:
            idade = int(input('Idade: '))
        
        except ValueError:
            print('\033[31mValor invalido!\033[m')
        
        else:
            grava = open(r'C:\Users\Public\cadastro\ark.txt','a',encoding='UTF-8')
            grava.write(f' {idade}\n')
            grava.close
            cabeçalho('Nome Salvo!')
            break
