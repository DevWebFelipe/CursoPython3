# Introdução à List comprehension em Python
# List comprehension é uma forma rápida para criar listas
# a partir de iteráveis.
# print(list(range(10)))
lista = []
for numero in range(10):
    lista.append(numero)
# print(lista)

lista = [
    numero * 2
    for numero in range(10)
]
# print(list(range(10)))
# print(lista)

# Mapeamento de dados em list comprehension
produtos = [
    {'nome': 'p1', 'preco': 20, },
    {'nome': 'p2', 'preco': 10, },
    {'nome': 'p3', 'preco': 30, },
]

novos_produtos1 = [
    produto
    for produto in produtos
]
# O * quer dizer que estou desempacotando essa lista, aí o separador está quebrando a linha
print(f'{novos_produtos1 = }')
print(*novos_produtos1, sep='\n')
print()

# aqui to pegando somente o valor da chave nome
nome_produtos2 = [
    nome['nome']
    for nome in produtos
]
print(f'{nome_produtos2 = }')
print(*nome_produtos2, sep='\n')
print()

# aqui to pegando somente o valor da chave preco
nome_produtos3 = [
    preco['preco']
    for preco in produtos
]
print(f'{nome_produtos3 = }')
print(*nome_produtos3, sep='\n')
print()

novos_produtos4 = [ # aqui to criando um nnovo dicionário vazio para cada item do for
    {}
    for produto in produtos
]
print(f'{novos_produtos4 = }')
print(*novos_produtos4, sep='\n')
print()

novos_produtos5 = [ # aqui to criando um novo dicionario passando em uma nova chave o valor da chave nome
    {'novo_nome': produto['nome']}
    for produto in produtos
]
print(f'{novos_produtos5 = }')
print(*novos_produtos5, sep='\n')
print()

novos_produtos6 = [ # aqui to criando um novo dicionario passando em novas chaves os valores das chaves do for
# da forma como ta sendo feito aqui, tem que mapear cada item da lista PRODUTOS
    {'novo_nome': produto['nome'], 'novo_preco': produto['preco']}
    for produto in produtos
]
print(f'{novos_produtos6 = }')
print(*novos_produtos6, sep='\n')
print()

novos_produtos7 = [ # aqui estou desempacotando o meu produto dentro do novo dicionário que estou criado
    {**produto}
    for produto in produtos
]
print(f'{novos_produtos7 = }')
print(*novos_produtos7, sep='\n')
print()

novos_produtos8 = [ # aqui estou desempacotando o meu produto dentro do novo dicionário que estou criado e 
# dizendo que a chave preco do novo dicionário receberá o valor da chave preco do dcionário antigo vezes
# 1.05, que seria somar 5% a mais no valor do item
    {**produto, 'preco': produto['preco'] * 1.05}
    for produto in produtos
]
print(f'{novos_produtos8 = }')
print(*novos_produtos8, sep='\n')
print()

novos_produtos8 = [ # aqui estou desempacotando o meu produto dentro do novo dicionário que estou criado e 
# dizendo que a chave preco do novo dicionário receberá o valor da chave preco do dcionário antigo vezes
# 1.05, que seria somar 5% a mais no valor do item, mas isso, só nos produtos acima de 20 
    {**produto, 'preco': produto['preco'] * 1.05}
    # isso aqui ta fazendo o seguinte, se o preço do produto for maior que 20
    # ele vai desempacotar o produto e retornar o produto desenpacotado com a chave preco acrescendo
    # 5%, se o preco não for maior que 20, vai retornar apenas o produto desempacotado
    if produto['preco'] > 20 else {**produto} # IF Ternário
    for produto in produtos
]
print(f'{novos_produtos8 = }')
print(*novos_produtos8, sep='\n')
print()

novos_produtos = [
    f'{produto["nome"]} possui valor acima de 20 -> Valor = {produto["preco"]}'
    if produto['preco'] > 20 else f'{produto["nome"]} possui valor abaixo de 20 -> Valor = {produto["preco"]}'
    for produto in produtos
]
print(f'{novos_produtos = }')
print(*novos_produtos, sep='\n')
print()
