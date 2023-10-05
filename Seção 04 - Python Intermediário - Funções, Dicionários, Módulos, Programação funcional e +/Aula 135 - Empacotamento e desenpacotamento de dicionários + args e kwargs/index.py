# Empacotamento e desempacotamento de dicionários
a, b = 1, 2
print(a, b)

a, b = b, a
print(a, b)
print()

pessoa = {
    'nome': 'Aline',
    'sobrenome': 'Souza',
}

dict_chave1, dict_chave2 = pessoa # Retorna as chaves do dcionário
print(dict_chave1, dict_chave2)
for chave in pessoa:
    print(chave)

print()

dict_value1, dict_value2 = pessoa.values() # Retorna os valores das chaves do dicionário
print(dict_value1, dict_value2)
for value in pessoa.values():
    print(value)

print()

dict_item1, dict_item2 = pessoa.items() # Retorna os items, que seria uma tupla com chave e valor do dicionário
print(dict_item1, dict_item2)
for item in pessoa.items():
    print(item)

print()

(key1, value1), (key2, value2) = pessoa.items() 
print(key1, value1, key2, value2)
for (chave, valor) in pessoa.items():
    print(chave, valor)

print()

(key1, value1), item2 = pessoa.items() 
print(key1, value1, item2)
for (chave, valor) in pessoa.items():
    print(chave, valor, tuple((chave, valor)))

print()

pessoa = {
    'nome': 'Felipe',
    'sobrenome': 'Texeira',
}

dados_pessoa = {
    'idade': 28,
    'altura': 1.8,
}

# Extrair um dicionário dentro de outro, quer dizer que vocês estpá criando um novo dicionário a partir dos 
# dados do primeiro dicionário, o que lhe permite criar um dicionário unindo vários outros, apra extrair um 
# dicionário e criar um novo0, usa-se o asterisco duas vezes **, depois de criado o novo dicionário, 
# pode-se além de juntar mais de um outro dicionário, também criar novas chaves individuais

pessoa_completa = {**pessoa}
print(pessoa_completa)
print()

pessoa_completa = {**dados_pessoa}
print(pessoa_completa)
print()

pessoa_completa = {**pessoa, **dados_pessoa}
print(pessoa_completa)
print()

pessoa_completa = {**pessoa, **dados_pessoa, 'estado_civil': 'Casado'}
print(pessoa_completa)
print()

# *args -> Argumentos não nomeados, ao usar em uma função, quer dizer que se pode passar n argumentos
# **kwargs -> Argumentos nomeados
def mostrar_argumentos_nomeados(*args, **kwargs):
    print('Não nomeados: ', args)
    
    print(f'{kwargs = }')

    for chave, valor in kwargs.items():
        print(f'{chave, valor = }')

mostrar_argumentos_nomeados(
    1, 5, 6, 8,                        # *args -> Não nomeados
    nome='Felipe', sobrenome='Texeira' # **kwargs -> Nomeados
)
print()

mostrar_argumentos_nomeados(**pessoa_completa)
print()

configuracoes = {
    'arg1': 1,
    'arg2': 2,
    'arg3': 3,
    'arg4': 4,
}

mostrar_argumentos_nomeados(**configuracoes)

print()
# args e kwargs
# args (já vimos)
# kwargs - keyword arguments (argumentos nomeados)