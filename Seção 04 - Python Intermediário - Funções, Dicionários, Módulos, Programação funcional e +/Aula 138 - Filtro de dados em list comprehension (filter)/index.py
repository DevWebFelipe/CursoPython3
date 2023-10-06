# Introdução à List comprehension em Python
# List comprehension é uma forma rápida para criar listas
# a partir de iteráveis.
# print(list(range(10)))
import pprint # isso é para poder usar o pprint.pprint

def mostrar(valor):
    pprint.pprint(valor, sort_dicts=False, width=40)
# vai formatar de forma visualmente mais clara a lista que for passado ali no argumento valor

lista = [
    numero                  # NUMERO é o que vai ser inserindo na lis comprehension
    for numero in range(10) # RANGE(10) quer dizer que vai varrer do 0 ao 9
    if numero < 5           # NUMERO < 5 quer dizer que só vai inserir os NUMERO menor que 5, isso que é o filtro
]
mostrar(lista)
print()

produtos = [
    {'nome': 'p1', 'preco': 20, },
    {'nome': 'p2', 'preco': 10, },
    {'nome': 'p3', 'preco': 30, },
]

novos_produtos8 = [ 
    {**produto, 'preco': produto['preco'] * 1.05} # Isso é o que vai ser inserido
    if produto['preco'] > 20 else {**produto}     # Isso é para tratar o dado que vai ser inserido
    for produto in produtos                       # Isso varre algo para determinar o que vai ser feito com cada item desse 'algo'
    if produto['preco'] != 20                     # Isso vai determinar o que vai ser inserido na nova lista em relação ao que está sendo varrido no for
]
print(f'{novos_produtos8 = }')
print(*novos_produtos8, sep='\n')
print()