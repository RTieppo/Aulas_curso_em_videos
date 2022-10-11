def metade(valor,formatar=False):
    metade = valor / 2
    return metade if formatar is False else moeda(metade)

def dobro(valor, formatar=False):
    dobra = valor *2
    return dobra if formatar is False else moeda(dobra)

def porcento (valor, formatar=False):
    aumenta = valor*0.1 + valor
    return aumenta if formatar is False else moeda(aumenta)

def menos_porcentagem(valor, formatar=False):
    diminui =  valor - valor*0.15
    return diminui if formatar is False else moeda(diminui)

def moeda(valores = 0, moeda = 'R$'):
    return f'{moeda}{valores:.2f}'.replace('.',',')

def resumo(valor):
    meio = metade(valor, True)
    dobra = dobro(valor, True)
    aumenta_10 = porcento(valor, True)
    diminui_15 = menos_porcentagem(valor, True)

    print('---'*10)
    print(f'{"RESUMO DO VALOR":.^30}')
    print('---'*10)
    print(f'Preço analisado:    {valor}')
    print(f'Dobro do preço:     {dobra}')
    print(f'Metade do preço:    {meio}')
    print(f'10% de aumento:     {aumenta_10}')
    print(f'15% de redução:     {diminui_15}')