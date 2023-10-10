numero_nfe = 15485
serie_nfe = 1
tomador_nfe = 'Felipe Texeira'

def valor_total_nfe(lista_item_valor):
    valor_total = 0

    for item_valor in lista_item_valor:
        valor_total += item_valor
    
    return valor_total

def monta_dados_nfe(lista_item_valor):
    return {
        'numero_nfe': numero_nfe,
        'serie_nfe': serie_nfe,
        'tomador_nfe': tomador_nfe,
        'valor_total_nfe': valor_total_nfe(lista_item_valor)
    }

""" 
    MUITO INTERESSANTE: Eu mudei o nome aqui com F2, ou seja, mudei o 
    nome na pasta 'raiz', como estando na pasta raiz e sendo importado
    em outros lugares, ele sabe onde fica a origem, com isso acaba
    alterando também em todos os lugares onde está sendo usado
"""
#
mudei_nome_f2_modulo_1 = 'Teste'