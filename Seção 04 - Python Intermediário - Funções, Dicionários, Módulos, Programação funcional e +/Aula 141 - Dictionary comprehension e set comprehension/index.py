import pprint

def mostrar(valor):
    pprint.pprint(valor, sort_dicts=False,  width=40)
    print()

# Dictionary Comprehension e Set Comprehension
produto = {
    'nome': 'Caneta preta',
    'preco': 2.5,
    'categoria': 'Escritório',
}
mostrar(produto.items())

for chave, valor in produto.items():
    print(chave, valor)
print()

novo_dicionario = {
    chave: valor
    if isinstance(valor, (int, float)) else valor.upper()
    for chave, valor in produto.items()
}
mostrar(novo_dicionario)

novo_dicionario = {
    chave: valor.upper()
    if isinstance(valor, str) else valor
    for chave, valor in produto.items()
}
mostrar(novo_dicionario)

novo_dicionario = {
    chave: valor.upper()
    if isinstance(valor, str) else valor
    for chave, valor in produto.items()
    if chave != 'categoria'
}
mostrar(novo_dicionario)

lista = [
    ('chave1', 'valor1'),
    ('chave2', 'valor2'),
    ('chave3', 'valor3'),
]
novo_dicionario = {
    chave: valor
    for chave, valor in enumerate(lista)
}
mostrar(dict(novo_dicionario))

novo_dicionario = {
    chave: valor
    for chave, valor in lista
}
mostrar(dict(novo_dicionario))

set_comprehension = {2 ** i for i in range(10)}
mostrar(set_comprehension)
mostrar(set(range(10)))