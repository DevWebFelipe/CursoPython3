print(f'Você importou {__name__}')

# qualquer coisa daqui, vai ficar disponível no package

def dobrar_valor(x):
    return x * 2

from .modulo_1 import numero_nfe, tomador_nfe, monta_dados_nfe, mudei_nome_f2_modulo_1