

def leia_entrada(valor):
    válido = False
    while not válido:
        entrada = str(input(valor)).replace(',','.').strip()

        if entrada.isalpha() or entrada =='':
            print(f'\033[0;31m Erro: \"{entrada}\" é uma entrada invalida!\033[m')
        else:
            válido = True
            return float(entrada)