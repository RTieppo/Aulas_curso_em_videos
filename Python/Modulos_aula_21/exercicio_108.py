def metade(valor):
    metade = valor / 2
    return metade

def dobro(valor):
    dobra = valor *2
    return dobra

def porcento (valor):
    aumenta = valor*0.1 + valor
    return aumenta

def moeda(valores = 0, moeda = 'R$'):
    return f'{moeda}{valores:.2f}'.replace('.',',')
