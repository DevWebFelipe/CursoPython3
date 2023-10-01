pessoa = {}

chave_nome = 'nome'
chave_lista_fones = 'fones'
chave_endereco = 'endereco'

nome = 'Felipe Texeira'
lista_fones = ['99480788', '998520116']
endereco = 'Rua Garibaldi Veronez 096'

# Adicionado chaves dinamicamente
pessoa[chave_nome] = nome
pessoa[chave_lista_fones] = lista_fones
pessoa[chave_endereco] = endereco 

print(pessoa)
print(f'{pessoa[chave_nome] = }')
print(f'{pessoa[chave_lista_fones][0] = }')
print(f'{pessoa[chave_lista_fones][1] = }')

# Para evitar quebrar o sistema caso uma chave possa ou não existir
if pessoa.get(chave_endereco) is None: # caso a chave não exista, retorna None
  print(f'Chave "{chave_endereco}" não encontrada')
else:
  print(f'{pessoa[chave_endereco] = }')

print()

# ALterando valores das chaves dinamicamente
nome = 'Giulia Gabrielle'
lista_fones = ['1111111111', '333333333']

pessoa[chave_nome] = nome
pessoa[chave_lista_fones] = lista_fones

# Deletando uma chave
del pessoa[chave_endereco]

print(pessoa)
print(f'{pessoa[chave_nome] = }')
print(f'{pessoa[chave_lista_fones][0] = }')
print(f'{pessoa[chave_lista_fones][1] = }')
print()

# Para evitar quebrar o sistema caso uma chave possa ou não existir
if pessoa.get(chave_endereco) is None: # caso a chave não exista, retorna None
  print(f'Chave "{chave_endereco}" não encontrada')
else:
  print(f'{pessoa[chave_endereco] = }')

print()

print(pessoa.get(chave_endereco, 'Posso passar um valor default caso não exista'))