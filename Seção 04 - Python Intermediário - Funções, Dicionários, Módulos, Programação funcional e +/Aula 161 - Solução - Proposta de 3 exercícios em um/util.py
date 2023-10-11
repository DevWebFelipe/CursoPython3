import pprint
import copy

def imprime(valor):
    pprint.pprint(valor)
    print()

def copiar_tudo(valor):
    return copy.deepcopy(valor)

def valor_sobre_percentual(valor_base, percentual):
    return round((valor_base * percentual) / 100)

produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

def listar_resultado(resultado, mensagem):
    print('ORIGINAL')
    imprime(produtos)

    print(mensagem)
    imprime(resultado)