# Dicionários em Python (tipo dict)
# Dicionários são estruturas de dados do tipo
# par de "chave" e "valor".
# Chaves podem ser consideradas como o "índice"
# que vimos na lista e podem ser de tipos imutáveis
# como: str, int, float, bool, tuple, etc.
# O valor pode ser de qualquer tipo, incluindo outro
# dicionário.
# Usamos as chaves - {} - ou a classe dict para criar
# dicionários.
# Imutáveis: str, int, float, bool, tuple
# Mutável: dict, list
# pessoa = {
#     'nome': 'Felipe',
#     'sobrenome': 'Texeira',
#     'idade': 28,
#     'altura': 1.75,
#     'endereços': [
#         {'rua': 'Garibalde Veronez', 
#          'número': 96},
#         {'rua': '7 de setembro', 
#          'número': 321},
#     ]
# }

pessoa1 = dict(nome='Felipe', sobrenome='Texeira')
print(pessoa1, type(pessoa1))
print()

pessoa = {
    'nome': 'Felipe',
    'sobrenome': 'Texeira',
    'idade': 28,
    'altura': 1.75,
    'endereços': [
        {'rua': 'Garibalde Veronez', 
         'número': 96},
        {'rua': '7 de setembro', 
         'número': 321},
    ],
}

print(pessoa, type(pessoa))

print()

print(pessoa['nome'])
print(pessoa['sobrenome'])
print(pessoa['endereços'])

print()

for chave in pessoa:
    print(chave, ':', pessoa[chave])