import index

pessoa = index.pessoa

# ITEMS -> Retorna um dict_items, que é uma 'lista'(porém, não funciona como lista, caso queira usar como lista, tem que usar 'coersão' ou seja, converter para lista, ou tupla etc) com as chaves e os valores que tem dentro do dicionário, a chave e os valores vem em uma tupla

print(f'{pessoa.items() = }')
print(f'{type(pessoa.items()) = }')
print(f'{list(pessoa.items()) = }')
print(f'{list(pessoa.items())[0] = }')
print(f'{type(list(pessoa.items())[0]) = }') # ATENÇÃO -> Estou convertendo para lista, o PESSOA.ITEMS, então os ITEMS são uma lista, mas os items possuem seus próprios valores, que nesse caso são uma TUPLA que traz CHAVE e VALOR DA CHAVE
print(f'{type(list(list(pessoa.items())[0])) = }') # ATENÇÃO -> Agora sim estou convertendo o VALOR dos ITEMS para LIST também, prestar muita atenção nos parênteses
print(f'{list(pessoa.items())[0][0] = } = {list(pessoa.items())[0][1] = }')
print(f'{list(pessoa.items())[1][0] = } = {list(pessoa.items())[1][1] = }')
print(f'{type(list(pessoa.items())) = }')
print()

# É possível também iterar sobre PESSOA, por padrão, vai retornar as chaves, mas posso passar o que quero retornar, nesse caso, items

for chave_valor in pessoa.items():
  print(chave_valor)
  print(chave_valor[0], '=', chave_valor[1])

print()
# Outra forma de fazer esse for

for chave, valor in pessoa.items():
  print(chave, valor)