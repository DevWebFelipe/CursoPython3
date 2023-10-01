import index

pessoa = index.pessoa

# KEYS -> Retorna um dict_keys, que é uma 'lista'(porém, não funciona como lista, caso queira usar como lista, tem que usar 'coersão' ou seja, converter para lista, ou tupla etc) com as chaves que tem dentro do dicionário

print(f'{pessoa.keys() = }')
print(f'{type(pessoa.keys()) = }')
print(f'{list(pessoa.keys()) = }')
print(f'{list(pessoa.keys())[0] = }')
print(f'{list(pessoa.keys())[0] = }')
print(f'{type(list(pessoa.keys())) = }')
print()

# É possível também iterar sobre PESSOA, por padrão, vai retornar as chaves

for chave in pessoa: # poderia ser PESSOA.KEYS() também
  print(chave)