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
